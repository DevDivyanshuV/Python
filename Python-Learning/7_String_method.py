#13 string method

word=input("enter a string: ")


findsm=word.find("a")                       # finding index of character in the string

findbackward=word.rfind("e")                # finding index of character from backword in string

capitalizesm=word.capitalize()              # Making first word of every word upper case

uppercasesm=word.upper()                    # converting the all characters in upper case

lowercase=word.lower()                      # converting the all characters in upper case

anydigit=word.isdigit()                     # gives true if all characters are letter or false 

anychar=word.isalpha()                      # gives true if all characters are numeric or false

numofchar=word.count("e")                   # count number repeatation of character

replacechar=word.replace(" ","-")           # replacement


print(findsm)
print(findbackward)
print(capitalizesm)
print(uppercasesm)
print(lowercase)
print(anydigit)
print(anychar)
print(numofchar)
print(replacechar)
