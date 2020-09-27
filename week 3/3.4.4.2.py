response = input("What is the starting day number?")
responseA = input("What is the length of your stay?")
f = float(response)


if f > 7:
     print("Wrong input: Starting day is not between 0 and 6")
     exit()

if f < 0:
     print("Wrong input: Starting day is not between 0 and 6")
     exit()


p = float(responseA)
days = p % 7
a = (f + p) % 7
if a == 1:
    print("sunday")
if a == 2:
    print("monday")
if a == 3:
    print("tuesday")
if a == 4:
    print("wednesday")
if a == 5:
    print("thursday")
if a == 6:
    print("friday")
if a == 0:
    print("saturday")


