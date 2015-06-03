#!/bin/bash

mkdir lib
echo Fetching the stanford NLP toolkit
wget http://mallet.cs.umass.edu/dist/mallet-2.0.6.tar.gz
tar xvzf mallet-2.0.6.tar.gz
mv mallet-2.0.6 lib/
rm mallet-2.0.6.tar.gz
