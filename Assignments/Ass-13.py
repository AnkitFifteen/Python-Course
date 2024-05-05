#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 09:55:36 2024

@author: ankit

Copy content from one file and paste in another file using file functions?
"""
fileAPath = "Assignments/fileA.txt"
fileBPath = "Assignments/fileB.txt"

#create fileA
fileA = open(fileAPath, "w")

#create fileB
fileB = open(fileBPath, "w")

#write "This is a sample text." in fileA
fileA.write("This is a sample text.")

#get contents of fileA
fileA = open(fileAPath, "r")
fileAContents = fileA.read()

#write fileAContents to fileB
fileB.write(fileAContents)

fileA.close()
fileB.close()