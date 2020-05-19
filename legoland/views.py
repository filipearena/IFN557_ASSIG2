from flask import Blueprint, render_template, url_for, request, session, flash
from .models import Product
from datetime import datetime
from .forms import CheckoutForm

product1 = Product(
    '1',
    'Star Wars - Ultimate Collector Millennium Falcon',
    89.99,
    'most_popular1.jpg',
    300,
    4.5,
    "LEGO® Star Wars™ Millennium Falcon™ - Ultimate Collector's Edittion",
    'Full Description',
    'Specification')
product2 = Product(
    '2',
    'Star Wards - Death Star',
    79.99, 'most_popular2.jpg',
    250,
    4,
    "LEGO® Star Wars™ Death Star™ - Ultimate Collector's Edittion",
    'Full Description',
    'Specification')
product3 = Product(
    '3',
    'Ninjago - Masters of Spinjitzu',
    49.99,
    'most_popular3.jpg',
    131,
    3.5,
    "LEGO® Ninjago - Masters of Spinjitzu",
    'Full Description',
    'Specification')
mostpopular = [product1, product2, product3]
products = mostpopular

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('home.html', products=mostpopular)


@bp.route('/home')
def home():
    return render_template('home.html', products=mostpopular)


@bp.route('/shop/<string:sortby>')
def shop(sortby):
    return render_template('shop.html', products=mostpopular, sortby=sortby)


@bp.route('/product/<int:productid>/')
def product(productid):
    selectedproduct = 1
    fullstar = 0
    emptystar = 0
    halfstar = False
    for product in products:
        print(product.reviewscore)
        if int(product.id) == int(productid):
            selectedproduct = product
            diff = 5 - product.reviewscore
            if isinstance(diff, int):
                emptystar = diff
            elif diff > 1:
                emptystar = int(diff - 0.5)
            if isinstance(product.reviewscore, int):
                fullstar = 5 - emptystar
            else:
                fullstar = int(5 - emptystar - 0.5)
                halfstar = True
    return render_template('product.html', product=selectedproduct, fullstar=fullstar, halfstar=halfstar, emptystar=emptystar)


@bp.route('/order')
def order():
    return render_template('order.html', products=mostpopular)


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
