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

welcome = input("What would you like to buy? Type confirm to check out.")
print(items)
while welcome != "confirm":
    if welcome == "Soda":
        print(items[0]["name"])