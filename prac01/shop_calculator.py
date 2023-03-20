num_of_items = -1

while num_of_items < 0:
    num_of_items = int(input("Enter the number of items: "))
    if num_of_items < 0:
        print("Invalid number of items!")

total_price = 0

for i in range(num_of_items):
    item_price = float(input(f"Enter the price of item {i+1}: "))
    total_price += item_price

if total_price > 100:
    total_price *= 0.9

print(f"The total price for {num_of_items} items is ${total_price:.2f}")