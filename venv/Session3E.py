#Pass by Reference
def squareOfNumbers(numbers):

    print("numbers is:",numbers, hex(id(numbers)))

    for i in range(0,len(numbers)):
        # print(numbers[i])
        numbers[i] = numbers[i] * numbers[i]


n = [1, 2, 3, 4, 5]
print("n is:",n, hex(id(n)))

squareOfNumbers(n)

print(n) # ?