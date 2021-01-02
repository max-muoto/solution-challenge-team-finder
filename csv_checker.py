import csv
import sys
from csv import DictReader
from typing import List, Dict
import matplotlib.pyplot as plt
import urllib.request
import wget
import os
import smtplib
import random

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

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


def listToString(s):  
    
    # initialize an empty string 
    str1 = " "  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  


def main() -> None:
    students: List[str] = find_students("Bob")
    emails: List[str] = ["pnyely25.rjh@cardour.com", "jack@gmail.com", "maxmuoto@gmail.com",
    "bill@gmail.com", "gary@gmail.com", "adfsdfdsafd@test.com", "jill@gmail.com", "testafkdsjfa@test.com",
    "jill@gmail.com", "testafkdsjfa@test.com", "jill@gmail.com", "testafkdsjfa@test.com", "jill@gmail.com",
    "testafkdsjfa@test.com", "jill@gmail.com", "testafkdsjfa@test.com"]
    student_emails: Dict[str, str] = {}
    i = 0
    while i < len(students):
        student_emails[students[i]] = emails[i]
        i += 1
    
    #questions: List[str] = ["email", "school", "year", "experience", "career", "major","languages"]
    # ["What school do you go to?", "What is your name?", "What is your major?", 
    # "What types of Google Technologies are you interested in?", "What is your programming experience level?",
    # "What languages are you comfortable with?", "How many DSC workshops have you attended?", 
    # "What career are you interested in pursuing?"]

    #scores: List[float] = run_questions("Bob", students, questions)
    #student_scores = student_scores_dict(students, scores)
    #best_names: List[str] = best_matches(student_scores)

    best_names: List[str] = []

    i: int = 0
    while i < 4:
        best_names.append(random.choice(students))
        i += 1
        
    new_emails: List[str] = []
    for name in best_names:
        new_emails.append(student_emails[name])

    with smtplib.SMTP('smtp.gmail.com', 587) as smpt:
        smpt.ehlo()
        smpt.starttls()
        smpt.ehlo()

        smpt.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        #Subject line for the email
        subject = "Here are your Solution Challenge team suggestions!"
        #Body message for the email
        body = (best_names) + (new_emails)

        msg = f"Subject: {subject}\n\n{body}"
        
        #Email addres from which it is sent from, and sent to
        smpt.sendmail(EMAIL_ADDRESS, "maxmuoto@gmail.com", msg)
        return None

def find_students(test_name: str) -> List[str]:
    students: List[str] = []
    for row in csv_reader:
        if row["name"] != test_name:
            try:
                students.append(row["name"])
            except ValueError:
                ...
    return students

"""def all_student_match(name: str) -> List[Dict[str, float]]:
    table: List[Dict[str, str]] = []
    for row in csv_reader:
        if row["name"] == name:
            table.append(str(row["name"]))"""

            
def answer(base_name: str, test_name: str, question: str) -> float:
    """Sees if a student matches answers with another student."""
    counter: float = 0
    check: bool = False
    base_value: str = ""
    for row in csv_reader:
        if row["name"] == base_name:
            base_value += row[question]
            print(base_value)
            check = True
        if check:
            if row["name"] == test_name:
                print(row["name"])
                if row[question] == base_value:
                    counter += 1
    counter += 1
    return counter


def run_questions(name: str, students: List[str], questions: List[str]) -> List[float]:
    """Creates score (just summing how many matches) for each student."""
    scores = []
    for student in students:
        sum = 0
        for question in questions:
            sum += answer(name, student, question)
        scores.append(sum)
    return scores


def student_scores_dict(students: List[str], scores: List[float]) -> Dict[str, float]:
    """Assigns score to each student."""
    student_scores: Dict[str, float] = {}
    i = 0
    while i < len(students):
        student_scores[students[i]] = scores[i]
        i += 1
    return student_scores


def best_matches(data: Dict) -> List[str]:
    """Should produce the four highest scoring students."""
    names: List[str] = []
    i: int = 0
    while i < 4:
        max_value = max(data.values())
        name = list(data.keys())[list(data.values()).index(max_value)]
        data.pop(name)
        names.append(name)
    return names


"""def compare(file_name: str, base_name: str, questions: List[str]) -> List[Dict[str,float]]:
    students: List[Dict[str, float]] = []
    student_data: Dict[str, float] = {}
    for row in csv_reader:
        for name in row["name"]:
            if name != base_name:
                for question in questions:
                    student_data[name] = answer(file_name, base_name, name, question)
                    students.append(student_data)
    return students"""





if __name__ == "__main__":
    main()