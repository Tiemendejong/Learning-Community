punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

text = "This is my piece of text, ?//because I do not have any ideas for ///an 'inspirational text and therefore I will write something myself. I think this exercise is quite difult and therefore I try to ocus more on ///the code instead of this text"

no_punct = ""
for char in text:
   if char not in punctuations:
       no_punct = no_punct + char
res = len(no_punct.split())
aaa = input("which letter?")
print("The amount of words are:", str(res), "and the letter", aaa, "showes up", text.count(aaa), "times")
a = (text.count(aaa)/len(text)*100)
b = "{:.2f}".format(a)
print("The percentage of occurence is:", b)
