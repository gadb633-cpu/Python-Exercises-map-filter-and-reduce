# part 1
# 1. Add 10 to each number
numbers = [3, 7, 10, 15]
numbers_bigger_by_10 = map(lambda num:num+10,numbers)
print(list(numbers_bigger_by_10))

# 2. Turn prices into prices with tax
prices = [100, 50, 200, 80]
prices_with_17_present = map(lambda price:price + price*0.17,prices)
print(list(prices_with_17_present))

# 3. Get the length of each word
words = ["cat", "elephant", "dog", "python"]
length_list = map(lambda word:len(word),words)
print(list(length_list))

# 4. Make all names uppercase
names = ["dan", "maya", "ron", "lea"]
uppercase = map(lambda name:name.upper(),names)
print(list(uppercase))

# 5. Create short user messages
users = ["Noa", "Adam", "Lior", "Tamar"]
with_hello = map(lambda user:f"hello {user}",users)
print(list(with_hello))

# 6. Convert meters to centimeters
meters = [1.5, 2, 0.75, 3.2]
costing_to_centimeters = map(lambda meret:meret*100,meters)
print(list(costing_to_centimeters))

# 7. Create pass/fail text from grades
grades = [95, 40, 67, 88, 52]
result = map(lambda grade:"pass" if grade >=60 else "fail",grades)
print(list(result))

# 8. Create product names with prices
products = [
    {"name": "Bread", "price": 8},
    {"name": "Milk", "price": 6},
    {"name": "Eggs", "price": 15}]

list_with_strings = map(lambda product:f"{product["name"]} costs {product["price"]}",products)
print(list(list_with_strings))

# 9. Update player scores
players = [
    {"name": "Dana", "score": 70},
    {"name": "Yoni", "score": 85},
    {"name": "Rami", "score": 40}]

bigger_by_5 = map(lambda player:{"name":player["name"],"score":player["score"]+5},players)
print(list(bigger_by_5))

# 10. Create order summaries
orders = [
    {"id": 1, "item": "Book", "amount": 3, "price": 40},
    {"id": 2, "item": "Pen", "amount": 10, "price": 5},
    {"id": 3, "item": "Bag", "amount": 1, "price": 120}]
list_of_strings = map(lambda order: f"order {order["id"]} :{order["item"]} total is {order["amount"]*order["price"]}",orders)
print(list(list_of_strings))

# Part 2 — filter Exercises
# 1. Keep only even numbers
numbers = [4, 7, 10, 13, 18, 21]
even_numbers = filter(lambda number:number if number %2==0 else "",numbers)
print(list(even_numbers))

# 2. Keep only passing grades
grades = [100, 55, 70, 40, 88, 59]
grade_above_60 = filter(lambda grade:grade if grade >= 60 else "",grades)
print(list(grade_above_60))

# 3. Keep only short words
words = ["dog", "elephant", "cat", "computer", "sun"]
words_with_3_letters = filter(lambda word:word if len(word)<=3 else "",words)
print(list(words_with_3_letters))

# 4. Keep only names that start with A
names = ["Adam", "Dana", "Amit", "Noa", "Alon"]
names_that_start_with_A = filter(lambda name:name if name[0] == "A" else "",names)
print(list(names_that_start_with_A))

# 5. Keep only positive numbers
numbers = [-5, 3, 0, 12, -2, 8]
numbers_bigger_than_0 = filter(lambda num:num if num > 0 else "",numbers)
print(list(numbers_bigger_than_0))

# 6. Keep only products cheaper than 50
products = [
    {"name": "Book", "price": 40},
    {"name": "Bag", "price": 120},
    {"name": "Pen", "price": 5},
    {"name": "Shirt", "price": 60}]
product_cost_less_than_50 = filter(lambda product:product if product["price"]<50 else "",products)
print(list(product_cost_less_than_50))

# 7. Keep only active users
users = [
    {"name": "Dana", "active": True},
    {"name": "Ron", "active": False},
    {"name": "Maya", "active": True},
    {"name": "Gil", "active": False}]
active_users = filter(lambda user:user if user["active"]==True else "",users)
print(list(active_users))
