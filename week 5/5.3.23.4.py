this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))

# we can see that at first the lists are equal to each other, however when we type that = this the lists suddenly are not equal to each other anymore. I do not know the reason for this. 