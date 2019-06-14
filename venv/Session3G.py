# Keyword Arguments -> **kwargs
# **kwargs -> Dictionary :)

def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print()


fun(a=10, b=20, c=30)
fun(name="john", age=30, email="john@example.com")