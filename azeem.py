from collections import UserList
from multiprocessing.connection import wait
import random
import sys
from select import select
from unicodedata import name

students_List_One = [
    {"name": "Tobias Fors", "email": "tobias.fors@yh.nackademin.se", "age": 30,  "student_id": 11230, "grades":
     {"Pythonprogrammering 1": 1, "Databasteknik": 4}},
    {"name": "Karin Börjell", "email": "karin.borjell@yh.nackademin.se", "age": 32,  "student_id": 11231, "grades":
     {"Pythonprogrammering 1": 1, "Pythonprogrammering 2": 3}},
    {"name": "Daniel Eliasson", "age": 29,  "email": "daniel.eliasson@yh.nackademin.se", "student_id": 11233, "grades":
     {"Pythonprogrammering 1": 1, "Affärsmannaskap": 2}},
    {"name": "Magdalena Andersson", "age": 50,  "email": "magdalena.andersson@yh.nackademin.se", "student_id": 11234, "grades":
     {"Pythonprogrammering 1": 1, "Webbramverk inom python": 5}},
]  # this is the list of all available students

print('Welcome to the greatest student system in the world.' '\n')
print('What would you like to do?')


def user_chose():  # putting all the user inputs in a function
    print('[q] - Exit')
    print('[l] - List all students from the registry')
    print('[a] - Add a student from the registry')
    print('[r] - Remove a student from the registry')


def student_grade():
    print('[b] - Go Back')
    print('[g] - Show summary of grades')
    print('[p] - Personal information')


while True:  # main while loop. use loop for capturing the user input
    user_chose()
    user_value = input()
    if user_value == 'q':
        sys.exit()  # exiting from the the program

    elif user_value == 'l':
        for student in students_List_One:  # print only the names of the students
            print(
                f"NAME: {student['name']}, EMAIL: {student['email']}, AGE: {student['age']}", sep='\n')
        print('')  # line space for next user command of action

        while True:
            student_grade()  # get user input to show grades of students from the list
            user_input = input()
            if user_input == 'g':
                for student in students_List_One:
                    print(
                        f"{student['name']} - {student['grades']}", sep='\n',)

            elif user_input == 'p':
                for student in students_List_One:
                    print(
                        f"{student['name']} - {student['student_id']} - {student['email']}", sep='\n',)

            elif user_input == 'b':

                break

    elif user_value == 'a':
        stu = dict()

        print('Provide the name of a student to add from the registry:  name')

        studentname = input()
        stu["name"] = studentname

        print('enter student id')
        studentid = int(input())
        stu["student_id"] = studentid

        print('Provide the email of a student')

        studentemail = input()
        stu["email"] = studentemail
        print('Provide the age of a student')

        studentage = input()

        stu["age"] = studentage
        print('In how much courses student will be enrolled')

        i = ""
        course = dict()
        while(type(i) is not int):
            i = int(input())
        for i in range(0, i):

            print("enter course name")
            coursename = input()

            print("enter course grad")
            coursegrad = int(input())

            course[coursename] = coursegrad

        stu["grades"] = course
        students_List_One.append(stu)
        for i in students_List_One:
            print(i)
            break
    elif user_value == 'r':
        print('Remove a student by ID from the registry' '\n')

        remove_student = input()
        listt = [i for i, _ in enumerate(students_List_One) if _[
            'student_id'] == int(remove_student)]
        try:

            students_List_One.pop(listt[0])

            print(remove_student + ' is removed.')
        except IndexError:
            print("something went wrong")
