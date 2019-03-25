#!/usr/bin/python3

# Developer : Hamdy Abou El Anein

# This Python 3 software display the nasa image of the day from https://www.nasa.gov/multimedia/imagegallery/iotd.html

# You must have an api key from the nasa to use it : https://api.nasa.gov/index.html#apply-for-an-api-key

# if the PIL library is missing : please install pillow to display images : pip3 install pillow

from easygui import *
import sys
import os
import wget
import json

def gui_vid():

    image = "nasa.jpg"
    msg = ("Today there's no picture !\n\n")+str(information)+str("\n\nWatch the video there : ")+str(SkyPic)
    choices = choices = ["Ok", "Reload"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Ok":
        sys.exit(0)
    elif reply == "Reload":
        start()
    else:
        sys.exit(0)

def gui_pic():

    print(("\n\n")+str(information))
    print(("\n\n")+str("Watch HD image there : ")+str(hdurl)+str("\n\n"))
    image = "pic-of-day.jpg"
    msg = ("Nasa Astronomy Picture of the Day : ")+str(pictitle)+str("\n")+str(information)
    choices = choices = ["Ok", "Reload"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Ok":
        sys.exit(0)
    elif reply == "Reload":
        start()
    else:
        sys.exit(0)

def start():
    global information,SkyPic,pictitle,hdurl

    filePath = "pic-of-day.jpg"

    if os.path.exists(filePath):
        os.remove(filePath)
    else:
        print("")

    filepath1 = "picture.json"

    if os.path.exists(filepath1):
        os.remove(filepath1)
    else:
        print("")

    # Get your own api key here in the " " # https://api.nasa.gov/index.html#apply-for-an-api-key
    apikey = "Enter-your-api-key-here"

    url = ("https://api.nasa.gov/planetary/apod?api_key="+str(apikey))

    filename = wget.download(url,out="picture.json")

    with open('picture.json', 'r') as f:  # open the json file
        pod = json.load(f)  # parse the json file

        information = pod["explanation"]
        SkyPic = pod["url"]
        pictitle = pod["title"]
        hdurl = pod["hdurl"]

        if pod["media_type"] == "image": # check if this is an image today
            url1 = (SkyPic)
            filename1 = wget.download(url1, out="pic-of-day.jpg")  # The picture is downloaded and named pic-of-day.jpg
            gui_pic()
        else:
            print(("It's a video today ! Watch the video there :")+str(SkyPic))
            gui_vid()

start()