names = "John, Jennie, Jim, Jack, Joe"
print(names[0]) # J

# idx = names.index("h")
idx = names.index("Jennie")
print(idx) #


# names = names.replace("J", "K")
# print(names)

data = names.split(",")
print(data)
print(type(data))

quote = "Search the candle rather than cursing the darkness"
data = quote.split(" ")
print(data)
print(len(data))
