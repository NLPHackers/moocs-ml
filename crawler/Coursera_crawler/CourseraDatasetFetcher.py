#!/usr/bin/python

import json
import sys
import urllib2
import time
import random as rnd

class CourseraDatasetFetcher(object):

    def __init__(self, homelinkFile):
        """ 
        """
        self.homelinkFile = homelinkFile
        self.homelinkData = None

    def read_homeLink_file(self):
        """
        """
        with open(self.homelinkFile) as fstream:
            self.homelinkData = json.load(fstream)

    def fetch_subtitles(self, startIdx=None, endIdx=None):
        """
        """
        if self.homelinkData == None:
            self.read_homeLink_file()

        courseSubtitles = {}

        try:

            if startIdx == None:
                startIdx = 0
            if endIdx == None:
                endIdx = len(self.homelinkData["elements"])

            for idx in xrange(startIdx, endIdx):
                
                element = self.homelinkData["elements"][idx]
                if "homeLink" in element:
                    homelink = element["homeLink"]
                else:
                    continue
                courseID = element["courseId"]

                print "Start pulling courseId", courseID

                videoCount = 0
                baseURL = homelink + "lecture/subtitles?q="

                allSubtitles = []

                for NN in xrange(150):
                    NN*=2
                    URL = baseURL + str(NN) + "_en&format=txt"
                    time.sleep(rnd.random()*0.05)
                    try:
                        data = urllib2.urlopen(URL).read()
                        print "NN=", NN, " subtitles found."
                        allSubtitles.append(data)
                    except:
                        print "NN=", NN, " missed."
                        videoCount -= 1
                    videoCount += 1

                    if videoCount >= 75:
                        break

                courseSubtitles[courseID] = allSubtitles

                print "courseID:", courseID," pulled: ", len(allSubtitles),"   idx:",idx

        except:

            with open('Coursera_dataset_'+str(startIdx)+'_'+str(endIdx)+'.json', 'w') as outfile:
                json.dump(courseSubtitles, outfile)
            raise

        with open('Coursera_dataset_'+str(startIdx)+'_'+str(endIdx)+'.json', 'w') as outfile:
                json.dump(courseSubtitles, outfile)


if __name__ == "__main__":

    startIdx = int(sys.argv[1]) 
    endIdx = int(sys.argv[2])

    datasetFetcher = CourseraDatasetFetcher("homelinks.json")
    datasetFetcher.fetch_subtitles(startIdx, endIdx)

