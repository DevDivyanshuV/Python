
# Grade calculation
    # Using if function.

marks=float(input("Enter your marks: "))
if 100>=marks>=90:
    grade="A"
if 90>marks>=80:
    grade="B"
if 80>marks>=70:
    grade="C"
if 0<=marks<70:
    grade="F"
if marks>100 or marks<0:
    grade="Invalid input."

print(f"Grade = {grade} ")