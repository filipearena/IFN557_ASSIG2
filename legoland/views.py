from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Product, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    mostpopular = []
    products = Product.query.order_by(Product.numreviews).all()
    for x in range(4):
        mostpopular.append(products[x])
    return render_template('home.html', products=mostpopular)


@bp.route('/home')
def home():
    mostpopular = []
    products = Product.query.order_by(Product.numreviews).all()
    for x in range(4):
        mostpopular.append(products[x])
    return render_template('home.html', products=mostpopular)


@bp.route('/shop/<string:sortby>')
def shop(sortby):
    # USING SORT BY TO FILTER PRODUCTS ON SHOP PAGE
    if(sortby == 'review'):
        products = Product.query.order_by(Product.fullstar.desc()).all()
    elif(sortby == 'price'):
        products = Product.query.order_by(Product.price).all()
    else:
        products = Product.query.order_by(Product.numreviews.desc()).all()
    return render_template('shop.html', products=products, sortby=sortby)


@bp.route('/shop/')
def search():
    originalSearch = request.args.get('search')
    search = '%{}%'.format(originalSearch)
    products = Product.query.filter(Product.name.like(search)).all()
    return render_template('shop.html', products=products, search=originalSearch)


@bp.route('/product/<int:productid>/')
def product(productid):
    product = Product.query.get(productid)
    return render_template('product.html', product=product)


@bp.route('/order', methods=['POST', 'GET'])
def order():
    product_id = request.values.get('product_id')

    # retrieve order if there is one
    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status=False, firstname='', surname='',
                      email='', phone='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None

    # calculate totalprice
    totalprice = 0
    if order is not None:
        for product in order.products:
            totalprice = totalprice + product.price

    # are we adding an item?
    if product_id is not None and order is not None:
        product = Product.query.get(product_id)
        if product not in order.products:
            try:
                order.products.append(product)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('Product already in basket')
            return redirect(url_for('main.order'))
    if (len(order.products) == 0):
        if 'order_id' in session:
            flash('No products on the basket!')
            return redirect(url_for('main.home'))
    # products = Product.query.order_by(Product.name).all()
    return render_template('order.html', order=order, totalprice=totalprice)

# Delete specific basket items


@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id = request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        product_to_delete = Product.query.get(id)
        try:
            order.products.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.home'))

# Scrap basket


@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))


@bp.route('/checkout', methods=['POST', 'GET'], strict_slashes=False)
def checkout():
    form = CheckoutForm()
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            totalcost = 0
            for product in order.products:
                totalcost = totalcost + product.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash(
                    'Thank you! One of our awesome team members will contact you soon...')
                return redirect(url_for('main.home'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form=form)
