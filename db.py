from pymongo import MongoClient
from datetime import datetime
import os

# Replace this with your remote MongoDB URI if needed
client = MongoClient("mongodb+srv://jash:Jash123@cluster0.sambn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["youtube_data"]
collection = db["video_details"]

def store_video_details(video_data):
    # Add timestamp to the data
    video_data["timestamp"] = datetime.utcnow()
    result = collection.insert_one(video_data)
    video_data["_id"] = str(result.inserted_id)
    return video_data

def get_video_statistics(video_id):
    # Fetch data from MongoDB by video_id
    return collection.find_one({"video_id": video_id})