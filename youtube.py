# File: youtube.py
# Name: Kevin Thai
# Date: May 11, 2021

# This file will hold the information of a YouTube video.

class YouTube:
    def __init__(self):
        self.title = ""
        self.views = 0
        self.thumbnail
        self.id = ""
    
    # setter methods
    def setTitle(self, title):
        self.title = title
        print("Title set successfully to ", self.title)

    def setViews(self, views):
        self.views = views
        print("Views set successfully to ", self.views)

    def setThumbnail(self, thumbnail):
        self.thumbnail = thumbnail
        print("Thumbnail set successfully to ", self.thumbnail)

    def setID(self, id):
        self.id = id
        print("ID set successfully to ", self.id)

    # getter methods
    def getTitle(self):
        return self.title

    def getViews(self):
        return self.views

    def getThumbnail(self):
        return self.thumbnail

    def getID(self):
        return self.id
    