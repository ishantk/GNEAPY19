class Parent:

    def __init__(self, fname, lname, money):
        self.fname = fname
        self.lname = lname
        self.money = money


    def showDetails(self):
        print("** Full Name:", self.fname, self.lname)
        print("** Money:",self.money)


class Child(Parent): # IS-A Relationship | Inheritance Relationship | Generalization

    # OVER-RIDING
    def showDetails(self):
        print(">> Full Name:", self.fname, self.lname)

# Rule Of Inheritance
# If Parent has properties which are not available with child, child can access them

"""
pRef = Parent("John", "Watson", 100000)
pRef.showParentDetails()


print("Dictionary of Object:",pRef.__dict__)
print("Dictionary of Class:",Parent.__dict__)

"""

print("Dictionary of Parent Class:",Parent.__dict__)
print("Dictionary of Child Class:",Child.__dict__)


cRef = Child("John", "Watson", 200000)
cRef.showDetails()


"""

    1. Single Level
    
    class CA:
        pass
        
    class CB(CA):
        pass
        
    2. Multi Level        
    
    class CA:
        pass
        
    class CB(CA):
        pass
        
    class CC(CB):
        pass 
        
    3. Multiple Level        
    
    class CA:
        pass
        
    class CB:
        pass
        
    class CC(CA,CB):
        pass    
        
    4. Hierarchy
    class CA:
        pass
        
    class CB(CA):
        pass
        
    class CC(CA):
        pass                

    5. Hybrid
        Any Combination of above
"""

# Code : All the above 5 Relationships in Lab