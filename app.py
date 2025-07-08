
from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def get_sentiment():
    data = request.get_json()
    text_to_analyze = data.get('text', '')
    
    if not text_to_analyze:
        return jsonify({'error': 'No text provided for analysis'}), 400

    blob = TextBlob(text_to_analyze)
    
    # Classify sentiment
    if blob.sentiment.polarity > 0:
        sentiment = 'Positive'
    elif blob.sentiment.polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
        
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(port=5000)
