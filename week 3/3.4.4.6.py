response = input("What is your exam mark?")
a = float(response)
if a >= 75:
    print("Grade First")
if 75 > a >= 70:
    print("Grade Upper Second")
if 70 > a >= 60:
    print("Grade Second")
if 60 > a >= 50:
    print("Grade Third")
if 50 > a >= 45:
    print("Grade F1 Supp")
if 45 > a >= 40:
    print("Grade F2")
if a < 40:
    print("Grade F3")
