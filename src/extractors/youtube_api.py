import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from src.utils.s3_utils import upload_to_s3

from src.utils.config import YOUTUBE_API_KEY
from datetime import date

def fetch_youtube_videos(brand_name, max_results=15):

    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    search_request = youtube.search().list(
        q=brand_name,
        part="snippet",
        maxResults=max_results,
        type="video"
    )
    search_response = search_request.execute()
    videos = []
    for item in search_response.get("items", []):
        video_id = item["id"]["videoId"]
        video_data = {
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "published_at": item["snippet"]["publishedAt"],
            "channel_title": item["snippet"]["channelTitle"],
            "video_id": video_id
        }

        stats_request = youtube.videos().list(
            part="statistics",
            id=video_id
        )
        stats_response = stats_request.execute()
        if stats_response["items"]:
            stats = stats_response["items"][0]["statistics"]
            video_data["views"] = stats.get("viewCount", "0")
            video_data["likes"] = stats.get("likeCount", "0")
            video_data["comments"] = stats.get("commentCount", "0")
        else:
            video_data["views"] = "N/A"
            video_data["likes"] = "N/A"
            video_data["comments"] = "N/A"

        content_details_request = youtube.videos().list(
            part="contentDetails",
            id=video_id
        )
        content_details_response = content_details_request.execute()
        if content_details_response["items"]:
            duration = content_details_response["items"][0]["contentDetails"]["duration"]
            video_data["duration"] = duration  
        else:
            video_data["duration"] = "N/A"

        
        try:
            transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
            #transcript_text = " ".join([entry['text'] for entry in transcript_data])
            video_data["transcript"] = transcript_data
        except Exception as e:
            video_data["transcript"] = f"Error: Could not retrieve transcript. Reason: {str(e)}"

        videos.append(video_data)

    return videos

def save_youtube_data_to_s3(brand_name):
    data = fetch_youtube_videos(brand_name)
    file_name = f"{brand_name}/youtube/{date.today()}/raw_data.json"
    upload_to_s3(data, "car-talks-raw", file_name)

if __name__ == "__main__":
    #save_youtube_data_to_s3("Tesla")
    vid = fetch_youtube_videos('Tesla')
    sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps(vid, ensure_ascii=False,indent=4))
    with open("sample.json", "w", encoding="utf-8") as outfile:
        json.dump(vid, outfile, ensure_ascii=False, indent=4)
