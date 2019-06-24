print(">> App Started")

numbers = [10, 20, 30, 40, 50]
a = 10
b = 0
c = 0

try:
    print("numbers[4] is:",numbers[4])
    c = a // b
    # print("This is Awesome")
# except IndexError as iRef:
#     print("Some Error Occurred: ",iRef)
# except ZeroDivisionError as zRef:
#     print("Some Error Occurred: ",zRef)
except Exception as eRef:
    print("Some Error Occurred: ",eRef)
finally:
    print("This is Awesome")

# c = a//b

print("c is:",c)


print(">> App Finished")