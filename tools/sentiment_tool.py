import joblib
import os

# Load saved sentiment model
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "sentiment_model.pkl")
sia = joblib.load(model_path)

def analyze_sentiment(text: str):
    try:
        prediction = sia.polarity_scores(text)
        # Simplified result
        emotion = "positive" if prediction["compound"] > 0.05 else "negative" if prediction["compound"] < -0.05 else "neutral"
        
        return {
            "compound": prediction["compound"],
            "positive": prediction["pos"],
            "negative": prediction["neg"],
            "neutral": prediction["neu"],
            "detected_emotion": emotion
        }
    except Exception as e:
        return {"error": f"Sentiment analysis failed: {str(e)}"}