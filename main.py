#create photographer class 

class Photographer:
    def __init__(self,id,name="",age=0,photos="",company="",date="",email=""):
        self.id=id
        self.name=name    
        self.age=age
    
        if self.validate_photos(photos):
            print(f"Valid photos are added for this photographer {self.name}")
            self.photos=photos
        else:
            self.photos = list()

        # self.photo = photos if self.validate_photos(photos) else list()
        self.company=company
        self.date=date if self.validate_date(date) else "Invalid Date"
        self.email = email if self.validate_email(email) else "Invalid Email"

    def photo_desc(self):
        print(f"\nPhotos of photographer {self.name} are: ")
        for i,ele in enumerate(self.photos):
            print("ID: ",ele.id)
            print("Name: ",ele.photo_name)
            print("Photo Size: ", ele.size)
            print("Alternate Text", ele.alt_text)
            print()


    def photographer_details(self):
        print()
        print("ID: ",self.id)
        print(f"PHOTOGRAPHER {self.name} INFORMATION")
        print("Name: ", self.name)
        print("Company: ", self.company)
        print("Age: ", self.age)
        print("Email: ", self.email)
        print("Date ", self.date)

        self.photo_desc()
        print("--------------------------------------------------------")

    def validate_photos(self, _photos):
        status = False
        if isinstance(_photos,list):
            for _photo in _photos:
                status = False
                if isinstance(_photo, Photo):
                    status = True
                else:
                    status = False
        
        return status
            
    def validate_age(self,_age):
      return True  if (_age<20) and (_age>80) else False
            

    def validate_email(self,_email):
        if isinstance(_email,str):
            if("@" in _email) and ("." in _email):return True
            else:
                return False
        # return True if isinstance(_email,str) and (("@" in _email) and ("." in _email) and (_email.endswith(".com")))  else False

        
                 

    def validate_date(self,_date):
        if isinstance(_date,str):return True
        else: return False

       
    def __str__(self) -> str:
       return str(self.name)

class Photo:
    def __init__(self,id,photo_name="",size=0,alt_text=""):
        self.id=id
        self.photo_name=str(photo_name)
        self.size=size
        self.alt_text=alt_text




    