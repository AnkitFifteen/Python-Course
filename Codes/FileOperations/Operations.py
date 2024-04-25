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
    fileContents = open(sample_textFilePath, "r").read()
    words_list = fileContents.split(" ")
    occurrence = words_list.count(word_to_search)
    print("Occurrence of", word_to_search, "in file =", occurrence)

sample_text_operator()