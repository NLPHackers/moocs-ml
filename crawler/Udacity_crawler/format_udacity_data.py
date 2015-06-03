import sys
import json

with open('Udacity_dataset_0_6.json') as chunk1:
    with open('Udacity_dataset_7_16.json') as chunk2:
        with open('Udacity_dataset_17_end.json') as chunk3:
            data1 = json.load(chunk1)
            data2 = json.load(chunk2)
            data3 = json.load(chunk3)

            courses = data1["courses"] + data2["courses"] + data3["courses"]

            finalJSON = {"courses":courses}

            with open('Udacity_dataset.json', 'w') as outfile:
                json.dump(finalJSON, outfile)

if __name__ == "__main__":

    with open('Udacity_dataset.json') as chunk:
        data = json.load(chunk)

        acc = 0
        for course in data["courses"]:
            acc += len(course["subtitles"])
            print course["metadata"]["title"],"     ",len(course["subtitles"])

        print "Total num of vids:", acc