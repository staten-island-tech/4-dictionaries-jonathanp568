items = [ {
    "name": "Soda",
    "price": 2.00,
    "company": "Coca Cola"},
    {
    "name": "24 pack crayons",
    "price": 10.00,
    "company": "Crayola"}
,{
    "name": "Toothpaste",
    "price": 5.00,
    "company": "Colgate"}
,{
    "name": "IPhone 15 Max",
    "price": 1896.00,
    "company": "Apple"}
,{
    "name": "Chips",
    "price": 4.00,
    "company": "Lays"}]
cart = []
total = 0
welcome = input(f"What would you like to buy? {items} Type confirm to check out.")
while welcome != "confirm":
    if welcome == items[0]["name"]:
        welcome = input("Would you like to buy anything else?")
        cart.append(items[0]["name"])
        total += items[0]["price"]
    elif welcome == items[1]["name"]:
        welcome = input("Would you like to buy anything else?")
        cart.append(items[1]["name"])
        total += items[1]["price"]
    elif welcome == items[2]["name"]:
        welcome = input("Would you like to buy anything else?")
        cart.append(items[2]["name"])
        total += items[2]["price"]
    elif welcome == items[3]["name"]:
        welcome = input("Would you like to buy anything else?")
        cart.append(items[3]["name"])
        total += items[3]["price"]
    elif welcome == items[4]["name"]:
        welcome = input("Would you like to buy anything else?")
        cart.append(items[4]["name"])
        total += items[4]["price"]
    else:
        welcome = input("We don't have that here.")
print(f"You have purchased:{cart}")
print(f"The total is:{total}")