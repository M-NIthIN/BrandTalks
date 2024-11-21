# import requests
# import sys
# import os
# import json
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# from src.utils.s3_utils import upload_to_s3
# from src.utils.config import INSTAGRAM_ACCESS_TOKEN
# from datetime import date

# def fetch_instagram_posts(brand_name, limit=10):
#     url = f"https://graph.facebook.com/v11.0/{INSTAGRAM_USER_ID}/media"
#     params = {
#         "access_token": INSTAGRAM_ACCESS_TOKEN,
#         "fields": "id,caption,media_url,timestamp,like_count,comments_count",
#         "limit": limit
#     }
#     response = requests.get(url, params=params)
#     posts = response.json().get("data", [])
#     return posts

# def save_instagram_data_to_s3(brand_name):
#     data = fetch_instagram_posts(brand_name)
#     file_name = f"{brand_name}/instagram/{date.today()}/raw_data.json"
#     upload_to_s3(data, "car-talks-raw", file_name)

# if __name__ == "__main__":
#     save_instagram_data_to_s3("Tesla")




import requests
import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.utils.s3_utils import upload_to_s3
from src.utils.config import INSTAGRAM_ACCESS_TOKEN
from datetime import date


# API Endpoint to test the connection (basic user info)
URL = "https://graph.facebook.com/v17.0/me?fields=id,name&access_token=" + INSTAGRAM_ACCESS_TOKEN
print(URL)
def test_instagram_api():
    try:
        response = requests.get(URL)
        # Parse the JSON response
        data = response.json()
        print(data)

        if response.status_code == 200:
            print("Connected Successfully!")
            print("User Info:")
            print(f"ID: {data['id']}")
            print(f"Name: {data['name']}")
        else:
            print("Failed to connect.")
            print(f"Error: {data.get('error', {}).get('message', 'Unknown error')}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Run the test
    test_instagram_api()
