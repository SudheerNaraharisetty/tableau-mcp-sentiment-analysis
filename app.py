from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# This endpoint is for discovery by Tableau
@app.route('/', methods=['GET'])
def index():
    return jsonify({'name': 'Sentiment Analysis Extension', 'version': '1.0'})

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        # Get the data from the request
        data = request.get_json()

        # Extract the script and data from the request
        script = data.get('script', '')
        data_args = data.get('data', {})

        # Check if the script is for sentiment analysis
        if script != '/sentiment':
            return jsonify({'error': 'Unknown script'}), 400

        # Get the text data from the arguments
        # Tableau sends data as a dictionary of lists, e.g., {'_arg1': ['text1', 'text2']}
        text_data = next(iter(data_args.values()), [])

        # Perform sentiment analysis on each text entry
        results = []
        for text in text_data:
            blob = TextBlob(str(text))
            if blob.sentiment.polarity > 0:
                sentiment = 'Positive'
            elif blob.sentiment.polarity < 0:
                sentiment = 'Negative'
            else:
                sentiment = 'Neutral'
            results.append(sentiment)

        # Return the results in the format Tableau expects
        return jsonify(results)

    except Exception as e:
        # Log the error for debugging
        print(f"Error during evaluation: {e}")
        # Return a generic error message to Tableau
        return jsonify({'error': 'An error occurred on the server'}), 500

if __name__ == '__main__':
    # Running on 0.0.0.0 makes it accessible from other machines on the network
    app.run(host='0.0.0.0', port=5001, debug=True)