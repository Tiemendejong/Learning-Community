response = input("initial amount") #principal amount
p = float(response)

responseR = input("interest rate") #Nominal Interest rate
r = float(responseR)

responseN = input("Number of times p/y interest is compunded") #number of times interest is compounded
n = float(responseN)

responseT = input("amount of years") #amount of years
t = float(responseT)

print("the present value is:", (p * (1+r/n) ** (n*t)))


