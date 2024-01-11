"""photo data"""

from tabulate import tabulate
from Models.photos import get_last_photo_id
from .file_io import file_appender,file_reader,file_list_writer

def add_new_photos():

    photo_id = get_last_photo_id + 1  
    name = input("ENter photo's name")
    size = float(input("Enter size: "))
    location = input("Enter location")
    

    new_photo = f"{photo_id},{name}, {size}, {location}, \n"

    file_appender("data/photographers.csv", new_photo)

def get_all_photos():
    photos = file_reader("data/photographers.csv")
    data = []
    for photo in photos:
        data.append([photo.split(",")[0],photo.split(",")[1],photo.split(",")[2],])
    print(tabulate(data))

def delete_photo():
    photo_id = input("Enter id:  \n")
    photos = file_reader("data/photos.csv")
    for photographer in photos:
        if str(photos.split(",")[0]) == str(photo_id):
            photos.remove(photographer)
    file_list_writer("data/photos.csv",photos)
    print("photo deleted successfully")
    