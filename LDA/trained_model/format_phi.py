#!/usr/bin/python

import json

if __name__ == "__main__":

    LUT = {"0":"social science","1":"Art and Humanities","2":"Science","3":"Engineering","4":"Business Economics","5":"IT","-1":"Other"}

    with open("phi.json") as fstream:
        phi_initial = json.load(fstream)

    phi_final = []

    for topic in phi_initial["topics"]["topic"]:

        name = topic["@name"]
        ID = topic["@id"]
        category = LUT[topic["@category"]]

        topbigrams = []
        topwords = []

        for phrase in topic["phrase"][:7]:

            text = phrase["#text"]
            prob = phrase["@weight"]

            ww = text.split()
            if ww[0] == ww[1]:
                text = ww[0]

            topbigrams.append({"bigram":text, "prob":float(prob)})

        for word in topic["word"][:7]:

            text = word["#text"]
            prob = word["@weight"]

            topwords.append({"word":text,"prob":float(prob)})

        phi_final.append({"_id":ID,"topwords":topwords,"topbigrams":topbigrams\
            ,"name":name,"category":category})

        with open("topics_data.json",'w') as fstream:
            json.dump(phi_final,fstream)