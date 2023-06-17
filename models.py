from extensions import db,login_manager
from app import app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email= db.Column(db.String(200), nullable=False)
    password= db.Column(db.String(255), nullable=False)
    reviews = db.relationship('Review', backref='user', lazy=True)
    
    

    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=password

    def save(self):
        db.session.add(self)
        db.session.commit()

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    is_active = db.Column(db.Integer, default=False)
    def __init__(self,user_id,product_id,is_active):
        self.user_id=user_id
        self.product_id=product_id
        self.is_active=is_active

    def save(self):
        db.session.add(self)
        db.session.commit()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price=db.Column(db.Integer)
    discount=db.Column(db.Integer)
    descriptiion = db.Column(db.String(150), nullable=False)
    image_url=db.Column(db.String(150), nullable=False)
    images=db.relationship("Imagee", backref="product")
    categoryid=db.Column(db.Integer,db.ForeignKey('category.id'), nullable=False)
    reviews = db.relationship('Review', backref='product', lazy=True)

    def __init__(self,name,price,discount,description,image_url,categoryid):
        self.name=name
        self.price=price
        self.descriptiion=description
        self.image_url=image_url
        self.discount=discount
        self.categoryid=categoryid
       

    def save(self):
        db.session.add(self)
        db.session.commit()

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    content = db.Column(db.Text)
    def __init__(self,user_id,product_id,content):
        self.user_id=user_id
        self.product_id=product_id
        self.content=content

    def save(self):
        db.session.add(self)
        db.session.commit()

class category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(150), nullable=False)
    products=db.relationship("Product", backref="category")

    def __init__(self,name):
        self.name=name
    def save(self):
        db.session.add(self)
        db.session.commit()




class Imagee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img=db.Column(db.String(150), nullable=False)
    proid=db.Column(db.Integer,db.ForeignKey('product.id'), nullable=False)

    def __init__(self,img,proid):
        self.img=img
        self.proid=proid
       

    def save(self):
        db.session.add(self)
        db.session.commit()



class contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    subject = db.Column(db.String(100), nullable=False)


    def __init__(self,name,email,message,subject):
        self.name=name
        self.email=email
        self.message=message
        self.subject=subject

    def save(self):
        db.session.add(self)
        db.session.commit()





