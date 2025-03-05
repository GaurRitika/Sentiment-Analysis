This is a Sentiment Analysis app , this allow users to input text like reviews , tweets , comments . After , that it will analyze the text on its sentiments like positive , negative , neutral . 
Main important feel is that it will provide sentiment scores and visualisation . It will highlight key positive and negative words.

![Screenshot 2025-03-05 173558](https://github.com/user-attachments/assets/ca9965d4-0310-4c4e-bd81-f36ff620a479)


Project Structures:
sentiment-analyzer/

│

├── venv/

├── static/

│   ├── css/                         # For CSS files

│   └── js/                          # For JavaScript files

├── templates/                       # For HTML templates

├── models/                          # For storing our trained model

└── app.py                           # Main application file

![image](https://github.com/user-attachments/assets/adab4541-d98b-48ef-8b04-32582bbaa51d)

1. NLTK Setup: We use the Natural Language Toolkit (NLTK) for text processing and sentiment analysis.
2. VADER Sentiment Analyzer: A rule-based sentiment analysis tool specifically attuned to sentiments expressed in social media.
3. Text Preprocessing: We tokenize the text, remove punctuation and stopwords.
4. Key Word Extraction: We identify important words and their sentiment.
5. Visualization: We create visual representations of the sentiment analysis results.
