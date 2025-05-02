#!/bin/bash

wget https://data.researchdatafinder.qut.edu.au/dataset/c5a0ccba-fa28-4cb7-a9f8-4a7f93670344/resource/2b581c49-17f0-4941-8f8f-ffd4871c1117/download/egadtrainset.zip
unzip egadtrainset.zip
mv egad_train_set/* ./
rmdir egad_train_set
