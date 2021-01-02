import csv
import sys
from csv import DictReader
from typing import List, Dict
import matplotlib.pyplot as plt
import urllib.request
import wget
import os

#Removes data.csv and redownloads it everytime the scripts one. Necessary to update it.
#file_download = "https://teamfinder.xyz/data.csv"
#if os.path.exists("data.csv"):
    #os.remove("data.csv")
#wget.download(file_download, "")

FILE = "test.csv"
READ_MODE = "r"

file_handle = open(FILE, READ_MODE, encoding="utf8")
csv_reader = DictReader(file_handle)


"""For now I just found the students that wasn't the desired student, 
then made a list out of all the other students. The questions I just manually inputted, still not sure for 
the file handling how to input the file as an argument if we don't do it within the function.
https://smallbusiness.chron.com/run-python-webpage-33100.html might be useful to see how to integrate it."""

def main() -> List[str]:
    questions = []
    for row in csv_reader:
        questions.append(row)
    print(questions[0])
    return questions[0]

def find_questions() -> List[str]:
    questions = []
    questions = next(csv_reader)
    del(questions[0])
    return questions






if __name__ == "__main__":
    main()