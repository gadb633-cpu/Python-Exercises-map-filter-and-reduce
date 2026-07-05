# part 1
# 1. Add 10 to each number
numbers = [3, 7, 10, 15]
numbers_bigger_by_10 = map(lambda num:num+10,numbers)
print(list(numbers_bigger_by_10))

# 2. Turn prices into prices with tax
prices = [100, 50, 200, 80]
prices_with_17_present = map(lambda num:num + num*0.17,prices)
print(list(prices_with_17_present))