import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MINIMUM_PRICE = 0.01
MAXIMUM_PRICE = 1000.0
STARTING_PRICE = 10.0
FILENAME = "stock_output.txt"

out_file = open(FILENAME, 'w')

price = STARTING_PRICE
day = 0
print(f"Starting price: ${price:,.2f}", file=out_file)

while MINIMUM_PRICE <= price <= MAXIMUM_PRICE:
    price_change = 0
    day += 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {day} price is: ${price:,.2f}", file=out_file)

out_file.close()