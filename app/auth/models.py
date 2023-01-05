from datetime import datetime
from slugify import slugify
from sqlalchemy.exc import IntegrityError

from app import db



class Poducts(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    info = db.Column(db.String(256), nullable=False)
    stock = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    price = db.Column(db.Integer)
    image_name = db.Column(db.String)
    history = db.relationship('price_history', backref='products', lazy=True, order_by='desc(price_history.created)')
    sales = db.relationship('sales_details', backref='products', lazy=True, order_by='desc(sales_details.created)')
    
    def __repr__(self):
        return f'<Product {self.name}>'
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # @staticmethod
    # def get_by_slug(slug):
    #     return Post.query.filter_by(title_slug=slug).first()

    # @staticmethod
    # def get_all():
    #     return Post.query.all()
        
    # @staticmethod
    # def get_by_id(id):
    #     return Post.query.get(id)
    
    # @staticmethod
    # def all_paginated(page=1, per_page=2):
    #     return Post.query.order_by(Post.created.asc()).\
    #         paginate(page=page, per_page=per_page, error_out=False)


class SalesDetails(db.Model):
    __tablename__ = 'sales_details'
    
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sales.id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    info = db.Column(db.String(256), nullable=False)
    quantity = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __repr__(self):
        return f'<Product {self.name}>'
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # @staticmethod
    # def get_by_slug(slug):
    #     return Post.query.filter_by(title_slug=slug).first()

    # @staticmethod
    # def get_all():
    #     return Post.query.all()
        
    # @staticmethod
    # def get_by_id(id):
    #     return Post.query.get(id)
    
    # @staticmethod
    # def all_paginated(page=1, per_page=2):
    #     return Post.query.order_by(Post.created.asc()).\
    #         paginate(page=page, per_page=per_page, error_out=False)



# class Comment(db.Model):
    
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='SET NULL'))
#     user_name = db.Column(db.String)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
#     content = db.Column(db.Text)
#     created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
#     def __init__(self, content, user_id=None, user_name=user_name, post_id=None):
#         self.content = content
#         self.user_id = user_id
#         self.user_name = user_name
#         self.post_id = post_id
        
#     def __repr__(self):
        
#         return f'<Comment {self.content}>'
    
#     def save(self):
        
#         if not self.id:
#             db.session.add(self)
#         db.session.commit()
        
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
        
#     @staticmethod
#     def get_by_post_id(post_id):
        
#         return Comment.query.filter_by(post_id=post_id).all()