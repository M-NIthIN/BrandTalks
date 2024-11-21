from transformers import pipeline
import matplotlib.pyplot as plt
import json

sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased")

def split_transcript(transcript, max_length=512):
    # Tokenize the transcript and split it into smaller segments of max_length tokens
    words = transcript.split(" ")
    segments = []
    for i in range(0, len(words), max_length):
        segments.append(" ".join(words[i:i+max_length]))  # Ensure each segment is within the max_length
    return segments

def analyze_sentiment(transcript, max_length=512):
    if not transcript:
        return []  # Return an empty list if transcript is missing or empty

    segments = split_transcript(transcript, max_length)
    sentiment_scores = []

    for segment in segments:
        result = sentiment_analyzer(segment)
        score = result[0]["score"] if result[0]["label"] == "POSITIVE" else -result[0]["score"]
        sentiment_scores.append(score)

    return sentiment_scores

def plot_sentiment(sentiment_data):
    for video in sentiment_data:
        times = [s["time"] for s in video["sentiment_over_time"]]
        scores = [s["score"] for s in video["sentiment_over_time"]]
        plt.plot(times, scores, label=video["title"])

    plt.xlabel("Time Intervals")
    plt.ylabel("Sentiment Score")
    plt.title("Sentiment Tone Over Videos")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    with open("sample.json", "r") as file:
        data = json.load(file)

    sentiment_data = []
    for video in data:
        if "transcript" in video and video["transcript"]:  # Check if transcript exists and is not empty
            sentiment_scores = analyze_sentiment(video["transcript"])
            if sentiment_scores:  # Only process if sentiment scores are found
                sentiment_over_time = [{"time": f"{i*30}-{(i+1)*30}s", "score": sentiment_scores[i]} for i in range(len(sentiment_scores))]
                sentiment_data.append({
                    "video_id": video["video_id"],
                    "title": video["title"],
                    "sentiment_over_time": sentiment_over_time
                })
            else:
                print(f"No transcript data to analyze for video: {video['title']}")
        else:
            print(f"Transcript not available for video: {video['title']}")

    plot_sentiment(sentiment_data)
