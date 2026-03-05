# key : value, key1 : value

stocks = {
    "AAPL" : "Tech",
    "XOM" : "Energy",
    "RACE" : "Automobile",
}

print(stocks)

for key in stocks:
    print(key, stocks[key])

stocks = {
    "AAPL" : {"type": "Tech", "name": "Apple Inc."},
    "XOM" : "Energy",
    "RACE" : "Automobile",
}

for key in stocks:
    print(key, stocks[key])

print("-------------")
print(stocks["AAPL"]["name"])