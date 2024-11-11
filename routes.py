from fastapi import APIRouter, HTTPException
from db import store_video_details, get_video_statistics
from utils import extract_video_id, build_youtube_service

# Initialize the APIRouter
router = APIRouter()

@router.post("/get_video_details/")
async def get_video_details(youtube_url: str):
    video_id = extract_video_id(youtube_url)
    if not video_id:
        raise HTTPException(status_code=400, detail="Invalid YouTube URL")

    youtube = build_youtube_service()

    # Get video statistics and snippet (which contains title)
    request = youtube.videos().list(part="snippet,statistics", id=video_id)  # Fetch both snippet and statistics
    response = request.execute()

    if "items" not in response or not response["items"]:
        raise HTTPException(status_code=404, detail="Video not found")

    video_info = response["items"][0]
    stats = video_info["statistics"]
    title = video_info["snippet"]["title"]  # Extract title from snippet

    # Prepare video data
    video_data = {
        "youtube_url": youtube_url,
        "video_id": video_id,
        "title": title,  # Include title
        "views": stats.get("viewCount", "N/A"),
        "likes": stats.get("likeCount", "N/A"),
        "comments": stats.get("commentCount", "N/A")
    }

    # Store the data in MongoDB
    store_video_details(video_data)

    return {
        "message": "Video details stored successfully",
        "data": video_data
    }