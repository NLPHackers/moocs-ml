#!/usr/bin/python

import subprocess
import sys 

if __name__ == "__main__":

	if len(sys.argv) != 4:
		print "usage:\npython mallet_processor <numTopics> <numIterations> <dataPath>\n"
		print "using default parameters: \n\tnumTopics 120 \n\tnumIterations 1000 \n\tdataPath ./mallet_formated_dataset/"
		numTopics = "120"
		numIterations = "1000"
		dataPath = "../../data/mallet_dataset/"
	else:
		numTopics = sys.argv[1]
		numIterations = sys.argv[2]
		dataPath = sys.argv[3]

	MALLET_PATH = '../lib/mallet-2.0.6/bin/mallet'

	subprocess.call([MALLET_PATH, 
		'import-dir', 
		'--input', 
		dataPath,
	    '--output',
	    './topic-input.mallet', 
	    '--keep-sequence',
	    '--remove-stopwords'])

	subprocess.call([MALLET_PATH, 
		'train-topics', 
		'--input', 
		'../trained_model/topic-input.mallet', 
		'--num-topics', 
		numTopics, 
		'--output-doc-topics',
		'../trained_model/theta.txt', 
		'--xml-topic-phrase-report', 
		'../trained_model/phi.xml', 
		'--num-threads', 
		'3', 
		'--num-iterations', 
		numIterations, 
		'--show-topics-interval', 
		'100', 
		'--output-model-interval', 
	    '100', 
	    '--optimize-interval', 
	    '10', 
	    '--inferencer-filename', 
	    'inferencer' ])

