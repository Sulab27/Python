"""This is Menu
"""

from Services.register import register
from Services.Login import login
from Services.utils import add_new_photographers, get_all_photographers, delete_photographer
from Services.photo_utils import get_all_photos,delete_photo,add_new_photos


def login_menu():
    print("Welcome to Login menu")
    print("1: Login")
    print("2: Register")
    print("3: Exit")
     
    choice = int(input("Enter choice:"))
    if choice == 1:
        username = input("Enter name:\n")
        password = input("Enter password:\n")
        # print(f"You enter name  :{username}\n",f"You enter password  :{password}\n")
        if login(username, password) == True:
            main_menu()
        else:
            login_menu()
       
    if choice == 2:
        
        username = input("Enter name:\n")
        password = input("Enter password:\n")
        email = input("Enter your mail:\n")
        print(f"YOU enter name :{username}\n", f"You enter password :{password}\n",f"you entered your mail :{email}\n")
        
        if register(username, password, email):
            main_menu()
            print("Registration successful!")
        else:
            login_menu()
            print("Registration failed. Please try again.")
        
def main_menu():
    print("\n----------------------------")
    print("WELCOME TO MAIN MENU")
    print("1. Photographers")
    print("2. Photos")
    
    print("3. Log out")

    choice = int(input("Enter 1-3 according to the menu :"))
    if choice == 1:
        photographer_menu()
    elif choice == 2:
        photo_menuu()
    elif choice == 3:
        login_menu()
    else:
        print("Invalid choice")


def photographer_menu():
    print("\n------------LOGIN---------\n")
    print("Welcome to the Photographer menu")
    print("1: View Photographers")
    print("2: Add Photographer")
    print("3: Delete Photographer")
    print("4: Update Photographer")
    print("5: Changepw")
    print("\n----------------\n")

    choice = int(input("Enter your choice"))
    
    if choice == 1:
        print("all photographers")
        get_all_photographers()
        main_menu() 
    elif choice == 2:
        add_new_photographers()
        main_menu()
    elif choice == 3:
        delete_photographer()
        main_menu()
    elif choice == 4:
        print("you can update the photographers")
    elif choice == 5:
        print("You can change password here")
    else:
        print("Invalid Input")   

def photo_menuu():
    print("\n------------LOGIN---------\n")
    print("Welcome to the Photo menu")
    print("1: View Photos")
    print("2: Add Photo")
    print("3: Delete Photo")
    print("4: Update Photo")
    print("\n----------------\n")
    choice =  int(input("Enter choice"))

    if choice == 1:
        get_all_photos()
        main_menu()
        print()
    elif choice == 2:
        add_new_photos()
        main_menu()
        print()
    elif choice == 3:
        delete_photo()
        main_menu()
    elif choice == 4:
        main_menu()
    else:
        print("Invalid choice")
        