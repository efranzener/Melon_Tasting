import unittest
import server
from server import app
from model import connect_to_db, db, test_data
from flask import session


class FlaskTestsDatabase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(server.app, db_uri="postgresql:///testdb")

        # Create tables and add sample data
        with server.app.app_context():
            db.create_all()
            test_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()
    
    def test_login(self):
        """Test login page."""

        result = self.client.post("/login",
                                  data={"username": "jmarcio", "password": "JankshT1G"},
                                  follow_redirects=True)
        self.assertIn(b"You are a valued user", result.data)

    def test_departments_list(self):
        """Test departments page."""

        result = self.client.get("/departments")
        self.assertIn(b"Legal", result.data)

    def test_departments_details(self):
        """Test departments page."""

        result = self.client.get("/department/fin")
        self.assertIn(b"Phone: 555-1000", result.data)




if __name__ == '__main__':
    unittest.main(verbosity=2)