"""This is for Photos
"""
from Services.file_io import file_reader

# class Photos:
#     def __init__(self,id,name,location,size):
#         self.id = id 
#         self.name = name
#         self.location = location
#         self.size = size
#     def __str__(self):
#         return f"{self.id},{self.name},{self.location}, {self.size}\n"

def get_last_photo_id():
    photos = file_reader("data/photos.csv")
    if photos[-1].split(",")[0] == "id":
        return 0
    return int(photos[-1].split(",")[0])