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