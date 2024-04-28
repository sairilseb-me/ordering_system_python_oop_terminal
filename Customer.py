class Customer:
    def greeting():
        print("Welcome to Coffee Palace!")
    
    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total
        
    
    def display_order(self):
        string_result = "Order of " + self.name + " is"
        for i, item in enumerate(self.beverage):
            string_result += " " + item["name"]
            if i < len(self.beverage) - 1:
                string_result += ","
        
        for i, item in enumerate(self.food):
            string_result += " " + item["name"]
            if i < len(self.food) - 1:
                string_result += ","
                
        string_result += " and the total is " + str(self.total)
        
        print(string_result)

    
    
   