import os

demoFilePath = "Codes/FileOperations/demo.txt"
sample_textFilePath = "Codes/FileOperations/sample_text.txt"

def demo_operator():
    f = open(demoFilePath, "r")
    print(f.read())
    print(f.readline())
    for i in f:
        print(i)
    f.close()

    f = open(demoFilePath, "w")
    f.write("this is the new content of file. Previous content is now deleted.")
    f.close()

    f = open(demoFilePath, "a")
    f.write("this is the new content of file. Previous content is not deleted.")
    f.close()
    os.remove(demoFilePath)

def sample_text_operator():
    occurrence = 0
    word_to_search = str(input("Enter the word to search for: "))
    sample_text = open(sample_textFilePath, "r")
    fileContents = sample_text.read()
    words_list = fileContents.split(" ")
    occurrence = words_list.count(word_to_search)
    print("Occurrence of", word_to_search, "in file =", occurrence)
    sample_text.close()

def count_each_character_occurrence():
    a = "Hello. This is my new pen"
    char_list = dict()
    for char in a:
        if char not in char_list:
            char_list[char] = 1
        else:
            char_list[char] += 1
    for char, count in char_list.items():
        print("Occurrence of", char, "in the given string =", count)

whatToRun = str(input("List of functions:\n #1 demo_operator()\n #2 sample_text_operator()\n #3 count_each_character_occurrence()\nEnter function number = "))

match whatToRun:
    case "1":
        demo_operator()
    case "2":
        sample_text_operator()
    case "3":
        count_each_character_occurrence()
    case _: print("Wrong option entered.")
