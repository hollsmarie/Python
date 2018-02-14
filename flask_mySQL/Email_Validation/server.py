from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "secretKey"

mysql = MySQLConnector(app,'email_validation')

@app.route('/')
def index():                      
    return render_template('index.html')   

#VALIDATE
@app.route('/emails', methods=['POST'])
def validate():
    query = "SELECT * from emails WHERE address = :address"
    data = {"address":request.form["emails"]}
    databaseEmail = mysql.query_db(query,data)
    if (databaseEmail):
        flash ("Valid Email")
    else:
        flash ("Not a valid email")
    return redirect('/')


# #SHOW EMAILS ENTERED
# @app.route('/emails/<email_id>')
# def show(email_id):
#     query = "SELECT * FROM emails WHERE id = :specific_id"
#     data = {'specific_id': email_id}
#     emails = mysql.query_db(query, data)
#     return render_template('index.html', one_email=emails[0])


# #UPDATE EMAILS ENTERED
# @app.route('/update_email/<email_id>', methods=['POST'])
# def update(email_id):
#     query = "UPDATE emails SET address = :emails WHERE id = :id"
#     data = {
#              'address': request.form['emails']
#            }
#     mysql.query_db(query, data)
#     return redirect('/')


app.run(debug=True)


