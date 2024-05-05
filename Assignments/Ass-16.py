#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 10:09:37 2024

@author: ankit

Consider the file test.txt and perform following operations
1. open the file if exists, if not create  a new file
2. add string 'abcde' to the end of the file
3. read and display first 5 characters
4. display total number of characters present in the file
"""
import os

testFilePath = "Assignments/testFile.txt"

#check if file exists
if os.path.exists(testFilePath):
    #if exists open
    testFile = open(testFilePath, "a")
else:
    #if not exists create
    testFile = open(testFilePath, "a")

#add string 'abcde' to end of file (append) in testFile
testFile.write("abcde")                  

#read testFile and store it in list
testFile = open(testFilePath, "r")
testFileContents = testFile.read()
testFileContentsList = list(testFileContents)

#display the first 5 characters from above list
char_count = 0
while char_count != 5:
    print(testFileContentsList[char_count])
    char_count += 1

#count number of characters present in the file and display count
print(f"Number of characters: {len(testFileContentsList)}")

testFile.close()
