from datetime import datetime


class Product:
    def __init__(self, id, name, price, image, numreviews, shortdescription, fulldescription, specification):
        self.id = id
        self.name = name
        self.price = price
        self.image = image
        self.numreviews = numreviews
        self.shortdescription = shortdescription
        self.fulldescription = fulldescription
        self.specification = specification

    def get_product_details(self):
        return str(self)

    def __repr__(self):
        str = "Id: {}, Name: {}, Price: {}, Image: {}, NumOfReviews: {}, ShortDescription: {}, FullDescription: {}, Specification: {} \n" 
        str =str.format( self.id, self.name,self.price,self.image,self.numreviews,self.shortdescription,self.fulldescription,self.specification)
        return str

class Order:
    def __init__(self, id, name, totalprice):
        self.id = id
        self.name = name
        self.totalprice = totalprice

    def get_product_details(self):
        return str(self)

    def __repr__(self):
        str = "Id: {}, Name: {}, TotalPrice: {} \n" 
        str =str.format( self.id, self.name,self.totalprice)
        return str