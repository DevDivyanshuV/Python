
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


# 2 Bank Loan Case Study
    # Using nested if

# Step 1
# If age is below 21:
# Reject immediately.

# Step 2
# Otherwise ask for monthly salary.

# Salary ≥ ₹50,000
# Ask for credit score.
# Credit score ≥ 750 → Loan Approved
# Otherwise → Loan Under Review
# Salary < ₹50,000
# Loan Rejected

age=int(input("Enter your Age: "))
if age>21:
    salary=int(input("Enter your Monthly Salary: "))
    if salary>50000:
        cscore=int(input("Enter your Credit Score: "))
        if cscore>=750:
            print("Loan Approved")
        else:
            print("Loan under review")
    else:
        print("Loan Rejected")
else:
    print("Loan Rejected")   