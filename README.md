This is a Sentiment Analysis app , this allow users to input text like reviews , tweets , comments . After , that it will analyze the text on its sentiments like positive , negative , neutral . 
Main important feel is that it will provide sentiment scores and visualisation . It will highlight key positive and negative words.

![image](https://github.com/user-attachments/assets/508735f2-fda9-4a5f-9cfe-07db85f37b02)

![image](https://github.com/user-attachments/assets/da214fbc-0050-42c0-b861-42e705e0f531)


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


1. NLTK Setup: We use the Natural Language Toolkit (NLTK) for text processing and sentiment analysis.
2. VADER Sentiment Analyzer: A rule-based sentiment analysis tool specifically attuned to sentiments expressed in social media.
3. Text Preprocessing: We tokenize the text, remove punctuation and stopwords.
4. Key Word Extraction: We identify important words and their sentiment.
5. Visualization: We create visual representations of the sentiment analysis results.
