from flask import Flask, render_template, redirect, url_for, request, flash, session
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined



# means: take this file and turns it into a flask app

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """get homepage"""
   
    return render_template('index.html')
    
@app.route('/login', methods=['POST'])
def login():
    """process login"""
    
    
    session['username']=[]
    
    # Validate username
    if (not request.form.get("username") or not request.form.get("password")) :
        flash("Please make sure you complete all the fields", "warning")
        return redirect('/')    
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        user = crud.get_user(username)
        
        if (not user or password != password):
            flash("Something went wrong please check your username and password and try again", "warning") 
            return redirect('/')  
        elif (username == username and password == password):
        
            session['user'] = username
    
        return redirect(url_for('show_user_dashboard', user_id = user.user_id))
    

@app.route('/user/<user_id>')
def show_user_dashboard(user_id):
    """View user dashboard"""

    user = crud.get_user_by_id(user_id)

    print("printuser", user)
    return render_template('user_dashboard.html', user=user)


if __name__== "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)


