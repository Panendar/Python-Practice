cart =[]
prices =[]
not_quit = True
print("===================SHOPPING CART==================")
while not_quit:
    choice = int(input("1.ADD TO CART\n2.REMOVE FROM CART\n3.VIEW CART\n4.VIEW TOTAL PAYMENT\n5.EXIT\n Enter your choice: "))
    print("========================================")
    if choice == 1:
        item = input("ENTER THE ITEM ADD TO CART: ")
        price = float(input("ENTER THE PRICE OF THE ITEM:"))
        cart.append(item)
        prices.append(price)
        print("========================================")
    elif choice == 2:
        print("========================================")
        item = input("ENTER THE ITEM TO REMOVE FROM CART: ")
        if item in cart:
            index =cart.index(item)
            cart.pop(index)
            prices.pop(index)
        else:
            print("ITEM NOT FOUND IN CART!")
        print("========================================")
    elif choice == 3:
        print("========================================")
        if cart:
            print("YOUR CART ITEMS ARE:")
            for i in range(len(cart)):
                print(f"{cart[i]} - ${prices[i]:.1f}")
        else:
            print("YOUR CART IS EMPTY!.....\nPLEASE ADD ITEMS TO CART")
        print("========================================")
    elif choice == 4:
        print("========================================")
        if prices:
            sum_prices = 0
            for i in range(len(prices)):
                sum_prices += prices[i]
            print(f"YOUR TOTAL PRICE IS: ${sum_prices:.1f}")
        else:
            print("PLEASE DO SOME SHOPPING FIRST!....")
        print("========================================")
    elif choice == 5:
        not_quit = False
        print("THANK YOU FOR SHOPPING WITH US!")
        print("========================================")