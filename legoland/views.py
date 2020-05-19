from flask import Blueprint, render_template, url_for, request, session, flash
from .models import Product
from datetime import datetime
from .forms import CheckoutForm
from . import db

# product1 = Product('1', 'Star Wars - Ultimate Collector Millennium Falcon', 89.99, 'most_popular1.jpg', 300, 4, , "LEGO® Star Wars™ Millennium Falcon™ - Ultimate Collector's Edittion", 'Full Description', 'Specification')
# product2 = Product(
#     '2',
#     'Star Wards - Death Star',
#     79.99, 'most_popular2.jpg',
#     250,
#     4,
#     "LEGO® Star Wars™ Death Star™ - Ultimate Collector's Edittion",
#     'Full Description',
#     'Specification')
# product3 = Product(
#     '3',
#     'Ninjago - Masters of Spinjitzu',
#     49.99,
#     'most_popular3.jpg',
#     131,
#     3.5,
#     "LEGO® Ninjago - Masters of Spinjitzu",
#     'Full Description',
#     'Specification')
# mostpopular = [product1, product2, product3]
# products = mostpopular

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    products = Product.query.order_by(Product.name).all()
    return render_template('home.html', products=products)


@bp.route('/home')
def home():
    products = Product.query.order_by(Product.name).all()
    return render_template('home.html', products=products)


@bp.route('/shop/<string:sortby>')
def shop(sortby):
    # USE SORT BY TO FILTER
    products = Product.query.order_by(Product.name).all()
    return render_template('shop.html', products=products, sortby=sortby)


@bp.route('/product/<int:productid>/')
def product(productid):
    product = Product.query.get(productid)
    return render_template('product.html', product=product)


@bp.route('/order')
def order():
    products = Product.query.order_by(Product.name).all()
    return render_template('order.html', products=products)


@bp.route('/checkout/', methods=['POST', 'GET'])
def checkout():
    form = CheckoutForm()
    # if 'order_id' in session:

    #     #retrieve correct order object
    #     for x in orders:
    #             if int(x.id) == int(session['order_id']):
    #                 order = x

    #     if form.validate_on_submit():
    #         order.status = True
    #         order.firstname = form.firstname.data
    #         order.surname = form.surname.data
    #         order.email = form.email.data
    #         order.phone = form.phone.data
    #         print(order)
    #         flash('Thank you for your information')

    return render_template('checkout.html', form=form)

# @bp.route('/')
# def index():
#     return render_template('index.html', cities = cities)

# @bp.route('/tours/<int:cityid>/')
# def citytours(cityid):
#     citytours = []
#     # create list of tours for this city
#     for tour in tours:
#             if int(tour.city.id) == int(cityid):
#                 citytours.append(tour)
#     return render_template('citytours.html', tours = citytours)


# @bp.route('/order/', methods=['POST','GET'])
# def order():

#     tour_id = request.args.get('tour_id')
#     # is this a new order?
#     if 'order_id'not in session:
#         session['order_id'] = 1 # arbitry, we could set either order 1 or order 2

#     #retrieve correct order object
#     for x in orders:
#             if int(x.id) == int(session['order_id']):
#                 order = x
#     # are we adding an item? - will be implemented later with DB
#     if tour_id:
#         print('user requested to add tour id = {}'.format(tour_id))

#     return render_template('order.html', order = order, totalprice = order.total_cost)


# @bp.route('/deleteorder/')
# def deleteorder():
#     if 'order_id' in session:
#         del session['order_id']
#     return render_template('index.html')

# @bp.route('/deleteorderitem/', methods=['POST'])
# def deleteorderitem():
#     print('User wants to delete tour with id={}'.format(request.form['id']))
#     return render_template('index.html')
