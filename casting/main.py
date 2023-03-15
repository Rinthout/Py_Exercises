# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1.
leek_price = 2
print("Leek is " + str(leek_price) + " euro per kilo.")

# Part 2.
order = "leek 4"
# print(order.find("4"))
amount = int(order[5])

sum_total = leek_price * amount
print(sum_total)

# Part 3.
price_broccoli_kg = 2.34
order_broccoli = 'broccoli 1.6'
amount_broccoli = float(order_broccoli[9:])
price = round((amount_broccoli * price_broccoli_kg), 2)

print(str(amount_broccoli) + "kg broccoli costs " + str(price) + "e")

