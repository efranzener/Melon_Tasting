"""Script to seed database"""

import os
import crud
import model
import server

import random
from random import choice
from datetime import datetime, timedelta
from faker import Faker

fake=Faker()


os.system("dropdb melon_tasting --if-exists")
os.system("createdb melon_tasting")

model.connect_to_db(server.app)
print("connected to db")
with server.app.app_context():
    model.db.create_all()

#set start and end dates for the random datetime   
start = datetime.now()+ timedelta(days=1)
end = datetime.now() + timedelta(days=30)

def create_random_datetime(start, end):
    """pick a random datetime"""  
    
    interval_days = end - start
    random_number = random.randrange(interval_days.days * 24 * 60 * 60)    
    
    random_datetime = start + timedelta(seconds=random_number)

    #check if random datetime is in the hour or hours and half mark, and if not it rounds it to be
    if random_datetime.minute > 0:

        random_datetime = random_datetime + (datetime.min - random_datetime) % timedelta(minutes=30)

    return random_datetime 
   

users_in_db=[]
def create_users():
    """create sample users"""

    for n in range(6):

        with server.app.app_context():  

            name = fake.name()
            splitted_name = name.split(" ")
            fname=splitted_name[0].strip()
            lname= splitted_name[1].strip()
            email= fname.lower()+f"{n}@test.com"
            username=fname[1] + lname.lower()
            password=fake.password()
            user = crud.create_user(name=name, email=email, username=username, password=password)
            
            model.db.session.add(user)
            model.db.session.commit()

def create_reservations():
    """create sample reservations""" 

    for n in range(1,6): 
        
        with server.app.app_context(): 
        
            # user_id = n
            date=create_random_datetime( start, end)
            time_string = date.strftime("%I:%M %p")
            if crud.check_availability_by_datetime(date, time_string):
                date = create_random_datetime( start, end)
                time_string = date.strftime("%I:%M %p")

            reservation = crud.create_reservation(user_id=n, date=date, time = time_string)

            model.db.session.add(reservation)
            model.db.session.commit()   


create_users()
create_reservations()
