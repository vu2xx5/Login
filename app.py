from flask import Flask
from routes import routes
from flask_sqlalchemy import SQLAlchemy
from extensions import db 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/login_demo?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)