# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def insertThreadObj(youtube, videoId):
    request = youtube.commentThreads().insert(
        part="snippet",
        body={
            "snippet": {
                "videoId": videoId,
                "topLevelComment": {
                    "snippet": {
                        "textOriginal": "This is a normal comment"
                    }
                }
            }
        }
    )
    return request


def insertReplyObj(youtube, parentId):
    request = youtube.comments().insert(
        part="snippet",
        body={
            "snippet": {
                "parentId": parentId,
                "textOriginal": "Hey, check out my new website!! This site is about kids stuff. hot-teens24.online"
            }
        }
    )

    return request


def ask_scan_mode(youtube):
    spam_type = input(
        "Choose from following spam type: \n 1 - 50 comments with 50 replies \n 2 - 100 comments \n")

    # videoId = "dkp-KrI13ds"

    video_id = input("Enter video id: \n")
    count = 0
    comments = []

    if spam_type == '1':
        try:
            print("Spam in progress ...")
            for _ in range(count):
                comments.append(
                    insertThreadObj(youtube, video_id).execute())

            for c in comments:
                insertReplyObj(youtube, c['id']).execute()

            print("Spam successful")
        except Exception as e:
            print(e)
    elif spam_type == '2':
        print("No scan mode set yet")

    else:
        print("Invalid scan mode")


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    ask_scan_mode(youtube)


if __name__ == "__main__":
    main()
