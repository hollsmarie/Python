from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re, md5, os, binascii
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[aA-zZ\s]+$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'login_register')

 
@app.route('/')
def index():
    if "user_id" in session:
        print session["user_id"]
        return redirect("/welcome")              
    return render_template('index.html')   

#VALIDATE
@app.route('/register', methods=['POST'])
def validate():

    errors = []
    first = request.form['first'] 
    last = request.form['last'] 
    email = request.form['email'] 
    password = request.form['password']
    salt =  binascii.b2a_hex(os.urandom(5))
    hashed_pw = md5.new(password + salt).hexdigest()
    confirm = request.form['confirm']
    
    if len(request.form['first']) <2:
        errors.append("First name cannot be blank!")
    elif not NAME_REGEX.match(request.form['first']):
        errors.append("First name must be valid and cannot contain numbers")

    
    if len(request.form['last']) <2:
        errors.append("Last Name cannot be blank!")
    elif not NAME_REGEX.match(request.form['last']):
       errors.append("Last name must be valid and cannot contain numbers")

    
    if len(request.form['email']) < 1:
        errors.append("Email cannot be blank!")

    elif not EMAIL_REGEX.match(request.form['email']):
        errors.append("Invalid Email Address!")
       
    
    if len(request.form['password']) <8:
        errors.append("Passwords must be at least 8 characters.")
       
    
    elif len(request.form['confirm']) <1:
        errors.append("Please confirm your password.")
     

    elif request.form['password'] != request.form['confirm']:
        errors.append("Passwords must match.")

    if len(errors) > 0:
        for error in errors:
            flash(error)
        return redirect('/')

    else:
        query = "INSERT INTO users (first, last, email, password, salt) VALUES(:first, :last, :email, :hashed_pw, :salt)"
        data = {
            'first': request.form['first'],
            'last': request.form['last'],
            'email':  request.form['email'],
            'hashed_pw': hashed_pw, 
             'salt': salt,
           }

    # return render_template("success.html", first=first, last=last, email=email) #Left variable references template 'name' 
    newUser=mysql.query_db(query, data)
    mysql.query_db(query, data)
    session["user_id"] = ['id']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/welcome')
def welcome():
   return render_template('welcome.html')

@app.route('/login', methods=['POST'])
def login():
    query1 = "SELECT * from users WHERE email = :email"
    data1 = {"email":request.form["email"]}
    databaseUser = mysql.query_db(query1,data1)
    if (databaseUser):
        session["user_id"] = databaseUser[0]['id']
        return redirect('/welcome')
    else:
        return redirect('/')
    


app.run(debug=True)


