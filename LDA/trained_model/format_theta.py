#!/usr/bin/python

import json

if __name__ == "__main__":

    thetaPath = "./theta.txt"

    finalTheta = {}

    with open(thetaPath) as theta:
        
        for numLine,line in enumerate(theta):

            if numLine == 0:
                continue

            data = line.strip().split()
            name = data[1].split('/')[-1]
            data = data[2:]

            currentTheta = []

            for i in xrange(len(data)):

                idx = 2*i
                topicIdx = data[idx]
                topicProba = data[idx+1]

                currentTheta.append([topicIdx,topicProba])

            finalTheta[name] = currentTheta

    with open('theta.json', 'w') as outfile:
        json.dump(finalTheta, outfile)

