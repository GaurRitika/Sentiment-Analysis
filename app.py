from flask import Flask, render_template, request
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import string
from collections import Counter
import random
import re

app = Flask(__name__)

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Set up stopwords
stop_words = set(stopwords.words('english'))

def simple_tokenize(text):
    # Simple tokenization without relying on punkt_tab
    # Split by spaces and remove punctuation
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def simple_sentence_tokenize(text):
    # Simple sentence tokenization without relying on punkt
    # Split by common sentence endings
    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if s.strip()]

def preprocess_text(text):
    # Tokenize into words using simple tokenization
    words = simple_tokenize(text.lower())
    
    # Remove punctuation and stopwords
    words = [word for word in words if word not in string.punctuation and word not in stop_words]
    
    return words

def get_key_words(text, sentiment_scores):
    words = preprocess_text(text)
    
    # Get sentiment for each word
    word_sentiments = {}
    for word in words:
        if len(word) > 2:  # Only consider words with more than 2 characters
            score = sid.polarity_scores(word)
            if score['compound'] > 0.3:
                word_sentiments[word] = 'positive'
            elif score['compound'] < -0.3:
                word_sentiments[word] = 'negative'
            else:
                word_sentiments[word] = 'neutral'
    
    # Count word frequencies
    word_counts = Counter(words)
    
    # Get top words
    top_words = []
    for word, count in word_counts.most_common(20):
        if word in word_sentiments:
            # Calculate font size based on frequency (min: 14, max: 30)
            size = min(30, max(14, 14 + count * 2))
            top_words.append({
                'text': word,
                'sentiment': word_sentiments[word],
                'size': size
            })
    
    # Shuffle to create a more randomized word cloud effect
    random.shuffle(top_words)
    
    return top_words

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        
        # Get sentiment scores
        sentiment_scores = sid.polarity_scores(text)
        
        # Determine overall sentiment
        compound_score = sentiment_scores['compound']
        if compound_score >= 0.05:
            sentiment = "Positive"
            sentiment_class = "positive"
        elif compound_score <= -0.05:
            sentiment = "Negative"
            sentiment_class = "negative"
        else:
            sentiment = "Neutral"
            sentiment_class = "neutral"
        
        # Get key words
        key_words = get_key_words(text, sentiment_scores)
        
        # Count words and sentences
        word_count = len(preprocess_text(text))
        sentence_count = len(simple_sentence_tokenize(text))
        
        return render_template('index.html', 
                              text=text,
                              sentiment=sentiment,
                              sentiment_class=sentiment_class,
                              compound_score=round(compound_score, 2),
                              pos_score=round(sentiment_scores['pos'], 2),
                              neu_score=round(sentiment_scores['neu'], 2),
                              neg_score=round(sentiment_scores['neg'], 2),
                              key_words=key_words,
                              word_count=word_count,
                              sentence_count=sentence_count)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
