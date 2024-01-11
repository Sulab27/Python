"""This is fo user
"""

from Services.file_io import file_reader

# class User:
#     def __init__(self,id,username,password,email):
#         self.id = id 
#         self.username = username
#         self.password = password
#         self.email = email
#     def __str__(self):
#         return f"{self.id},{self.username},{self.password},\n"
    
def get_last_user_id():
    users = file_reader("data/users.csv")
    if users[-1].split(",")[0] == "id":
        return 0
    return int(users[-1].split(",")[0])
              

