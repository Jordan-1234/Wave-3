numOfItems = int(input("Enter the amount of items purchased: "))
if numOfItems < 0:
    print("Incorrect amount of items")
else: 
    print("The shipping cost will be" , 10.95 + (2.95 * numOfItems))
