S = {10, 20, 30, 'A', 'B', "John"}
S.add("Jennie")
S.add(10)

print(S)

for data in S:
    print(data)

print()

print("S Before:",S)

S.remove(20)
print("S After Remove:",S)

S.pop()
print("S After Pop:",S)


S.clear()
print(S)