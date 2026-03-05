#         0  , 1     , 2
prices = [103, 123.45, "154", 152]

print(prices, type(prices))

prices.append(100)
print(prices, type(prices))

for item in prices:
    print(item, type(item))

print("--------------")

print(prices[0])
print(prices[3])
print(prices[-1])

print(prices[2:-1])