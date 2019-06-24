import datetime as dt

class Counter:

    def __init__(self):
        self.count = 1

    def incrementCount(self):
        self.count = self.count + 1

    def showCount(self):
        print("count is:",self.count)


def hello(name):
    print("Hello",name)
    print("Its: ", dt.datetime.today())

def bye(name):
    print("Bye",name)
    print("Its: ", dt.datetime.today())