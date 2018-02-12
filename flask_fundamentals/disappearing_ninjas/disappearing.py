from flask import Flask, render_template, request, redirect, url_for
import os# Import Flask to allow us to create our app.

disappearing_ninjas = os.path.join('static', 'images')

app = Flask(__name__)
app.config['flask_fundamentals'] = disappearing_ninjas                         # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def index():
  return render_template("index.html")   # Return the string 'Hello World!' as a response.

@app.route('/ninja', methods=['GET'])
def ninja():
  return render_template('ninja.html')

@app.route('/ninja/blue', methods=['GET'])
def blue():
  return render_template('blue.html')

@app.route('/ninja/red', methods=['GET'])
def red():
  return render_template('red.html')

@app.route('/ninja/purple', methods=['GET'])
def purple():
  return render_template('purple.html')

@app.route('/ninja/orange', methods=['GET'])
def orange():
  return render_template('orange.html')

@app.route('/ninja/<color>', methods=['GET'])
def april(color):
  if color != 'red':
    return render_template('april.html')
  elif color != 'blue':
    return render_template('april.html')
  elif color != 'purple':
    return render_template('april.html')
  elif color != 'orange':
    return render_template('april.html')


app.run(debug=True)     