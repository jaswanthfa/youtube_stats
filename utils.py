import re
from googleapiclient.discovery import build
import os
# Function to extract video ID from a YouTube URL
def extract_video_id(youtube_url):
    video_id = re.findall(r'(?:v=|\/)([0-9A-Za-z_-]{11})', youtube_url)
    if video_id:
        return video_id[0]
    return None

# Function to build the YouTube API client
def build_youtube_service():
    API_KEY = "AIzaSyCpNWXEP2BvP0LFA4v4o-UfoQ_6akPfwkA"  # Make sure you have your API key in .env
    return build('youtube', 'v3', developerKey=API_KEY)