response = input("What is the current time?")
a = float(response)

responseB = input("How long do you want to sleep?")
b = float(responseB)
c = b % 24
print((a + c) % 24)

#I think it works well!

