import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')

# Verify the downloads
try:
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    
    # Test tokenization
    word_tokenize("Testing if punkt is working.")
    
    # Test stopwords
    stopwords.words('english')
    
    # Test sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    sid.polarity_scores("Test")
    
    print("All NLTK data downloaded and verified successfully!")
except Exception as e:
    print(f"Error during verification: {e}")
    print("Please try downloading again with:")
    print("import nltk")
    print("nltk.download()")
