def area(r):
    return lambda a:3.14*r*r
circle=area(2)
print("Area of circle = ",circle(1))
