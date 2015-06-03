#!/usr/bin/python

import json
import sys

import YoutubeCrawler as YTC

class UdacityDatasetFetcher(object):

    def __init__(self, bridgeFile, metadataFile):
        """ bridgeFile: path to file making the link between metadata ID and playlistID
            metadataFile: path to file containing all the metadata 
        """
        self.bridgeFile = bridgeFile
        self.bridgeData = None
        self.metadataFile = metadataFile
        self.metadataData = None

    def read_metadataFile(self):
        """ Read the metadata json file.
        """
        with open(self.metadataFile) as fstream:
            self.metadataData = json.load(fstream)

    def read_bridgeFile(self):
        """ Import the content of the bridgeFile into a list
        """
        with open(self.bridgeFile,'r') as fstream:
            self.bridgeData = []
            for line in fstream:
                line = line.strip('\n').split('|')
                courseName = line[0]
                courseID = int(line[1])
                coursePlaylists = line[2:]

                self.bridgeData.append((courseName, courseID, coursePlaylists))

    def fetch_data(self):
        """ Call the youtubeCrawler module to fetch the subtitles, wrap the data with the 
            metadata. Save the whole as Udacity_dataset.json.
        """
        if self.bridgeData == None:
            self.read_bridgeFile()
        if self.metadataData == None:
            self.read_metadataFile()

        courses = []

        try:

            for courseName, courseID, coursePlaylists in self.bridgeData:

                #print "Fetching",courseName
                metadata = self.metadataData["courses"][courseID]
                subtitlesList = []

                for coursePlaylist in coursePlaylists:
                    crawler = YTC.YoutubeCrawler(coursePlaylist)
                    crawler.get_all_subtitles()
                    subtitlesList += crawler.allSubtitles

                print "Udacity: ",courseName," fetched."
                courses.append({"metadata":metadata, "subtitles":subtitlesList})

        except:
            finalJSON = {"courses":courses}
            with open('Udacity_dataset.json', 'w') as outfile:
                json.dump(finalJSON, outfile)
            raise

        finalJSON = {"courses":courses}

        with open('Udacity_dataset.json', 'w') as outfile:
            json.dump(finalJSON, outfile)

if __name__ == "__main__":

    datasetFetcher = UdacityDatasetFetcher('metadata_bridge.txt','Udacity_metadata.json')
    datasetFetcher.fetch_data()
