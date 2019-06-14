# Pass By Value :)
def squareOfNum(num):
    print("HashCode of num", hex(id(num)))
    num = num * num
    print("num is:",num)
    print("HashCode of num now is:", hex(id(num)))

n = 10
print("HashCode of n",hex(id(n)))
squareOfNum(n)
print("n is:",n)