#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:28:43 2024

@author: ankit

Write a program that creates a list of 10 random integers. Then create two lists by
name odd_list and even_list that have all odd and even values of the list respectively.

"""
import random

list_of_random_numbers = list()
odd_list = list()
even_list = list()

for iter in range(0, 10):
    list_of_random_numbers.append(random.randint(0, 9999))

for value in list_of_random_numbers:
    if value % 2 == 0:
        even_list.append(value)
    else:
        odd_list.append(value)

print("Even list: ", even_list)
print("Odd list: ", odd_list)

