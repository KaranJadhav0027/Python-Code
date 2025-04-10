try:
    a=5
    b=0
    print(a/b)
except TypeError:
    print("unsupported Operation")
except ZeroDivisionError:
    print("Division by zero are not allowed")
    print("out of try except blocks")
