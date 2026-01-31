from nltk.sentiment import SentimentIntensityAnalyzer
import os
import joblib
sia=SentimentIntensityAnalyzer()
sample_texts={
    "I am very happy today",
    "this is the worst thing ever",
    "I feel okay, noot too bad"
}
print ("testinng sentiment detection:")
for text in sample_texts:
    sentiment=sia.polarity_scores(text)
    print(f"Text: {text} -> sentiment: {sentiment}")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


models_dir = os.path.join(BASE_DIR, "..", "models")
os.makedirs(models_dir, exist_ok=True)

model_path = os.path.join(models_dir, "sentiment_model.pkl")

joblib.dump(sia, model_path)

print("Model saved successfully at models/sentiment_model.pkl")