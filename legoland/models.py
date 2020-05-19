from datetime import datetime


class Product:
    def __init__(self, id, name, price, image, numreviews, reviewscore, shortdescription, fulldescription, specification):
        self.id = id
        self.name = name
        self.price = price
        self.image = image
        self.fullstar = 0
        self.emptystar = 0
        self.halfstar = False

        self.reviewscore = reviewscore
        diff = 5 - self.reviewscore
        if isinstance(diff, int):
            self.emptystar = diff
        elif diff > 1:
            self.emptystar = int(diff - 0.5)
        if isinstance(self.reviewscore, int):
            self.fullstar = 5 - self.emptystar
        else:
            self.fullstar = int(5 - self.emptystar - 0.5)
            self.halfstar = True
        self.numreviews = numreviews
        self.reviewscore = reviewscore
        self.shortdescription = shortdescription
        self.fulldescription = fulldescription
        self.specification = specification

    def get_product_details(self):
        return str(self)

    def __repr__(self):
        str = "Id: {}, Name: {}, Price: {}, Image: {}, NumOfReviews: {}, ReviewScore: {}, ShortDescription: {}, FullDescription: {}, Specification: {} \n"
        str = str.format(self.id, self.name, self.price, self.image, self.numreviews,
                         self.reviewscore, self.shortdescription, self.fulldescription, self.specification)
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
        str = str.format(self.id, self.name, self.totalprice)
        return str
