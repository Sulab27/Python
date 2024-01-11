"""for Photographer
"""
from Services.file_io import file_reader

# class Photographers:
#     def __init__(self,id,name="",age = 0,experience = "",gmail = ""):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.experience = experience
#         self.gmail = gmail
        
#     def __str__(self):
#         return f"id: {self.id},{self.name},{self.age},{self.experience},{self.gmail}"

def get_last_photographer_id():
    photographers = file_reader("data/photographers.csv")
    if photographers[-1].split(",")[0] == "id":
        return 0
    return int(photographers[-1].split(",")[0])
    
    # def photo_desc():
    #     print(f"Photos of photographer{self.name} are:")
    #     for i,ele in enumerate(self.photos):
    #         print("id: ",ele.id)
    #         print("Name: ",ele.photo_name)
    #         print("Photo Size: ", ele.size)
    #         print("location", ele.location)
    #         print()     
    
    # def photographer_details(self):
    #     print()
    #     print("ID: ",self.id)
    #     print(f"PHOTOGRAPHER {self.name} INFORMATION")
    #     print("Name: ", self.name)
    #     print("Age: ", self.age)
    #     print("Experience: ", self.experience)
    #     print("Email: ", self.gmail)
       

        # self.photo_desc()
        # print("--------------------------------------------")
    
       