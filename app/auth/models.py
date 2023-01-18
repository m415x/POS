from datetime import datetime
from dataclasses import dataclass
from app import db


# @dataclass
class Items(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    info = db.Column(db.String(256), nullable=False)
    stock = db.Column(db.Float)
    cost = db.Column(db.Float)
    price = db.Column(db.Float)
    img_name = db.Column(db.String)
    user = db.relationship('Users', backref='items', lazy=True)
    category = db.relationship('Categories', backref='items', lazy=True)
    
    def __init__(self, name, info, stock, cost, price, img_name, user_id=None, category_id=None):
        self.user_id = user_id
        self.category_id = category_id
        self.name = name.capitalize()
        self.info = info.capitalize()
        self.stock = stock
        self.cost = cost
        self.price = price
        self.img_name = img_name
        
    def __repr__(self):
        return self.id
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def json(self):
        return {
            "id": self.id,
            "category_id": self.category_id,
            "category": self.category.category,
            "name": self.name,
            "info": self.info,
            "stock": self.stock,
            "cost": self.cost,
            "price": self.price,
            "img_name": self.img_name
        }
        
    def get_img_name(self):
        return self.img_name

    @staticmethod
    def get_all():
        return Items.query.order_by(Items.id).all()
        
    @staticmethod
    def get_by_id(id):
        return Items.query.get(id)
    
    @staticmethod
    def get_order_by(field, order):
        return Items.query.order_by(Items.field.order()).all()


class SalesDetails(db.Model):
    __tablename__ = 'sales_details'
    
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sales.id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    info = db.Column(db.String(256), nullable=False)
    quantity = db.Column(db.Float)
    cost = db.Column(db.Float)
    price = db.Column(db.Float)
    sale = db.relationship('Sales', backref='sales_details', lazy=True)
    category = db.relationship('Categories', backref='sales_details', lazy=True)
    item = db.relationship('Items', backref='sales_details', lazy=True)
    
    def __init__(self, name, info, quantity, cost, price, sales_id=None, category_id=None, item_id=None):
        self.sale_id = sales_id
        self.category_id = category_id
        self.item_id = item_id
        self.name = name.capitalize()
        self.info = info.capitalize()
        self.quantity = quantity
        self.cost = cost
        self.price = price

    def __repr__(self):
        return f'<SalesDetails {self.name}>'
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return SalesDetails.query.all()
        
    @staticmethod
    def get_by_id(id):
        return SalesDetails.query.get(id)


class Sales(db.Model):
    __tablename__ = 'sales'
    
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total_cost = db.Column(db.Float)
    sub_total = db.Column(db.Float)
    method_id = db.Column(db.Integer, db.ForeignKey('pay_methods.id'), nullable=False)
    discount = db.Column(db.Float)
    total_sale = db.Column(db.Float)
    user = db.relationship('Users', backref='sales', lazy=True)
    method = db.relationship('PayMethods', backref='sales', lazy=True)
    
    def __init__(self, total_cost, sub_total, discount, total_sale, user_id=None, method_id=None):
        self.user_id = user_id
        self.total_cost = total_cost
        self.sub_total = sub_total
        self.method_id = method_id
        self.discount = discount
        self.total_sale = total_sale

    def __repr__(self):
        return f'<Sales {self.name}>'
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Sales.query.all()
        
    @staticmethod
    def get_by_id(id):
        return Sales.query.get(id)


class PayMethods(db.Model):
    __tablename__ = 'pay_methods'
    
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    method = db.Column(db.String(20), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))
    card = db.relationship('Cards', backref='pay_methods', lazy=True)
    
    def __init__(self, method):
        self.method = method.capitalize()

    def __repr__(self):
        return f'<PayMethods {self.name}>'
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return PayMethods.query.all()
        
    @staticmethod
    def get_by_id(id):
        return PayMethods.query.get(id)


class Cards(db.Model):
    __tablename__ = 'cards'
    
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    entity = db.Column(db.String(30), nullable=False)
    payment_surcharge = db.Column(db.Float)
    
    def __init__(self, entity, payment_surcharge):
        self.entity = entity.capitalize()
        self.payment_surcharge = payment_surcharge

    def __repr__(self):
        return f'<Cards {self.name}>'
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Cards.query.all()
        
    @staticmethod
    def get_by_id(id):
        return Cards.query.get(id)

class Categories(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(20), nullable=False)
    
    def __init__(self, category):
        self.category = category.capitalize()

    def __repr__(self):
        return f'<Categories {self.category}>'
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Categories.query.all()
        
    @staticmethod
    def get_by_id(id):
        return Categories.query.get(id)


class PriceHistory(db.Model):
    __tablename__ = 'price_history'
    
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(20), nullable=False)
    info = db.Column(db.String(256), nullable=False)
    stock = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    price = db.Column(db.Integer)
    item = db.relationship('Items', backref='price_history', lazy=True)
    user = db.relationship('Users', backref='price_history', lazy=True)
    
    def __init__(self, name, info, stock, cost, price, item_id=None, user_id=None):
        self.item_id = item_id
        self.user_id = user_id
        self.name = name.capitalize()
        self.info = info.capitalize()
        self.stock = stock
        self.cost = cost
        self.price = price

    def __repr__(self):
        return f'<PriceHistory {self.name}>'
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return PriceHistory.query.all()
        
    @staticmethod
    def get_by_id(id):
        return PriceHistory.query.get(id)