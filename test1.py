from DisplayMenu import DisplayMenu
from Customer import Customer
from Order import Order
from ComputeOrder import Compute

display_menu = DisplayMenu()
order = Order()


Customer.greeting()

cust_name = input("Enter Customer Name: ")
compute = Compute()

c_1 = Customer(cust_name, [], [], 0)

display_option = True
select_option = 0

while display_option:
    print("What would you like to do?")
    print("1. Display Menu")
    print("2. Select Beverage")
    print("3. Select Food")
    print("4. Add additional Food")
    print("5. Add additional Beverage")
    print("6. Bill")
    print("9: Exit")
    
    select_option = int(input("Enter option: "))
    
    if select_option == 1:
        display_menu.display_beverages()
        display_menu.display_food()
    elif select_option == 2:
        display_menu.display_beverages()
        bev_id = int(input("Enter Beverage ID: "))
        selected_beverage = order.selected_beverage(bev_id)
        if selected_beverage != False:
            c_1.beverage.append(selected_beverage)
        else:
            print("Beverage not found.")
    elif select_option == 3:
        display_menu.display_food()
        food_id = int(input("Enter Food ID: "))
        selected_food = order.selected_food(food_id)
        if selected_food != False:
            c_1.food.append(selected_food)
        else:
            print("Food not found.")
    elif select_option == 6:
        c_1.total = compute.compute_total(c_1.beverage, c_1.food)
        c_1.display_order()
        
    elif select_option == 9:
        print("Thank you!")
        display_option = False
    




