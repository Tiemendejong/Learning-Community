response = input("How far is your destination in km?")
p = float(response)
a = 50  #speed of car
b = 20  #speed of biking
c = 5   #speed of walking
d = 4   #minutes for finding a parking spot
e = 2   #minutes to grab your bike

print("time it would take for you to arrive in minutes")
print("car:", ((p/a)*60)+d)
print("bike:", ((p/b)*60)+e)
print("walking:", (p/c)*60)
