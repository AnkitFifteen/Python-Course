#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:15:25 2024

@author: ankit

Write a program that accepts a string from the user and display the same string after removing vowels from it.

"""

input_string = str(input("Enter a string: "))

vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

for vowel in vowels:
    if vowel in input_string:
        input_string = input_string.replace(vowel, "")
        
print("Your string without vowels: ", input_string)
