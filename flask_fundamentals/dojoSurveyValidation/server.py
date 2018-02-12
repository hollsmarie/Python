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
    name = request.form['name'] 
    email = request.form['email'] 
    location = request.form['location'] 
    language = request.form['language'] 
    comments = request.form['comments'] 

    if len(request.form['name']) <1:
        flash("Name cannot be blank!")
        return redirect('/')
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    if len(request.form['comments']) <1:
        flash("Please leave a comment")
        return redirect('/')
    elif len(request.form['comments']) > 120:
        flash("Comments have a 120 Character limit")
        return redirect('/')
    else:
        return render_template("result.html", name=name, email=email,location=location, language=language, comments=comments)

    return redirect('/')
app.run(debug=True)

