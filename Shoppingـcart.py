items_dict = {}
while True:
    print("-" * 30)
    print("1. Add item")
    print("2. Remove item")
    print("3. Total price shopping cart")
    print("4. Display shopping cart")
    print("5. Exit")
    print("-" * 30)
    user_input = int(input("Enter your selection: "))

    if user_input == 1:
        while True:
            user = input("Enter your name: ")
            if user == "":
                break
            else:
                item = input("Enter name item: ")
                number = int(input("Enter number of item: "))
                price = int(input("Enter price item: "))
                if user in items_dict:
                    if item in items_dict[user]:
                        # items_dict[user]['price']=price
                        items_dict[user][item]["count"] += number
                    else:
                        items_dict[user][item] = {"count": number, "price": price}

                else:
                    items_dict[user] = {item: {"count": number, "price": price}}

    elif user_input == 2:
        user = input("Enter your name: ")
        if user in items_dict:
            remove_item = input("Enter item for delete: ")

            if remove_item in items_dict[user]:
                items_dict[user].pop(remove_item)
                print(f'success deleted "{remove_item}"')

    elif user_input == 3:
        add = 0
        user = input("Enter your name: ")
        if user in items_dict:
            for item in items_dict[user].values():
                add += item["count"] * item["price"]
        print(f"total price is: {add}")

    elif user_input == 4:
        print("your shopping cart:")
        user = input("Enter your name: ")
        if user in items_dict:
            for item, other in items_dict[user].items():
                print(f"{user}: {item}- {other['count']}- {other['price']}$")
    
    elif user_input == 5:
        break
    else:
        raise ValueError("Number input must be 1-5")
