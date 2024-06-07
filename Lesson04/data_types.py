# String data type

#literal assignment
first = "Ayodya"
last = "Banuka"

# print (type(first))
# print(type(first) == str)
# print(isinstance(first,str))

#constructor function
# pizza = str("pepperoni")
# print (type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza,str))

#concaternation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#Casting a number to string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)


#Multiple lines
multiline = '''
Hey,How are you?                                            

I was just checking in.     
                                   All good?

'''
print(multiline)

#Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#String methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good","ok"))
print(multiline)

print(len(multiline))
multiline += "                                          "
multiline = "                                    " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print(" ")

#build a menu
title = "menu".upper()
print(title.center(20,"="))
print("Coffee".ljust(16,".")+"$1".rjust(4))
print("Muffin".ljust(16,".")+"$2".rjust(4))
print("CheeseCake".ljust(16,".")+"$4".rjust(4))

print("")

#String index value
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

#Some methods return boolean data
print(first.startswith("A"))
print(first.endswith("Z"))

#Boolean Data type
myValue = False
x= bool(False)
print(type(x))
print(isinstance(myValue,bool)) 