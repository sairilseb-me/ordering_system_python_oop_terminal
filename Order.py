class Order:
    def __init__(self):
        self.beverages = [
            {
                "id": 1,
                "name": "Espresso",
                "price": 39
            },
            {
                "id": 2,
                "name": "Strawberry frappuccino",
                "price": 30
            },
            {
                "id": 3,
                "name": "Iced caffee latte",
                "price": 25
            },
            {
                "id": 4,
                "name": "Caramel macchiato",
                "price": 35
            },
            {
                "id": 5,
                "name": "Iced Tea",
                "price": 20
            }
        ]
        
        self.food = [
            {
                "id": 1,
                "name": "Pastrami on Rye",
                "price": 100
            },
            {
                "id": 2,
                "name": "Tuna Wrap",
                "price": 120
            },
            {
                "id": 3,
                "name": "Cinnamon Roll",
                "price": 105
            },
            {
                "id": 4,
                "name": "Glazed Doughnut",
                "price": 110
            },
            {
                "id": 5,
                "name": "Blueberry Pancakes",
                "price": 150
            }
        ]
        
    def add_beverage(self, name, price):
        self.beverages.append({
            len(self.beverages) + 1,
            name,
            price
        })
        
    def add_food(self, name, price):
        self.food.append({
            len(self.food) + 1,
            name,
            price
        })
        
    def remove_beverage(self, id):
        for i in range(len(self.beverages)):
            if self.beverages[i]["id"] == id:
                self.beverages.pop(i)
        return "Beverage not found."
    
    def remove_food(self, id):
        for i in range(len(self.food)):
            if self.food[i]["id"] == id:
                self.food.pop(i)
                
        return "Food not found."
    
    def selected_beverage(self, id):
        for i in self.beverages:
            if id == i["id"]:
                return i
        return False
    
    def selected_food(self, id):
        for i in self.food:
            if id == i["id"]:
                return i
        return False
