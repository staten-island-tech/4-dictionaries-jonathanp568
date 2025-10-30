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
    num = -1
    for i in items:
        num += 1
        if welcome == items[num]["name"]:
            welcome = input("Would you like to buy anything else?")
            cart.append(items[num]["name"])
            total += items[num]["price"]
    else:
            welcome = input("We don't have that here.")
print(f"You have purchased:{cart}")
print(f"The total is:{total}")