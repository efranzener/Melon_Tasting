"""CRUD Operations"""

from model import db, User, Reservation, connect_to_db

def create_user(name, email, username, password):
    """create and return a new user"""
    
    user = User(name=name, email=email, username=username, password=password)
    
    return user


def create_reservation(user_id, date, time):
    """create and return a new reservation for a user"""
    
    reservation = Reservation(user_id=user_id, date=date, time=time)
    
    return reservation

def get_user(username):
    """return a user by username in in database"""
    
    return User.query.filter(User.username == username).first()


def get_user_by_id(user_id):
    """return a user by its id"""
    
    return User.query.get(user_id)

def get_all_reservations():
    """return all reservations in database"""

    return Reservation.query.all()

def check_availability_by_datetime(date, time):
    """check if reservation date and time is available"""

    if Reservation.query.filter(Reservation.date == date and Reservation.time == time).first():
        return True
    return False





if __name__ == "__main__":
    from server import app
    
    connect_to_db(app)
 