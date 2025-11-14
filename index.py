cart = []

while True:
    action = input("Enter item to add, 'remove', or 'q' to quit: ").lower()

    if action == "remove":
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print("Removed!")
        else:
            print("Item not found!")

    elif action == "q":
        break

    else:
        cart.append(action)  
        print("Added!")

print("\nFinal Shopping List:")
print(cart)

