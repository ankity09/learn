def main():    
    product_stock = {"computer":35, "chair": 100, "desk": 20, "iphone": 15}
    print("The current stock")
    print (product_stock)

    def show_functions():
        print("\n**********************************************")
        print("1. Generateoverall stats forall products (total #, avg #, min, and max)* ")
        print("2. Calculate the amount for a given product* ")
        print("3. Update the amount for a given product")
        print("*********************************************\n")
        choice = input("Enter your choice: ")
        return(choice)

    def gen_stats(product):
        total = sum(product.values())
        avg = float(sum(product.values())) / len(product)
        minimum = min(product.values())
        maximum = max(product.values())
        return(total, avg, minimum, maximum)
    
    def check_stock(product, product_name):
        product_value = product[product_name]
        print("There are ",product_value, product_name, "in stock")
        return(product_value)

    def update_stock(product, product_name, update_amount):
        updated_value = product[product_name] + update_amount
        product[product_name] = updated_value
        return(product) 

    
    chk = True
    while chk == True: #Creates Infinite Loop for choice selection
        choice = show_functions()

        if choice == '1':
            total, avg, minimum, maximum = gen_stats(product_stock)
            print ("total:",total,"\naverage:",avg ,"\nminimum:",minimum,"\nmaximum:",maximum)

        elif choice == '2':
            product_name = input("Enter Name of Product to be checked: ")
            check_stock(product_stock, product_name)

        elif choice == '3':
            product_name = input("Enter the name of the Product: ")
            update_amount = int(input("Enter the amount, Example: 5, -5 : "))
            updated_stock = update_stock(product_stock, product_name, update_amount)
            print ("The updated stock:")
            print (updated_stock)

        else:  #Breaks out of loop, when one of the choices is not selected
            print ("wrong operations...")
            chk = False
if __name__ == '__main__':
    main()