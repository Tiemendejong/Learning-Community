str = input("What word?")
stringlength = len(str)
slicedString = str[stringlength::-1]
print(slicedString)
a = "true"
b = "not true"
if str == slicedString:
    print(a)
else: print(b)
