items =[ {
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
""" storage = [item1, item2, item3, item4, item5]
cart = []
intro = input("Choose items. Type confirm to check out.")
confirm = str(confirm)
while intro != confirm:
    if intro == item1: """

for item in items:
    print(item['name'], item['company'])