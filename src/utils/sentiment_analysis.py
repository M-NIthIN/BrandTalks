from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_analyzer(text)
    score = result[0]["score"] if result[0]["label"] == "POSITIVE" else -result[0]["score"]
    return score

if __name__=="__main__":
    print(analyze_sentiment("hi how are you?"))
