import sqlite3
import os
import time

conn = sqlite3.connect('Student.db')
curser = conn.cursor()


def menu():
    os.system('cls')
    print(' [1] Öğrencileri Listele')
    print(' [2] Öğrenci Ekle')
    print(' [3] Öğrenci Sil')
    print(' [0] Exit the program')
    global option
    valid_input = False
    while not valid_input:
        try:
            option = int(input("Enter your option: "))
            valid_input = True
        except ValueError:
            print("Invalid option. Please enter a number.")

menu()

# Function to check if the ID exists in the database
def id_exists_in_database(input_id):
    curser.execute("SELECT COUNT(*) FROM Students WHERE st_id = ?", (input_id,))
    result = curser.fetchone()
    return result[0] > 0


def list_student():
    os.system('cls')
    curser.execute("SELECT * FROM Students")
    students = curser.fetchall()
    print("ID","Name","Surname","Age","Gender", sep="\t\t")
    print("------------------------------------------------------------------------------------------------------------------")
    for student in students:
        print(student[0],student[1],student[2],student[3],student[4], sep="\t\t")
    print("------------------------------------------------------------------------------------------------------------------")
    input("Press enter to continue...")
    if option != 0:
        os.system('cls')
        menu()

def add_student():
    os.system('cls')
    # try and except block to catch errors for name, surname , gender and age
    valid_input = False
    while not valid_input:
        input_name = input("Enter name: ")
        if input_name.isdigit():
            print("Invalid name. Please enter a string.")
        else:
            valid_input = True

    valid_input = False
    while not valid_input:
        input_surname = input("Enter surname: ")
        if input_surname.isdigit():
            print("Invalid surname. Please enter a string.")
        else:
            valid_input = True

    valid_input = False
    while not valid_input:
        try:
            input_age = int(input("Enter age: "))
            valid_input = True
        except ValueError:
            print("Invalid age. Please enter a number.")
    valid_input = False
    while not valid_input:
        input_gender = input("Enter gender: ").upper()
        if input_gender not in ["KADIN", "ERKEK"]:
            print("Invalid gender. Please enter either 'Kadin' or 'Erkek'.")
        else:
            valid_input = True
    
    curser.execute("INSERT INTO Students (name, surname, age, gender) VALUES (?, ?, ?, ?)", (input_name, input_surname, input_age, input_gender))
    conn.commit()

    print("Student added successfully.")
    time.sleep(1) 
    os.system('cls')
    menu()

def delete_student():
    os.system('cls')
    curser.execute("SELECT * FROM Students")
    students = curser.fetchall()
    print("ID","Name","Surname","Age","Gender", sep="\t\t")
    print("------------------------------------------------------------------------------------------------------------------")
    for student in students:
        print(student[0],student[1],student[2],student[3],student[4], sep="\t\t")
    print("------------------------------------------------------------------------------------------------------------------")
    choice = (input("Press enter to continue or write '0' back to menu..."))
    if choice == "0":
        os.system('cls')
        menu()
    else:
        valid_input = False
        while not valid_input:
            try: 
                input_id = int(input("Enter id: "))
                # Check if the ID exists in the database
                if not id_exists_in_database(input_id):  # Replace with your database check logic
                    print("Invalid id. This ID does not exist. Please enter a valid ID.")
                else:
                    valid_input = True
                    confirm = input("Öğrenciyi silmek istediğinize emin misiniz? (E/H): ")
                    if confirm.upper() == "E":
                        curser.execute("DELETE FROM Students WHERE st_id = ?", (input_id,))
                        conn.commit()
                        print("Student deleted successfully.")
                        time.sleep(1)
                        os.system('cls')
                        menu()
                    else:
                        print("Student not deleted.")
                        time.sleep(1)
            except ValueError:
                print("Invalid id. Please enter a number.")


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

conn.close()