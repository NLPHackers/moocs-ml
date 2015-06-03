#!/usr/bin/python

import sys 
import json


class CourseraDatasetMerger(object):

    def __init__(self, subtitlesFile, metadataFile):
        self.subtitlesFile = subtitlesFile
        self.subtitlesData = None
        self.metadataFile = metadataFile
        self.metadataData = None

    def read_subtitlesFile(self):
        """
        """
        with open(self.subtitlesFile) as fstream:
            self.subtitlesData = json.load(fstream)

    def read_metadataFile(self):
        """
        """
        with open(self.metadataFile) as fstream:
            self.metadataData = json.load(fstream)

    def zip_subtitles_metadata(self):
        """
        """
        if self.metadataData == None:
            self.read_metadataFile()
        if self.subtitlesData == None:
            self.read_subtitlesFile()

        courses = []

        for courseId_s in self.subtitlesData:
            for course in self.metadataData:
                if str(course["id"]) == courseId_s:
                    courses.append({"metadata":course, "subtitles":self.subtitlesData[courseId_s]})

        finalJSON = {"courses":courses}

        with open('Coursera_dataset.json', 'w') as outfile:
            json.dump(finalJSON, outfile)

        with open('Udacity_dataset_sample.json', 'w') as outfile:
            json.dump({"courses":courses[:2]}, outfile)


    def remove_empty_courses(self):
        """ Generate a new version of the json object with only the courses with some subtitles.
        """
        pass
        
def zip_several_subtitlesFiles(subtitlesFileList):
    """
    """
    current_data = {}
    for subtitlesFile in subtitlesFileList:
        with open(subtitlesFile) as fstream:
            subtitlesData = json.load(fstream)
            for key in subtitlesData:
                if len(subtitlesData[key]) != 0:
                    current_data[key] = subtitlesData[key]
                if len(current_data) == 2:
                    with open("sample_data_subtitles.json", 'w') as fstream:
                        json.dump(current_data, fstream)

    with open("Coursera_subtitles_data.json", 'w') as fstream:
        print "Total number of courses:", len(current_data)
        json.dump(current_data, fstream)

if __name__ == "__main__":

    #zip_several_subtitlesFiles(["Coursera_dataset_0_64.json","Coursera_dataset_64_1000.json"])
    
    CDM = CourseraDatasetMerger("Coursera_subtitles_data.json","metadata.json")
    CDM.zip_subtitles_metadata()
