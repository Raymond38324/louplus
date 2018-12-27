from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config.update(dict(
    SECRET_KEY='a very very secret key',
    SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/seiya?charset=utf8'))

db=SQLAlchemy(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/jobs")
def jobs():
    return 'Jobs'

if __name__ == '__main__':
    app.run()
