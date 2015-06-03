#!/usr/bin/python

import json

def filter_theta(theta, phi):
    blackList = []
    for topic in phi:
        if topic["name"] == "":
            blackList.append(topic["_id"])
    for key in theta:
        newList = []
        for e in theta[key]:
            if e[0] in blackList:
                newList.append((e[0],e[1]))
        theta[key] = newList

if __name__ == "__main__":

    courseraDataPath = "./Coursera_dataset.json"
    udacityDataPath  = "./Udacity_dataset.json"

    destFolder = "./mallet_dataset/"

    with open(courseraDataPath) as fstream:
        courseraData = json.load(fstream)

    with open(udacityDataPath) as fstream:
        udacityData = json.load(fstream)

    with open("../LDA/trained_model/theta.json") as fstream:
        theta = json.load(fstream)

    with open("../LDA/trained_model/phi.json") as fstream:
        phi = json.load(fstream)

    filter_theta(theta, phi)

    metadata_zipped = {"courses":[]}

    # Handling coursera data
    for course in courseraData["courses"]:
        source = "coursera"
        coursename = course["metadata"]["name"] 
        ID = course["metadata"]["id"] 
        description = course["metadata"]["short_description"]
        if course["metadata"]["instructor"] == None:
            instructors = []
        else:
            instructors = course["metadata"]["instructor"].replace('and',',').split(',')
        image = course["metadata"]['large_icon']
        universities = []
        for univ in course["metadata"]['universities']:
            name = univ["name"]
            ID = univ['id']
            im = univ['square_logo']
            universities.append({"name":name, "id":ID, "image":im})
        video = course["metadata"]["video"]
        theta_key = source+'_'+str(course["metadata"]["id"])+'.txt'
        topics = [ {"topicRef":tref,"prob":prob} for tref,prob in theta[theta_key][:10]]
        metadata_zipped["courses"].append({"name":coursename, "source":source, \
            "description":description, "instructors":instructors, "image":image,\
            "affiliates":universities,"video":video, "topics":topics})

    # Handling udacity data
    for course in udacityData["courses"]:
        source = "udacity"
        coursename = course["metadata"]["title"]
        ID = course["metadata"]["key"] 
        description = course["metadata"]["short_summary"]
        instructors = []
        for instructor in course["metadata"]["instructors"]:
            instructors.append(instructor["name"])
        image = course["metadata"]['image']
        universities = []
        for univ in course["metadata"]['affiliates']:
            name = univ["name"]
            universities.append({"name":name, "id":"", "image":univ["image"]})
        video = course["metadata"]["homepage"]
        theta_key = source+'_'+course["metadata"]["key"]+'.txt'
        topics = [ {"topicRef":tref,"prob":prob} for tref,prob in theta[theta_key][:10]]
        metadata_zipped["courses"].append({"name":coursename, "source":source, \
            "description":description, "instructor":instructors, "image":image,\
            "affiliates":universities,"video":video, "topics":topics})

    with open('metadata.json', 'w') as outfile:
        json.dump(metadata_zipped, outfile)

    with open('metadata_sample.json', 'w') as outfile:
        json.dump({"courses":metadata_zipped["courses"][:5]+metadata_zipped["courses"][-5:]}, outfile)
