from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "30302220jefferson"

userpass = "mysql+pymysql://jefferson:30302220@"
basedir = "127.0.0.1"
dbname = "/companydb"


app.config["SQLALCHEMY_DATABASE_URI"] = userpass + basedir + dbname

login_manager = LoginManager(app)
db = SQLAlchemy(app)
