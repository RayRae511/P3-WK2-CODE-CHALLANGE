class Customer:
    all_customers = []
    
    def __init__(self, name, fam_name):
        self.name = name
        self.fam_name = fam_name
        self.reviews = []
        Customer.all_customers.append(self)
    
    def given_name(self):
        return self.name
    
    def fam_name(self):
        return self.fam_name
    
    def full_name(self):
        return f"{self.name} {self.fam_name}"
    
    @classmethod
    def all(self):
        return self.all_customers