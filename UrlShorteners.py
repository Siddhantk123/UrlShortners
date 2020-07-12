import pyshorteners

link= input("Please enter the link to be shortened\n")

#creating the object of the class
shortener= pyshorteners.Shortener()

x=shortener.tinyurl.short(link)

print(x)
