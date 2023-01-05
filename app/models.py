from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db



class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    user_name = db.Column(db.String(12), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_superadmin = db.Column(db.Boolean, default=False)

    def __init__(self, name, email, user_name):
        self.name = name
        self.email = email
        self.user_name = user_name

    def __repr__(self):
        return f'<User {self.user_name}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def set_admin(self, admin):
        self.is_admin = admin
        return self.is_admin
    
    def set_superadmin(self, superadmin):
        self.is_superadmin = superadmin
        return self.is_superadmin

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_user_name(user_name):
        return User.query.filter_by(user_name=user_name).first()

    @staticmethod
    def get_all():
        return User.query.all()
    