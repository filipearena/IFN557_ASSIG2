'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the miltontours package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    from miltontours import db, create_app
    db.create_all(app=create_app())
The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or tours table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000

# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

Use DB Browser for SQLite to check that the data is as expected before 
continuing.
'''

from flask import Blueprint
from . import db
from .models import Product
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database


@bp.route('/dbseed')
def dbseed():
    p1 = Product(name="LEGO® Star Wars™ Millennium Falcon™ - Ultimate Collector's Edittion", shortdescription='Star Wars - Ultimate Collector Millennium Falcon', image='milenium.jpg', fulldescription='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                 price=89.99, fullstar=5, halfstar=False, emptystar=0, numreviews=534, specification='Specification Text')
    p2 = Product(name="LEGO® Star Wars™ Death Star™ - Ultimate Collector's Edittion", shortdescription='Star Wars - Death Star', image='death_star.jpg', fulldescription='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                 price=69.99, fullstar=4, halfstar=True, emptystar=0, numreviews=468, specification='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed enim ut sem viverra aliquet eget sit. Nunc faucibus a pellentesque sit amet porttitor eget. Lacus luctus accumsan tortor posuere ac ut consequat semper. In dictum non consectetur a erat. At varius vel pharetra vel turpis. Ornare arcu odio ut sem nulla. Venenatis a condimentum vitae sapien pellentesque habitant morbi tristique senectus. Sollicitudin aliquam ultrices sagittis orci a scelerisque purus. Diam ut venenatis tellus in metus vulputate eu.')
    p3 = Product(name='LEGO® Ninjago - Masters of Spinjitzu', shortdescription='Ninjago - Masters of Spinjitzu', image='ninjago_masters.jpg', fulldescription='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                 price=40.00, fullstar=3, halfstar=True, emptystar=1, numreviews=168, specification='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed enim ut sem viverra aliquet eget sit. Nunc faucibus a pellentesque sit amet porttitor eget. Lacus luctus accumsan tortor posuere ac ut consequat semper. In dictum non consectetur a erat. At varius vel pharetra vel turpis. Ornare arcu odio ut sem nulla. Venenatis a condimentum vitae sapien pellentesque habitant morbi tristique senectus. Sollicitudin aliquam ultrices sagittis orci a scelerisque purus. Diam ut venenatis tellus in metus vulputate eu.')
    p4 = Product(name='LEGO® City - Space Explorer', shortdescription='City - Space Explorer', image='city.jpg', fulldescription='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                 price=72.99, fullstar=3, halfstar=True, emptystar=1, numreviews=101, specification='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed enim ut sem viverra aliquet eget sit. Nunc faucibus a pellentesque sit amet porttitor eget. Lacus luctus accumsan tortor posuere ac ut consequat semper. In dictum non consectetur a erat. At varius vel pharetra vel turpis. Ornare arcu odio ut sem nulla. Venenatis a condimentum vitae sapien pellentesque habitant morbi tristique senectus. Sollicitudin aliquam ultrices sagittis orci a scelerisque purus. Diam ut venenatis tellus in metus vulputate eu.')
    p5 = Product(name='LEGO® Classic Box', shortdescription='Classic Box', image='classic.jpg', fulldescription='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                 price=59.99, fullstar=5, halfstar=False, emptystar=0, numreviews=628, specification='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed enim ut sem viverra aliquet eget sit. Nunc faucibus a pellentesque sit amet porttitor eget. Lacus luctus accumsan tortor posuere ac ut consequat semper. In dictum non consectetur a erat. At varius vel pharetra vel turpis. Ornare arcu odio ut sem nulla. Venenatis a condimentum vitae sapien pellentesque habitant morbi tristique senectus. Sollicitudin aliquam ultrices sagittis orci a scelerisque purus. Diam ut venenatis tellus in metus vulputate eu.')
    p6 = Product(name='LEGO® Super Mario - Starter Course (Expansion Set)', shortdescription='Super Mario - Starter Course (Expansion Set)', image='mario.jpg', fulldescription='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                 price=30.00, fullstar=4, halfstar=False, emptystar=1, numreviews=200, specification='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed enim ut sem viverra aliquet eget sit. Nunc faucibus a pellentesque sit amet porttitor eget. Lacus luctus accumsan tortor posuere ac ut consequat semper. In dictum non consectetur a erat. At varius vel pharetra vel turpis. Ornare arcu odio ut sem nulla. Venenatis a condimentum vitae sapien pellentesque habitant morbi tristique senectus. Sollicitudin aliquam ultrices sagittis orci a scelerisque purus. Diam ut venenatis tellus in metus vulputate eu.')
    p7 = Product(name='LEGO® Minions - The Rise of Gru', shortdescription='Minions - The Rise of Gru', image='minions.jpg', fulldescription='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                 price=60.00, fullstar=5, halfstar=False, emptystar=0, numreviews=442, specification='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed enim ut sem viverra aliquet eget sit. Nunc faucibus a pellentesque sit amet porttitor eget. Lacus luctus accumsan tortor posuere ac ut consequat semper. In dictum non consectetur a erat. At varius vel pharetra vel turpis. Ornare arcu odio ut sem nulla. Venenatis a condimentum vitae sapien pellentesque habitant morbi tristique senectus. Sollicitudin aliquam ultrices sagittis orci a scelerisque purus. Diam ut venenatis tellus in metus vulputate eu.')
    p8 = Product(name='LEGO® Ninjago - The Strike of the Ice Dragon', shortdescription='Ninjago - The Strike of the Ice Dragon', image='ninjago_dragon.jpg', fulldescription='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                 price=47.30, fullstar=3, halfstar=True, emptystar=1, numreviews=168, specification='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed enim ut sem viverra aliquet eget sit. Nunc faucibus a pellentesque sit amet porttitor eget. Lacus luctus accumsan tortor posuere ac ut consequat semper. In dictum non consectetur a erat. At varius vel pharetra vel turpis. Ornare arcu odio ut sem nulla. Venenatis a condimentum vitae sapien pellentesque habitant morbi tristique senectus. Sollicitudin aliquam ultrices sagittis orci a scelerisque purus. Diam ut venenatis tellus in metus vulputate eu.')
    p9 = Product(name='LEGO® Technic - Car Transporter', shortdescription='Technic - Car Transporter', image='technic.jpg', fulldescription='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                 price=45.99, fullstar=2, halfstar=True, emptystar=2, numreviews=58, specification='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed enim ut sem viverra aliquet eget sit. Nunc faucibus a pellentesque sit amet porttitor eget. Lacus luctus accumsan tortor posuere ac ut consequat semper. In dictum non consectetur a erat. At varius vel pharetra vel turpis. Ornare arcu odio ut sem nulla. Venenatis a condimentum vitae sapien pellentesque habitant morbi tristique senectus. Sollicitudin aliquam ultrices sagittis orci a scelerisque purus. Diam ut venenatis tellus in metus vulputate eu.')
    try:
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)
        db.session.add(p7)
        db.session.add(p8)
        db.session.add(p9)
        db.session.commit()
    except:
        return 'There was an issue adding the cities in dbseed function'

    return 'DATA LOADED'
