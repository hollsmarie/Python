# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations

import re
# create a regular expression object that we can use run operations on

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['GET','POST'])
def submit():
    firstname = request.form['firstname'] 
    lastname = request.form['lastname'] 
    email = request.form['email'] 
    password = request.form['password']
    cpassword = request.form['cpassword']
    
    if len(request.form['firstname']) <1:
        flash("First name cannot be blank!")
        return redirect('/')
    
    if len(request.form['lastname']) <1:
        flash("Last Name cannot be blank!")
        return redirect('/')
    
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    
    if len(request.form['password']) <8:
        flash("Passwords must be at least 8 characters.")
        return redirect('/')
    
    elif len(request.form['cpassword']) <1:
        flash("Please confirm your password.")
        return redirect('/')

    elif request.form['password'] != request.form['cpassword']:
        flash("Passwords must match.")
        return redirect('/')
    else:
        return render_template("results.html", firstname=firstname, lastname=lastname, email=email)

    return redirect('/')
app.run(debug=True)

