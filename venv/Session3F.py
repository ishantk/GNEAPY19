# *args -> Variable Arguments
# *args -> args can be any name of your choice
# *args -> is a tuple :)
def fun(*args):
    print(args)
    print(type(args))
    print()


fun(10, 20, 30)
fun(10, 20, 30, 40, 50)
fun("John", "Jennie", "Jim")

# 1. in the same function fun calculate sum of all the numbers
# 2. find maximum and minimum number
# 3. Sorth the elements in ascending order (future assignment)
