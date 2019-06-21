# cProgram is a String in Python
# Hello World Program
cProgram = """
#include<stdio.h>
int main(){
    printf("Hello World");
    return 0;
}
"""

pyProgram = """
print("Hello World")
"""
"""
print("Enter 1 for C++ Program")
print("Enter 2 for Java Program")
choice = int(input("Which Programming Language?"))

if choice == 1:
"""

# Using Voice Recognition we may see in the end

# print(cProgram)

# file = open("/Users/ishantkumar/Downloads/MyApp.c", "w")
# file.write(cProgram)
file = open("/Users/ishantkumar/Downloads/MyApp.py", "w")
file.write(pyProgram)
file.close()    # Releasing Memory Resources
print(">> Data Written in File")


"""
    Source Code Generator :)
    1. Take Input from User what Hello World Program he wants to develop
    2. Generate corresponding Hello World Program File anywhere in your computer
    3. C#, C++, Java, Python, Go, Ruby, Dart, Kotlin, Scala  
"""

