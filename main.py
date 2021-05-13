# File: main.py
# Name: Kevin Thai
# Date: May 11, 2021

# This file will run the main function.

from datetime import date, datetime

import os
from youtube import YouTube

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


# Getting environment variables
key = os.getenv('KEY')
idVideo = os.getenv('ID_VIDEO')
idChannel = os.getenv('ID_CHANNEL')
#videoID = os.getenv('VIDEO_ID')

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

video = YouTube(idVideo)

def main():

    api_service = 'youtube'
    api_version = 'v3'

    # TODO: Getting credentials does not work at the moment.

    # Getting credentials and create API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #     client_secrets_file, scopes)
    # credentials = flow.run_console()
    # youtube = googleapiclient.discovery.build(
    #     api_service, api_version, credentials=credentials)
    
    # request = youtube.channels().list (
    #     part = 'contentDetails',
    #     id = video.getID()
    # )
    # response = request.execute()

    updateTitle()
    updateDesciption()


def updateTitle():
    new_title = "This video has " + str(video.getViews()) + " views!"
    video.setTitle(new_title)

def updateDesciption():
    time = datetime.now()
    time_string = time.strftime('%m/%d/%Y %H:%M:%S')

    des_ref = 'This is a personal project of mine that is inspired by Tom Scott!\n'
    des_ref_link = 'You can check out his video on this here: https://www.youtube.com/watch?v=BxV14h0kFs0\n'
    des_time = 'Last updated at ' + time_string
    new_description = des_ref + des_ref_link + des_time

    video.setDescription(new_description)

main()