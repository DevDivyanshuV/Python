    # Use of assignments and elif function
# calculator

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

# Bill Calculator

amount=float(input("Enter the shopping amount: "))
discount=0
delivery=50

if amount<0:
    print("invalid value")
elif amount<1000:
    pass
elif amount<5000:
    discount=0.10
    
elif amount<10000:
    discount=0.20
   
elif 10000<=amount:
    discount=0.30
    delivery=0
else:
    print("Invalid input")

bill=amount*(1-discount)+delivery
print(f"Thanks for shopping\nYour bill amount is Rs. {round(bill,2)} after {discount*100}% discount.")