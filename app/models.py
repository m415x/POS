from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.inspection import inspect
from datetime import datetime

from app import db



class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    user_name = db.Column(db.String(12), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_superadmin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    discharge_date = db.Column(db.DateTime)

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
    
    def set_active(self, active):
        self.is_active = active
        return self.is_active
    
    def set_discharge(self, date):
        self.discharge_date = date
        return self.discharge_date

    def get_superadmin(self):
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
        return Users.query.get(id)

    @staticmethod
    def get_by_user_name(user_name):
        return Users.query.filter_by(user_name=user_name).first()
    
    @staticmethod
    def get_by_super_admin():
        return Users.query.filter_by(is_superadmin=True).first()

    @staticmethod
    def get_all():
        return Users.query.all()
    
    @staticmethod
    def table_exist(table):
        return inspect(db.engine).has_table(table)
