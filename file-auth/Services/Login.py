"""For login the data 
"""
from Services.file_io import file_reader


def login(username:str, password:str):
    print(username, password, "login function ma aayo")
    status = False
    users = file_reader('data/users.csv')
    for user in users:
        print(f"user le haneko username {username}")
        print(f"file ma vako username {user.split(',')[1]}")
        if username.strip() == str(user.split(',')[1].strip()):
            if password.strip() == user.split(',')[3].strip():
                status = True
                # print(password, user.split(',')[3].strip(), "mileko password haru")
                new_user = f"{user.split(',')[0]},{user.split(',')[1]},{user.split(',')[2]},{user.split(',')[3]},,1\n"
                users.remove(user)
                users.append(new_user)
                print("Login successful")
                return status
            else:
                 print("password incorrect")
                 return status
        else:
            print("username not found")
            
    return status
            
             