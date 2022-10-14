""" Model for Melon Tasting Reservation """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False, unique=True)
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
    time = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    user = db.relationship("User", backref="reservations")

    
    def __repr__(self):
        return f"<User user_id={self.user_id} date={self.date}>"
 

def connect_to_db(app, db_uri="postgresql:///melon_tasting", echo=True):
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
    
