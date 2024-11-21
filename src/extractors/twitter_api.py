import tweepy
import time
import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from datetime import date
from src.utils.s3_utils import upload_to_s3
from src.utils.config import (
    TWITTER_BEARER_TOKEN, 
    TWITTER_ACCESS_TOKEN, 
    TWITTER_ACCESS_TOKEN_SECRET, 
    TWITTER_API_KEY, 
    TWITTER_API_KEY_SECRET
)

client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_KEY_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def retrieve_tweets(brand_name, max_results=5):
    query = f"{brand_name} -is:retweet lang:en"
    tweet_fields = [
        "id", "text", "created_at", "public_metrics",
        "entities", "context_annotations", "geo",
        "lang", "possibly_sensitive", "source"
    ]

    tweets_data = []
    retries = 6  

    for attempt in range(retries):
        try:
            for tweet in tweepy.Paginator(
                client.search_recent_tweets,
                query=query,
                tweet_fields=tweet_fields,
                max_results=max_results 
            ).flatten(limit=max_results):

                tweet_info = {
                    "Tweet ID": tweet.id,
                    "Created At": tweet.created_at,
                    "Full Text": tweet.text,
                    "Source": tweet.source,
                    "Language": tweet.lang,
                    "Favorite Count": tweet.public_metrics["like_count"],
                    "Retweet Count": tweet.public_metrics["retweet_count"],
                    "Is Quoted": tweet.public_metrics.get("quote_count", 0) > 0,
                    "Entities": tweet.entities,
                    "Hashtags": [hashtag["tag"] for hashtag in tweet.entities.get("hashtags", [])],
                    "URLs": [url["expanded_url"] for url in tweet.entities.get("urls", [])],
                    "Coordinates": tweet.geo,
                    "Possibly Sensitive": tweet.possibly_sensitive
                }
                tweets_data.append(tweet_info)

            break

        except tweepy.errors.TooManyRequests as e:
            wait_time = 5 * (2 ** attempt)  
            print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

    return tweets_data

def save_tweets_to_s3(brand_name):
    data = retrieve_tweets(brand_name)
    file_name = f"{brand_name}/twitter/{date.today()}/raw_data.json"
    json_data = json.dumps(data, indent=4, default=str)
    upload_to_s3(json_data, "car-talks-raw", file_name)

if __name__ == "__main__":
    tweets = retrieve_tweets("Tesla")
    print(json.dumps(tweets, indent=4))
    # Uncomment below to save tweets to S3
    # save_tweets_to_s3("Tesla")
