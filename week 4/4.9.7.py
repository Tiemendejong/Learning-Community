
def sum_to(n):
    g = 0
    for i in range(n+1):
        g += i
    return g

sum = int(input("What value to sum?"))
print(sum_to(sum))
