# Import Package to help with formatting currency
import locale
import json
from pathlib import Path
# load the menu
# get the path
script_dir = (Path(__file__).resolve()).parent
# import initial menu
with open(f'{script_dir}/my_menu.json', 'r') as f:
    menu = json.load( f)
    # print (json.dumps(menu,indent=4))
# Just a few house keeping to make display and frmat better
# Set the locale to use a specific currency format (e.g., US dollars)
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
# Define "clear screen" function to keep things neat
def clear_screen():
    print("\033[H\033[J")
# Menu dictionary
# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order ={}
i2 = 1
# Launch the store and present a greeting to the customer
# this was added to let this run for multiple orders. 
New_order=True
while New_order:
    # Customers may want to order multiple items, so let's create a continuous
    # loop
    place_order = True
    while place_order:
        # Ask the customer from which menu category they want to order
        clear_screen()
        print("\nWelcome to the variety food truck.\n")
        print("From which menu would you like to order?\n ")
        # Create a variable for the menu item number
        # Create a dictionary to store the menu for later retrieval
        i = 1
        menu_items = {}
        """
        Print the options to choose from menu headings 
        (all the first level dictionary items in menu
        """
        for key in menu.keys():
            print(f"{i}: {key}")
            # Store the menu category associated with its menu item number
            menu_items[i] = key
            # Add 1 to the menu item number
            i += 1

        # Get the customer's input
        menu_category = input("\nType menu number: ")

        # Check if the customer's input is a number
        if menu_category.isdigit():
            # Check if the customer's input is a valid option
            if int(menu_category) in menu_items.keys():
                # Save the menu category name to a variable
                menu_category_name = menu_items[int(menu_category)]
                # Print out the menu category name they selected
                clear_screen()
                print(f"You selected {menu_category_name}\n")

                # Print out the menu options from the menu_category_name
                print(f"What {menu_category_name} item would you like to order?\n")
                i = 1
                menu_items = {}
                print("Item # | Item name                | Price")
                print("-------|--------------------------|-------")
                for key, value in menu[menu_category_name].items():
                    # Check if the menu item is a dictionary to handle differently
                    if type(value) is dict:
                        for key2, value2 in value.items():
                            num_item_spaces = 24 - len(key + key2) - 3
                            item_spaces = " " * num_item_spaces
                            print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                            menu_items[i] = {
                                "Item name": key + " - " + key2,
                                "Price": value2
                            }
                            i += 1
                    else:
                        num_item_spaces = 24 - len(key)
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key}{item_spaces} | ${value}")
                        menu_items[i] = {
                            "Item name": key,
                            "Price": value
                        }
                        i += 1
                # 2. Ask customer to input menu item number
                menu_selection =  (input("\nType menu number: "))
                # 3. Check if the customer typed a number
                if menu_selection.isdigit():               
                    # Convert the menu selection to an integer (done with input)
                    menu_selection = int(menu_selection)
                    # 4. Check if the menu selection is in the menu items
                    if (menu_selection) in menu_items.keys():
                        # Store the item name as a variable (Opt out. not needed)
                        # Ask the customer for the quantity of the menu item
                        clear_screen()
                        item_quantity = (input(f"\n***100 limit per item please***\nHow many {menu_items[menu_selection]['Item name']} would you like?  "))
                        # Check if the quantity is a number, default to 1 if not
                        if item_quantity.isdigit():
                            item_quantity=(int(item_quantity))
                        else:
                            item_quantity=(int(1))
                        if item_quantity > 100: 
                            item_quantity = 100
                        # print (f"""\n{menu_items[menu_selection]['Item name']}      \
                        # ${menu_items[menu_selection]['Price']}     \ 
                        # {'item_quantity'}   \
                        # {round((menu_items[menu_selection]['Price'])*(item_quantity),2)}\n""")   
                        # Add the item name, price, and quantity to the order list
                        order[i2]={"Menu_item":(menu_items[menu_selection]['Item name']),
                                        "Price":(menu_items[menu_selection]['Price']),
                                        "Quantity":item_quantity,
                                        # Multiply the price by quantity for each item in the order list
                                        "Total":(menu_items[menu_selection]['Price']*item_quantity)
                        }
                        grand_total=0
                        clear_screen()
                        print("Item name                 | Price  |  Qty  |   Total ")
                        print("--------------------------|--------|-------|-------------")
                        for key in order.keys():
                            item_space=(" "*(25-int(len(str(order[key]['Menu_item'])))))
                            price_space=(" "*(7-int(len(str(locale.currency(order[key]['Price']))))))
                            qty_space=(" "*( 5-int(len(str(order[key]['Quantity' ])))))
                            total_space=(" "*( 12-int(len(str(locale.currency(order[key]['Total']))))))
                            grand_total=grand_total+(order[key]['Total'])
                            print(order[key]['Menu_item'],item_space,price_space,locale.currency(order[key]['Price']),
                                qty_space,order[key]['Quantity'],total_space,locale.currency(order[key]['Total']))
                        gtotal_space= (" "*(35-int(len(str(locale.currency(grand_total))))))
                        print(f"\nYour current total is{gtotal_space}{(locale.currency(grand_total))}\n")    
                        i2 = i2+1
                else:
                    # Tell the customer they didn't select a menu option
                    print(f"{menu_selection} was not a menu selection")
            else:
                # Tell the customer they didn't select a menu option
                print(f"{menu_category} was not a menu option.")
        else:
            # Tell the customer they didn't select a number
            print("Please select by using the number from the menu.")
        while True:
            # Ask the customer if they would like to order anything else
            keep_ordering = (input("Would you like to keep ordering? (Y)es or (N)o ")).lower()
                    # 5. Check the customer's input
            if keep_ordering == "y":
                break
                # Keep ordering
                # Exit the keep ordering question loop
            elif keep_ordering == "n":
                place_order = False
                break
                # Exit the keep ordering question loop
            else :
                # Tell the customer to try again
                clear_screen()
                print ("please try again")
                # loop back to main menu
    # Print out the customer's order
    #
    # Uncomment the following line to check the structure of the order
    # print(order)
    # 6. Loop through the items in the customer's order
    # 7. Store the dictionary items as variables
    # proposed changes
    grand_total=0
    if order:
        clear_screen()
        print("Thank you for your order\n")
        print("This is what we are preparing for you.\n")
        print("Item name                 | Price  | Qty |   Total ")
        print("--------------------------|--------|-----|-----------")
        for key in order.keys():
            item_space=(" "*(25-int(len(str(order[key]['Menu_item'])))))
            price_space=(" "*(7-int(len(str(locale.currency(order[key]['Price']))))))
            qty_space=(" "*( 3-int(len(str(order[key]['Quantity' ])))))
            total_space=(" "*( 11-int(len(str(locale.currency(order[key]['Total']))))))
            # 11. Calculate the cost of the order using list comprehension        grand_total=grand_total+(order[key]['Total'])
            # 10. Print the item name, price,quantity and subtotal
            print(order[key]['Menu_item'],item_space,price_space,locale.currency(order[key]['Price']),
            qty_space,order[key]['Quantity'],total_space,locale.currency(order[key]['Total']))
        gtotal_space= (" "*(32-int(len(str(locale.currency(grand_total))))))
        print(f"\nYour current total is{gtotal_space}{(locale.currency(grand_total))}\n")
    else:
        clear_screen()
        print("Thank you for coming.\n")
        print("We will miss you. Have a great day!")
        input()
    
    if input: 
        order_again=input("Would you like a new order(Y/N)? ").upper()
        if (order_again) == "Y":
            clear_screen()
        else:
            New_order = False
clear_screen()
print("Bye Bye")
input()
clear_screen()
