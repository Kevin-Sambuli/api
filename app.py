from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:kevoh@127.0.0.1:5432/test"
app.config["SECRET_KEY"]="secret"

db = SQLAlchemy(app)

@app.before_first_request
def create():
    db.create_all()

# importing db
from model.forex import Forex

@app.route("/exchangerate", methods=['GET', 'POST'])
def home():

    return "home"




if __name__ == "__main__":
    app.run()