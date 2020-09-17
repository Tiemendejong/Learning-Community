response = input(100) #principal amount
p = float(response)

responseR = input(5) #Nominal Interest rate
r = float(responseR)

responseN = input(3) #number of times interest is compounded
n = float(responseN)

responseT = input(10) #amount of years
t = float(responseT)

print("the present value is", (p * (1+r/n) ** (n*t)))


