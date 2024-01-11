"""Photographer data
"""

from tabulate import tabulate
from Models.photographers import get_last_photographer_id
from .file_io import file_appender,file_reader,file_list_writer
"""for adding new photographers"""
def add_new_photographers():
    photographer_id = get_last_photographer_id() + 1 
    name = input("ENter photographer's name")
    age = int(input("Enter age: "))
    experience = input("Enter experience")
    gmail = input("ENter gmail accont")

    new_photographer = f"{photographer_id},{name}, {age}, {experience}, {gmail}\n"

    file_appender("data/photographers.csv", new_photographer)


def get_all_photographers():
    photographers = file_reader("data/photographers.csv")
    data = []
    for photographer in photographers:
        data.append([photographer.split(",")[0],photographer.split(",")[1],photographer.split(",")[2],photographer.split(",")[3]])
    print(tabulate(data))

def delete_photographer():
    photographer_id = input("Enter id:  \n")
    photographers = file_reader("data/photographers.csv")
    for photographer in photographers:
        if str(photographer.split(",")[0]) == str(photographer_id):
            photographers.remove(photographer)
    file_list_writer("data/photographers.csv",photographers)
    print("photographer deleted successfully")
    
