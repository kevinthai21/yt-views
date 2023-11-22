# File: main.py
# Name: Kevin Thai
# Date: May 11, 2021

# This file will run the main function.

from datetime import date, datetime

import os
from dotenv import load_dotenv
from youtube import YouTube
from googleapiclient.http import MediaFileUpload

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

load_dotenv('.env')

# Getting environment variables
key = os.getenv('KEY')
idVideo = os.getenv('ID_VIDEO')
idChannel = os.getenv('ID_CHANNEL')
client = os.getenv('PAST_CLIENT')
category = os.getenv('CATEGORY')


scopes = ["https://www.googleapis.com/auth/youtubepartner",
            "https://www.googleapis.com/auth/youtube",
            "https://www.googleapis.com/auth/youtube.force-ssl"]

# YouTube object that will hold details of the video
video = YouTube(idVideo)

thumbnail_path = "thumbnail_base.png"

# Function: main()
# The function that will create an API client and use the logic to update the 
# title and description.
def main():

    api_service = 'youtube'
    api_version = 'v3'
    client_secrets_file = client

    # Getting credentials and create API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credential = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service, api_version, credentials=credential)

    # Create a function that will read the details of the video
    request_read = youtube.videos().list(
        part = "statistics",
        id = video.id,
        
    )

    response = request_read.execute()
    video.setViews(int(response['items'][0]['statistics']['viewCount']))

    # Create a function that will update the details of the video
    request_update = youtube.videos().update(
        part="snippet, contentDetails",
        body={
            "id": video.id,
        
            "snippet": {
                "description": updateDesciption(),
                "categoryId": category,
                "title": updateTitle()
            }
        }
    )
    response = request_update.execute()

    # Create a function that will update the thumbnail of the video.
    request_thumbnail = youtube.thumbnails().set (
        videoId = video.id,
        # access_token = access,
        media_body = MediaFileUpload(thumbnail_path)
    )
    response = request_thumbnail.execute()

# Function: createThumbnail()
# It will create a image for the video.
def createThumbnail():
    return

# Function: updateTitle()
# It will update the title of the video with the number of views!
def updateTitle():
    new_title = "[TEST] "+" This video has " + str(video.getViews()) + " views!"
    video.setTitle(new_title)
    return(video.title)

# Function: updateDescription()
# It will update the description of the video, with a revised draft; and showing
# the last time it has been updated.
def updateDesciption():

    # Gets the current time
    time = datetime.now()
    time_string = time.strftime('%m/%d/%Y %H:%M:%S')

    des_ref = 'This is a personal project of mine that is inspired by Tom Scott!\n'
    des_ref_link = 'You can check out his video on this here: https://www.youtube.com/watch?v=BxV14h0kFs0\n'
    des_time = 'Last updated at ' + time_string + " PT"
    new_description = des_ref + "\n" + des_ref_link + "\n" + des_time

    video.setDescription(new_description)
    return(video.description)

# Function: updateThumbnail()
# It will updaate the thumbnail of the video.
def updateThumbnail(picture):
    video.setThumbnail(picture)
    return

main()