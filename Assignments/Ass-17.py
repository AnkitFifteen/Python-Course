#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:35:12 2024

@author: ankit

Create a class called library with data attributes like acc_number, publisher, title
and author. The methods of the class should include

a. read() – acc_number, title, author.
b. compute() - to accept the number of days late, calculate and display the fine
   charged at the rate of $1.50 per day.
c. display the data.
"""

class library:
    acc_number = 000
    publisher = "unknown"
    title = "unknown"
    author = "unknown"

    def read(self, AccountNumber, Publisher, Title, Author):
        self.acc_number = AccountNumber
        self.publisher = Publisher
        self.title = Title
        self.author = Author

    def compute(self):
        noOfDaysLate = int(input("Enter no. of days late: "))
        rate = 1.50
        print(f"Fine to be charged = ${rate * noOfDaysLate}")
        
    def display(self):
        print(f"Account Number: {self.acc_number} Publisher: {self.publisher} Title: {self.title} Author: {self.author}")
        
Lib1 = library()
Lib1.read(258, "McGraw Hill", "Core Java", "James")
Lib1.compute()
Lib1.display()
