class Resturant:
    all_resturants = []
    
    def __init__(self, name):
        self.name = name
        self.all_resturants.append(self)
    
    def name(self):
        return self.name
    
    def reviews(self):
        return [review for review in Review.all() if review.resturant() == self]
    
    def customers(self):
        return list(set([review.customer() for review in self.reviews()]))
    
    @classmethod
    def all(self):
        return self.all_resturants
    
    def avarage_star_review(self):
        total_rating = 0
        num_reviews = 0
        for review in self.reviews():
            total_rating += review.rating()
            num_reviews += 1
        if num_reviews > 0:
            return total_rating / num_reviews
        else:
            return 0.0