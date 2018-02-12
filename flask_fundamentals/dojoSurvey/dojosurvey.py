from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['GET','POST'])
def result():
    name = request.form['name'] 
    location = request.form['location'] 
    language = request.form['language'] 
    comments = request.form['comments'] 
    print request.form
    return render_template("result.html", name=name,location=location, language=language, comments=comments)

app.run(debug=True)


# from flask import Flask, request,render_template  # Import Flask to allow us to create our app, and import
#                                           # render_template to allow us to render index.html.
# app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
#                                           # are running the file directly or importing it as a module.
# @app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
#                                           # following function to the '/' route. This means that
#                                           # whenever we send a request to localhost:5000/ we will run
#                                           # the following "hello_world" function.
# def form():
#   return render_template('form.html')    # Render the template and return it!

# @app.route('/process', methods=['POST'])
# def process():
#     name = request.form['name'] 
#     print name
#     return render_template('process.html')
# app.run(debug=True)                       # Run the app in debug mode.
