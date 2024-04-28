from Order import Order

class DisplayMenu(Order):
    def __init__(self):
        super().__init__()
        
    def display_beverages(self):
        print("Beverages: ")
        for i in self.beverages:
            print(f'{i["id"]}. {i["name"]} - {i["price"]}')
    
    def display_food(self):
        print("Food: ")
        for i in self.food:
            print(f'{i["id"]}. {i["name"]} - {i["price"]}')
    
    