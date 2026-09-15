#shopping cart Exercise
item= input("Enter the name of the first item: ")
price= float(input("Enter the price of the first item: "))
quantity= int(input("Enter the quantity of the first item: "))
total= price* quantity
print(f"the total cost of {quantity} {item} is ${total:.2f}")
