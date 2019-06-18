name = "John Watson"
print(len(name)) # 11

print(max(name)) # t
print(min(name)) # space

print(name[1])   # o
print(name[len(name)-1]) # n

print(name[-1])

print(name[1:3]) # oh

print(name*2)

print(name+" California")
print(name) # Concatenation will not modify old String

email = "john@example.com"
password = "pass123"

if "@" in email and "." in email:
    print("A Valid Email")
else:
    print("Its an Invalid Email")

if len(password) > 6:
    print("A Valid Password Length")
else:
    print("Please create password with length more than 6")