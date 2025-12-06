import csv
from sys import exit
from tabulate import tabulate


menu = {
    1: {"name": "burger", "price": 5.99},
    2: {"name": "shawarma", "price": 6.99},
    3: {"name": "pizza", "price": 8.99},
    4: {"name": "fries", "price": 2.99},   # menu for ordering
    5: {"name": "soda", "price": 1.49},
    6: {"name": "salad", "price": 4.99}
}

def main():
    user_choice = input("Type 'menu' to display the menu or 'order' to order: ").lower().strip()

    if not user_choice.isalpha():
        print("Invalid input: Please enter alphabetic characters only.")
        exit(1)

    if user_choice == "menu":
        display_menu()

        if ask_yes_no():
            order_items, total_price = order()
        else:
            exit(0)

    elif user_choice == "order":
        order_items, total_price = order()
    else:
        print("Sorry, we don't understand you!")
        exit(1)

    create_bill(order_items, total_price)


def display_menu():
    menu_data = [(item["name"], item["price"]) for item in menu.values()]
    print(tabulate(menu_data, headers=["Item", "Price"], tablefmt="grid"))


def ask_yes_no():
    while True:
        response = input("Do you want to order? Type (y/n): ").lower().strip()
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Please type 'y' or 'n'.")


def order():
    ordered_items = []
    total_price = 0
    while True:
        user_input = input("Type '<number> <food>' or 'finish' to stop ordering: ").lower().strip()
        parsed_items = check_input(user_input)

        if parsed_items is False:
            break

        for item_name in parsed_items:
            menu_item = check_item(item_name)
            if menu_item:
                ordered_items.append(menu_item)
                total_price += menu_item["price"]
            else:
                break

    return ordered_items, total_price


def check_input(user_input):
    items_list = []
    if user_input == "finish":
        return False

    try:
        quantity_str, item_name = user_input.split(" ")

        if not item_name.isalpha():
            raise ValueError

        try:
            quantity = int(quantity_str)
        except ValueError:
            raise ValueError

        for _ in range(quantity):
            items_list.append(item_name)

    except ValueError:
        print("Error input, write like this: '3 soda'")
        #raise ValueError

    return items_list


def check_item(item_name):
    for menu_item in menu.values():
        if item_name == menu_item["name"]:
            return menu_item
    print("We don't have this kind of food or drink here.")
    return False


def create_bill(ordered_items, total_price):
    with open("bill.txt", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Price"])
        for item in ordered_items:
            writer.writerow([item["name"], item["price"]])
        writer.writerow([f"Total: ${total_price:.2f}"])

    print("✅ Bill created successfully as bill.txt")


if name == "main":
    main()
