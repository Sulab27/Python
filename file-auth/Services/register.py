"""this is register"""
from .file_io import file_appender
from Models.user import get_last_user_id

def register(username:str,password:str,email:str)->None:

    user_id = get_last_user_id() +1
    user = f"{user_id},{username},{email},{password}\n"
    # file_writer("data/users.csv", user)
    print("-----------SUCCESS-----------")
    file_appender("data/users.csv", user)
    