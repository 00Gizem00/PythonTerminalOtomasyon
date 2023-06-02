import sqlite3
import os
import time

conn = sqlite3.connect('Student.db')
curser = conn.cursor()

def menu():
    print(' [1] Öğrencileri Listele')
    print(' [2] Öğrenci Ekle')
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

def add_student():
    os.system('cls')
    input_name = input("Enter name: ")
    input_surname = input("Enter surname: ")
    input_age = input("Enter age: ")
    input_gender = input("Enter gender: ")
    
    curser.execute("INSERT INTO student (name, surname, age, gender) VALUES (?, ?, ?, ?)", (input_name, input_surname, input_age, input_gender))
    conn.commit()
    conn.close()

    print("Student added successfully.")
    menu()

def delete_student():
    os.system('cls')
    input_id = input("Enter id: ")
    curser.execute("DELETE FROM student WHERE st_id = ?", (input_id,))
    conn.commit()
    conn.close()

    print("Student deleted successfully.")
    menu()


while option != 0:
    if option == 1:
        list_student()
    elif option == 2:
        add_student()
    elif option == 3:
        delete_student()
    else:
        print("Invalid option.")
        time.sleep(1)
        os.system('cls')
        menu()


print("Exiting the program...")
time.sleep(1)
os.system('cls')
print("Program exited.")