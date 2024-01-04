from datetime import datetime
from main import Photo,Photographer

p1 = Photo(1,"River",10," hello from Fewa")
p2 = Photo(2,"Mountain",11,"Mardi Himal")
p3 = Photo(3,"Himal", 5.7, "Tihs is pic of Mountain Machhapuchre")
p4 = Photo(4,"Mahendrapool in 1998", 8.9, "This is picture of Pokhara Mahendrapol in 1998")


bob = Photographer(1,"Bob",10,[p1,p2],"Soch",datetime.now(),"mm@mail.com")
tom = Photographer(2,"Tom Hanks",28,  [p3, p4], "Reev IT", datetime.now(),"wwgmail.com")

# photos_of_bob = Bob.get_photos_desc()

bob.photographer_details()
tom.photographer_details()