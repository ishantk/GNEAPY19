class Counter:

    def __init__(self):
        self.count = 1

    def incrementCount(self):
        self.count = self.count + 1

    def showCount(self):
        print("count is:",self.count)

c1 = Counter()
c2 = Counter()
c3 = c1

c1.incrementCount()
c2.incrementCount()
c3.incrementCount()

c1.incrementCount()
c3.incrementCount()

c1.showCount() # count is: ?
c2.showCount() # count is: ?
c3.showCount() # count is: ?