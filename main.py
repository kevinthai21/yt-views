# File: main.py
# Name: Kevin Thai
# Date: May 11, 2021

# This file will run the main function.

from datetime import date, datetime

import os
from dotenv import load_dotenv
from youtube import YouTube

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

load_dotenv('#.env')

# Getting environment variables
key = os.getenv('KEY')
idVideo = os.getenv('ID_VIDEO')
idChannel = os.getenv('ID_CHANNEL')
client = os.getenv('CLIENT')
category = os.getenv('CATEGORY')

scopes = ["https://www.googleapis.com/auth/youtubepartner",
            "https://www.googleapis.com/auth/youtube",
            "https://www.googleapis.com/auth/youtube.force-ssl"]

video = YouTube(idVideo)
def main():

    api_service = 'youtube'
    api_version = 'v3'
    client_secrets_file = "client_secret_514071497858-gg76s3kneij8de17lon4sfbvc0amnlhp.apps.googleusercontent.com.json"

    # Getting credentials and create API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service, api_version, credentials=credentials)


    request_read = youtube.videos().list(
        part = "statistics",
        id = video.id
    )

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

    #TODO: Get the view count.

    response = request_read.execute()
    # print(response.items)
    # print(response.items[0])
    # print("Response: " , response.items[0].statistics.viewCount)

    response = request_update.execute()

    # updateVideo()

def updateTitle():
    new_title = "[TEST] "+"This video has " + str(video.getViews()) + " views!"
    video.setTitle(new_title)
    return(video.title)

def updateDesciption():
    time = datetime.now()
    time_string = time.strftime('%m/%d/%Y %H:%M:%S')

    des_ref = 'This is a personal project of mine that is inspired by Tom Scott!\n'
    des_ref_link = 'You can check out his video on this here: https://www.youtube.com/watch?v=BxV14h0kFs0\n'
    des_time = 'Last updated at ' + time_string
    new_description = des_ref + "\n" + des_ref_link + "\n" + des_time

    video.setDescription(new_description)
    return(video.description)

def updateVideo():
    updateTitle()
    updateDesciption()

main()