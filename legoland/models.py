from datetime import datetime
from . import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    image = db.Column(db.String(60), nullable=False,
                      default='most_popular1.jpg')
    price = db.Column(db.Float)
    fullstar = db.Column(db.Integer)
    emptystar = db.Column(db.Integer)
    halfstar = db.Column(db.Boolean, default=False)
    numreviews = db.Column(db.Integer)
    shortdescription = db.Column(db.String(60), nullable=False)
    fulldescription = db.Column(db.String(500), nullable=False)
    specification = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        str = "Id: {}, Name: {}, Price: {}, Image: {}, NumOfReviews: {}, ShortDescription: {}, FullDescription: {}, Specification: {} \n"
        str = str.format(self.id, self.name, self.price, self.image, self.numreviews,
                         self.shortdescription, self.fulldescription, self.specification)
        return str


orderdetails = db.Table('orderdetails',
                        db.Column('order_id', db.Integer, db.ForeignKey(
                            'orders.id'), nullable=False),
                        db.Column('product_id', db.Integer, db.ForeignKey(
                            'products.id'), nullable=False),
                        db.PrimaryKeyConstraint('order_id', 'product_id'))


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    totalcost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    products = db.relationship(
        "Product", secondary=orderdetails, backref="orders")

    def __repr__(self):
        str = "id: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Date: {}, Products: {}, Total Cost: {}\n"
        str = str.format(self.id, self.status, self.firstname, self.surname,
                         self.email, self.phone, self.date, self.products, self.totalcost)
        return str
