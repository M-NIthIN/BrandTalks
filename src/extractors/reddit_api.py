 
import praw
import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from datetime import date
from src.utils.s3_utils import upload_to_s3
from src.utils.config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
)


def fetch_reddit_posts(brand_name, limit=1):
    posts = []
    for submission in reddit.subreddit("all").search(brand_name, limit=limit):
        post = {
            "title": submission.title,
            "selftext": submission.selftext,
            "score": submission.score,
            "upvote_ratio": submission.upvote_ratio,
            "is_video": submission.is_video,
            "created_utc": submission.created_utc,
            "num_comments": submission.num_comments,
            "gilded": submission.gilded
        }

        # Fetch top comments for each post
        submission.comments.replace_more(limit=0)  # Limit comment depth
        post["comments"] = [
            {"comment_body": comment.body, "comment_score": comment.score}
            for comment in submission.comments.list()
        ]

        posts.append(post)

    return posts

def save_reddit_data_to_s3(brand_name):
    data = fetch_reddit_posts(brand_name)
    file_name = f"{brand_name}/reddit/{date.today()}/raw_data.json"
    upload_to_s3(data, "car-talks-raw", file_name)

if __name__ == "__main__":
    pass
    post = fetch_reddit_posts('Tesla')
    print(type(post))
    sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps(post, ensure_ascii=False,indent=4))
    #save_reddit_data_to_s3("Tesla")
