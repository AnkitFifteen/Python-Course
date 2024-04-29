#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:42:43 2024

@author: ankit

Write a program that has the dictionary of your friends’ names as keys and phone
numbers as its values. Print the dictionary in a sorted order. Prompt the user to
enter the name and check if it is present in the dictionary. If the name is not present,
then enter the details in the dictionary.

"""
def addEntry(PhoneBook):
    nameToAdd = str(input("Enter name to add: "))
    phoneNumberToAdd = int(input("Enter phone number(without + prefix): "))
    PhoneBook[nameToAdd] = phoneNumberToAdd
    print("Details added successfully.")
    sortPhoneBook(PhoneBook)
    
def findEntry(PhoneBook):
    nameToCheck = str(input("Enter name to search for: "))
    if nameToCheck in PhoneBook:
        print("Details:\n Name:", nameToCheck, "\n Phone Number:", PhoneBook.get(nameToCheck), end = "\n")
    else:
        yesNo = input("Details not found. Do you want to create a new entry?(Y/N): ")
        match yesNo:
            case 'Y'| 'y':
                addEntry(PhoneBook)
            case 'N' | _:
                print("Exiting...")
                return
        
def sortPhoneBook(PhoneBook):
    names = PhoneBook.keys()
    PhoneBook = sorted(dict.fromkeys(names))
    
def printSortedPhoneBook(PhoneBook):
    serialNumber = 1
    if PhoneBook == {}:
        print("No entry yet.")
        return
    else:
        for name, phoneNumber in PhoneBook.items():
            print("Entry No.", serialNumber, "\n Name:", name, "\n Phone Number:", phoneNumber, end = "\n")
            serialNumber += 1
    
def runPhoneBook():
    PhoneBook = dict()
    optionChosen =  str(input("PhoneBook Operations:\n #1 Find a phone number.\n #2 Add a phone number.\n #3 Print PhoneBook.\nEnter operation number: "))
    match optionChosen:
        case "1":
            findEntry(PhoneBook)
        case "2":
            addEntry(PhoneBook)
        case "3":
            printSortedPhoneBook(PhoneBook)
        case _:
            print("Wrong input.")
            
runPhoneBook()