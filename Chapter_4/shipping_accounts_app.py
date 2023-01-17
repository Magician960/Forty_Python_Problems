#You are responsible for writing a program that will simulate logging into a business’s shipping
#accounts software. Once logged in your program will display the current costs of shipping x
#amount of items. Based on the number of items shipped, the cost to ship each item will vary.
#Once the cost to ship an item is set, your program will calculate the cost of shipping the entire
#order. Upon confirmation of the order, your program will place the order and prepare the
#shipment.

#List of authorised usernames
authorised_users = ["EramoM","allenj"]

#Welcome message
print("Welcome to the Shipping Accounts Program")

#Verify username
username = input("Hello, what is your username: ")
if username not in authorised_users:
    print("Sorry, you do not have an account with us. Goodbye.")
    quit()
else:
    print(f"\nHello {username}. Welcome back to your account.")

#Display shipping prices
print("Current shipping prices are as follows:")
print("\nShipping orders 0 to 100:\t$5.10 each")
print("Shipping orders 100 to 500:\t$5.00 each") 
print("Shipping orders 500 to 1000:\t$4.95 each") 
print("Shipping orders over 1000:\t$4.80 each")

#Ask user for no. of items shipped
shipping_amount = int(input("\nHow many items would you like to ship: "))

#Display total cost of shipping
if shipping_amount in range(0,101):
    print(f"To ship {shipping_amount} items it will cost you ${round(shipping_amount * 5.10,2)} at $5.10 per item")
elif shipping_amount in range(101,501):
    print(f"To ship {shipping_amount} items it will cost you ${round(shipping_amount * 5.00,2)} at $5.00 per item")
elif shipping_amount in range(501,1001):
    print(f"To ship {shipping_amount} items it will cost you ${round(shipping_amount * 4.95,2)} at $4.95 per item")
else:
    print(f"To ship {shipping_amount} items it will cost you ${round(shipping_amount * 4.80,2)} at $4.80 per item")

#Ask user to confirm order
if input("\nWould you like to place this order (y/n): ") == "y":
    print(f"Okay. Shipping your {shipping_amount} items.")
else:
    print("Okay, no order is being placed at this time.")