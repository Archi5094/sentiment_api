# Sentiment Analysis API 🚀

This project is a **Sentiment Analysis API** built with **Flask** and deployed on **Google Cloud Run**.  
It uses **VADER Sentiment Analyzer** to classify text into **Positive**, **Negative**, or **Neutral**.

---

## 📂 Project Structure
├── app.py                     # Flask API code  
├── requirements.txt           # Dependencies  
├── Sentiment_analysis.ipynb   # Notebook for testing/exploration  

---

## ⚡ Features
- Simple REST API with `/sentiment` endpoint  
- Returns sentiment label (**Positive / Negative / Neutral**) and raw sentiment scores  
- Deployable on **Google Cloud Run**  
- Easy to test via **cURL** or browser  

---

## 🛠️ Installation (Run Locally)

1. Clone the repository:
   git clone https://github.com/Archi5094/sentiment-api.git
   cd sentiment-api

2. Create a virtual environment & install dependencies:
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

3. Run the Flask app:
   python app.py

4. Open in browser:
   http://127.0.0.1:8080/

---

## 🌐 API Usage

### Endpoint: `/sentiment`
- Method: POST  
- Content-Type: application/json  

Example Request:
curl -X POST https://<your-cloud-run-url>/sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this project!"}'

Example Response:
{
  "text": "I love this project!",
  "score": 0.6696,
  "sentiment": "Positive",
  "raw_scores": {
    "neg": 0.0,
    "neu": 0.4,
    "pos": 0.6,
    "compound": 0.6696
  }
}

---

## 🚀 Deployment on Google Cloud Run

1. Build container:
   gcloud builds submit --tag gcr.io/<PROJECT-ID>/sentiment-api

2. Deploy to Cloud Run:
   gcloud run deploy sentiment-api \
     --image gcr.io/<PROJECT-ID>/sentiment-api \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated

3. You’ll get a public URL like:
   https://sentiment-api-xxxxxx-uc.a.run.app

---
