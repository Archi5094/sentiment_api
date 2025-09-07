from flask import Flask, request, jsonify, render_template_string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

# HTML template with CSS and JS
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sentiment Analyzer</title>
<style>
  body {
    font-family: Arial, sans-serif;
    background: linear-gradient(to right, #f5f7fa, #c3cfe2);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  .container {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    width: 400px;
    text-align: center;
  }
  input[type=text] {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border-radius: 8px;
    border: 1px solid #ccc;
    font-size: 16px;
  }
  button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 12px 20px;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
  }
  button:hover {
    background-color: #45a049;
  }
  .result {
    margin-top: 20px;
    font-size: 18px;
    font-weight: bold;
  }
</style>
</head>
<body>
<div class="container">
  <h2>Sentiment Analyzer</h2>
  <input type="text" id="textInput" placeholder="Type your sentence here">
  <button onclick="analyzeSentiment()">Submit</button>
  <div class="result" id="result"></div>
</div>

<script>
async function analyzeSentiment() {
    const text = document.getElementById('textInput').value;
    if (!text) return alert('Please enter some text!');

    const response = await fetch('/sentiment', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text})
    });

    const data = await response.json();
    document.getElementById('result').innerText = 
        `Sentiment: ${data.sentiment} (Score: ${data.score})`;
}
</script>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_PAGE)

@app.route("/sentiment", methods=["POST"])
def sentiment():
    data = request.get_json() or {}
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "no text provided"}), 400

    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        label = "Positive"
    elif compound <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"

    return jsonify({
        "text": text,
        "score": compound,
        "sentiment": label,
        "raw_scores": scores
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
