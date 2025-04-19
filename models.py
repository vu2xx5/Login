from extensions import db

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

def get_user_by_credentials(username, password):
    return users.query.filter_by(username=username, password=password).first()
