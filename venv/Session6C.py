class Student:

    # Constructor : When object is created in memory
    def __init__(self, name):
        self.name = name
        print(">> init executed - Student Object Created")

    # Destructor : When Object is deleted from Memory
    def __del__(self):
        print(">> del executed - Student Object Deleted:",self.name)

s1 = Student("John")
s2 = Student("Fionna")

for i in range(1, 10):
    print(i)
    if i == 5:
        del s1 # You can explicitly delete the object


