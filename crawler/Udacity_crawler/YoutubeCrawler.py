#!/usr/bin/python

import json
import urllib2
import urlparse
import xml.dom.minidom as xml
import time
import random as rnd

class YoutubeCrawler(object):
    """ Class to hadle youtube playlists, from getting the urls of all the videos to
        extracting the subtitles.
    """

    def __init__(self, playlistID):
        self.playlistID = playlistID
        self.allUrls = None
        self.allSubtitles = None

    def get_all_subtitles(self):
        """ Get the english subtitles for each video in the playlist.
        """
        if self.allUrls == None:
            self.get_videos_urls()

        videoIDs = []
        allSubtitles = []

        for videoURL in self.allUrls:
            url_data = urlparse.urlparse(videoURL)
            query = urlparse.parse_qs(url_data.query)
            videoIDs.append(query["v"][0])

        for videoID in videoIDs:
            #print "en?",
            if has_english_subtitles(videoID):
                queryURL = "https://www.youtube.com/api/timedtext?v="+videoID+"&lang=en"
                try:
                    xmlData = xml.parse(urllib2.urlopen(queryURL))
                    time.sleep(rnd.random()*0.007)
                    allSubtitles.append(get_subtitles(xmlData))
                except:
                    #print "error",
                    allSubtitles.append("")
                #print "y_get",
            else:
                allSubtitles.append("")
            #print "."

        self.allSubtitles = allSubtitles

    def get_videos_urls(self):
        """ Uses youtube API to get the urls of all the videos inside the playlist.
        """
        tail = "?max-results=50&v=2&alt=json"
        queryURL = "https://gdata.youtube.com/feeds/api/playlists/"+self.playlistID+tail

        allUrls = []

        try:
            data = json.load(urllib2.urlopen(queryURL))
        except:
            raise

        moreToPull = True
        while moreToPull:

            allUrls += add_videos_urls(data)

            nextURL = has_next(data)
            if nextURL != False:
                moreToPull = True
                queryURL = nextURL
                data = json.load(urllib2.urlopen(queryURL))
                time.sleep(rnd.random()*0.007)
            else:
                moreToPull = False

        self.allUrls = allUrls

    def save_as_json(self):
        """ Save all the subtitles as a big json file:
                video url : subtitles 
        """
        assert(len(self.allSubtitles) == len(self.allUrls))
        jsonData = {videoURL : subtitles for videoURL, subtitles in zip(self.allUrls,self.allSubtitles)}
        with open(self.playlistID+'.json', 'w') as outfile:
            json.dump(jsonData, outfile)

def get_subtitles(xmlData):
    """ Extract all the subtitles from the xml data file.
    """
    allSubtitles = ""
    transcript = xmlData.getElementsByTagName("transcript")[0]
    for text in transcript.getElementsByTagName("text"):
        if text.firstChild != None:
            allSubtitles += " "+text.firstChild.data

    return allSubtitles

def has_english_subtitles(videoID):
    """ Return True if the video has english subtitles available
    """
    queryURL = "http://video.google.com/timedtext?type=list&v="+videoID
    xmlData = xml.parse(urllib2.urlopen(queryURL))
    time.sleep(rnd.random()*0.007)

    return " lang_code=\"en\"" in xmlData.toprettyxml()

def add_videos_urls(jsonData):
    """ Get all the videos urls from the json data. Return a list with all of them.
    """
    allUrls = []
    for entry in jsonData["feed"]["entry"]:
        allUrls.append(entry["link"][0]["href"])
    return allUrls

def has_next(jsonData):
    """ Return the next url to query if the json contains the "next" flag, else false
    """
    for link in jsonData["feed"]["link"]:
        if link["rel"] == "next":
            return link["href"]
    return False

if __name__ == "__main__":

    myCrawler = YoutubeCrawler("PLAwxTw4SYaPmtf5v3hefG5seVynUtV9T8")#YoutubeCrawler("PLAwxTw4SYaPnMwH5-FNkErnnq_aSy706S")
    myCrawler.get_all_subtitles()
    myCrawler.save_as_json()
 
    for url in myCrawler.allUrls:
        print url
    print len(myCrawler.allUrls)," urls pulled from youtube."
