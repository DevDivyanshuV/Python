# calculator
    # Use of assignments and elif function


operators=input("Enter the operator (+ - / * **): ")
numc1=float(input("Enter the first number: "))
numc2=float(input("Enter the second number: "))

if operators =="+":
    result=numc1+numc2
elif operators =="-":
    result=numc1-numc2
elif operators =="/":
    result=numc1/numc2
elif operators =="*":
    result=numc1*numc2
elif operators =="**":
    result=numc1**numc2
elif operators not in ["+","-","/","*","**"]:
    result=f"Check the operator again. '{operators}' is not valid"


print(f"result is = {result}")