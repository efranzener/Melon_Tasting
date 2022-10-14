"""CRUD Operations"""

from model import db, User, Reservation, connect_to_db

def create_user(name, email, username):
    """create and return a new user"""
    
    user = User(name=name, email=email, username=username)
    
    return user


def create_reservation(user_id, date, time):
    """create and return a new reservation for a user"""
    
    reservation = Reservation(user_id=user_id, date=date, time=time)
    
    return reservation

if __name__ == "__main__":
    from server import app
    
    connect_to_db(app)
 