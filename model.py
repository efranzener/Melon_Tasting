""" Model for Melon Tasting Reservation """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta


db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    

    # reservation = a list of Reservations objects
    

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"
    

class Reservation(db.Model):
    """A melon tasting reservation"""
    
    __tablename__ = "reservations"
    
    reservation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id")) 
    date = db.Column(db.DateTime, default=datetime.today(), nullable=False)
    time = db.Column(db.String, default=(datetime.now() + (datetime.min - datetime.now()) % timedelta(minutes=30)).strftime("%I:%M %p"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    user = db.relationship("User", backref="reservations")

    
    def __repr__(self):
        return f"<User user_id={self.user_id} date={self.date}>"
 
def test_data():
    """create some test data"""

    User.query.delete()
    Reservation.query.delete()

    user1 = User(name="Marcio Januario", email="jmarcio@test.com", username="jmarcio", password="JankshT1G")
    user2 = User(name="Marcela Oliveira", email="omarcela@test.com", username="omarcela", password="JKlnaksJ234?")
    
    db.session.add_all([user1, user2])
    db.session.commit()

    
    reservation1 = Reservation(user_id=1)
    
    reservation2 = Reservation(user_id=2)

    db.session.add_all([reservation1, reservation2])
    db.session.commit()


def connect_to_db(app, db_uri="postgresql:///melon_tasting", echo=False):
    """Connect to database."""
    

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = echo
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

  

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
   

    connect_to_db(app)
    
