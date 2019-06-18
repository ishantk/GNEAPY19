# List of Lists
data = [
            ["shoe", "shirt", "jeans"], # 0 index
            [1000, 800, 1200]           # 1 index
       ]

print(len(data))
print(data[0])      # List at 0
print(data[1][2])   # 1st List's 2nd index -> 1200

print("data[1][0:2] is:",data[1][0:2])
# add more lists in data and try below statements:
print("data[0:1][0:2] is:",data[0:1][0:2])