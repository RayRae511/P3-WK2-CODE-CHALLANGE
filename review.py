class Review:
    all_reviews = []
    
    def __init__(self, customer, resturant, rate):
        self.customer = customer
        self.resturant = resturant
        self.rate = rate
        self.all_reviews.append(self)
        
    def rate(self):
        return self.rate
    
    @classmethod
    def all(self):
        return self.all.reviews
    
    def customer(self):
        return self.customer
    
    def resturant(self):
        return self.resturant