#creating a small grocery inventory program >> buy/add/exit
available_items = [
    ("apple", 10), ("milk", 4), ("bread", 3), ("banana", 2),
    ("chocolate", 1), ("cherry", 1), ("water", 25), ("beef", 1),
    ("cucumber", 2), ("spices", 3)
]

previously_stocked = set(item for item, _ in available_items)

while True:
    print("Available items: ", available_items)
    print("Please choose which action you would like to perform: buy / add / exit")
    action_input = input("buy - press 1 / add - press 2 / exit - press 3: ")

    if action_input == "1":  # BUY
        selected_item = input("Enter product name: ").lower()
        amount = int(input("Enter amount of product: "))
        is_exist = False

        for idx, (name, stock) in enumerate(available_items):
            if name == selected_item:
                is_exist = True
                if stock >= amount:
                    available_items[idx] = (name, stock - amount)
                    print(f"You bought {amount} {name}(s).")
                else:
                    print("Not enough stock.")
                break

        if not is_exist:
            print("Item not found.")

    elif action_input == "2":  # ADD
        selected_item = input("Enter product name: ").lower()
        amount = int(input("Enter amount to add: "))
        is_exist = False

        for idx, (name, stock) in enumerate(available_items):
            if name == selected_item:
                available_items[idx] = (name, stock + amount)
                is_exist = True
                break

        if not is_exist:
            available_items.append((selected_item, amount))

        previously_stocked.add(selected_item)
        print(f"{selected_item} added/updated in inventory.")

    elif action_input == "3":  # EXIT
        print("Previously stocked items:", previously_stocked)
        break

    else:
        print("Invalid choice. Please try again.")

