#S10Q2B
def distancesum (x, y, n):
    sum = 0    
    for i in range(n):
        for j in range(i+1,n):
            sum += (abs(x[i] - x[j]) +
                        abs(y[i] - y[j]))
    return sum
x = [ -1, 1, 3, 2 ]
y = [ 5, 6, 5, 3 ]
n = len(x)
print(distancesum(x, y, n) )
