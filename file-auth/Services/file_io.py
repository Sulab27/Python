"""reading files 
""" 

def file_reader(file):
    with open(file, 'r',encoding="utf-8") as f:
     data = f.readlines()
    return data

def file_writer(file,data):
    with open(  file, 'w',encoding="utf-8") as f:
     f.write(data)
    return True

def file_appender(file,data):
    with open(file, 'a',encoding="utf-8") as f:
     f.write(data)
    return True

def file_list_writer(file,data):
    with open(file, 'w',encoding="utf-8") as f:
      f.writelines(data)
    return True
