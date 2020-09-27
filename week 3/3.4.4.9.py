response1 = input("Length any side")
response2 = input("Length any side")
response3 = input("Length any side")

x1 = float(response1)
x2 = float(response2)
x3 = float(response3)


a = max(x1, x2, x3)
b = min(x1, x2, x3)
c = [x1, x2, x3]
c.sort()
d = (c[int(len(c)/2)])
print(a, b, d)
if a == (b ** 2 + d ** 2) ** 0.5:
    print(True)
else:
    print(False)
