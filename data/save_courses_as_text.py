#!/usr/bin/python

import json

def clean_coursera_subtitles(data):
    return data.replace('\r\n',' ')\
        .replace('\n',' ')\
        .replace('\'ll ',' ')\
        .replace(' eh ',' ')\
        .replace(' yeah ',' ')\
        .replace(' ago ',' ')\
        .replace(' uh ',' ')\
        .replace('\'ve ',' ')\
        .encode('utf8')

def clean_udacity_subtitles(data):
    return data.replace('\r\n',' ')\
        .replace('\n',' ')\
        .replace('&#39;','\'')\
        .replace('&gt;',' ')\
        .replace('[SOUND]',' ')\
        .replace('[UNKNOWN]',' ')\
        .replace('[INAUDIBLE]',' ')\
        .replace('\'ll ',' ')\
        .replace(' eh ',' ')\
        .replace(' yeah ',' ')\
        .replace(' ago ',' ')\
        .replace(' uh ',' ')\
        .replace('\'ve ',' ')\
        .encode('utf8')

if __name__ == "__main__":

    courseraDataPath = "./Coursera_dataset.json"
    udacityDataPath  = "./Udacity_dataset.json"

    destFolder = "./mallet_dataset/"

    with open(courseraDataPath) as fstream:
        courseraData = json.load(fstream)

    with open(udacityDataPath) as fstream:
        udacityData = json.load(fstream)

    for course in courseraData["courses"]:
        source = "coursera"
        coursename = course["metadata"]["name"] 
        ID = course["metadata"]["id"] 

        destFile = source+"_"+str(ID)+'.txt'

        data = ' '.join(course["subtitles"])

        with open(destFolder+destFile, 'w') as outFile:
            outFile.write(clean_coursera_subtitles(data))

    for course in udacityData["courses"]:
        source = "udacity"
        coursename = course["metadata"]["title"]
        ID = course["metadata"]["key"] 

        destFile = source+"_"+str(ID)+'.txt'

        data = ' '.join(course["subtitles"])

        with open(destFolder+destFile, 'w') as outFile:
            outFile.write(clean_udacity_subtitles(data))