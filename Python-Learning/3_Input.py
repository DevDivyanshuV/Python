# input
# a function that prompts the user to enter data. Returns the entered data as a string.

namei=input("What's your name? : ")
agei=int(input("Your age : "))
agei = agei+1                                              ## it will not work if we add directly because input returns data as string.
print(f"Hello {namei}!\nNice to see as a {agei} yr old.")
