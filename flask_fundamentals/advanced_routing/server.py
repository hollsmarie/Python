from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users/<username>')
def show_user_profile(hollllllyv):
    print username
    return render_template("user.html")
app.run(debug=True)


