import sqlite3
import os

conn = sqlite3.connect('Student.db')
curser = conn.cursor()

def menu():
    print(' [1] Öğrencileri Listele')
    print(' [2] Öğrenci Ekle') # income or expense
    print(' [3] Öğrenci Sil')
    print(' [0] Exit the program')
    global option
    option = int(input("Enter your option: "))

menu()

def list_student():
    os.system('cls')
    curser.execute("SELECT * FROM student")
    students = curser.fetchall()
    print("ID\t\tName\t\tSurname\t\tAge\t\tGender")
    print("------------------------------------------------------------------------------------------------------------------")
    for student in students:
        print(student[0],"\t\t",student[1],"\t\t",student[2],"\t\t",student[3],"\t\t",student[4])
    print("------------------------------------------------------------------------------------------------------------------")
    menu()