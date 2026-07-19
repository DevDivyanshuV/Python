#7 if statement     --if else
age=float(input("Enter your age: "))
name=input("Enter your name: ")
if age>=20:
    print(f"Mr. {name} you're eligible for license")
elif age<0:
    print(f"Error in age.")
else:
    print(f"You're not eligible for License")
