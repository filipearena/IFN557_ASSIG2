from datetime import datetime


class Product:
    def __init__(self, id, name, price, image):
        self.id = id
        self.name = name
        self.price = price
        self.image = image

    def get_product_details(self):
        return str(self)

    def __repr__(self):
        str = "Id: {}, Name: {}, Price: {}, Image: {} \n" 
        str =str.format( self.id, self.name,self.price,self.image)
        return str