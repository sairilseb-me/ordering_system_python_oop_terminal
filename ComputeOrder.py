

class Compute():
        def __init__(self):
            pass
            
        def compute_beverages(self, order):
            beverage_total = 0
            for item in order:
                beverage_total += item["price"]
            return beverage_total
        
        def compute_food(self, order):
            food_total = 0  
            for item in order:
                food_total += item["price"]
            return food_total
        
        def compute_total(self, beverage, food):
            return self.compute_beverages(beverage) + self.compute_food(food)