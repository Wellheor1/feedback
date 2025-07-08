

def create_sentiment(text) -> str:
    sentiments = {"хорош": "positive", "люблю": "positive", "плохо": "negative", "ненавиж": "negative"}
    sentiment = "neutral"
    for key, value in sentiments.items():
        if key in text.lower():
            sentiment = value
    return sentiment