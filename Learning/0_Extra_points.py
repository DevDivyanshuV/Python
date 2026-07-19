
# 1 assignment and string are very uniquely defined by python.

print(" * " * 5)               #-- it basically multiplies" * " (a string) 5 times 
print("**"* 0)                 
print("**\n"*3)
# print("Hi"/3)                 -- gives an error, because there's no meaning of it
print(3*"Hi ")
print("A" + "B" * 3)
print("A"+"B")

# 2 Concept of id.
    # Id refers to the value not to variable.
    # same value have same id.

i1="Pal"
i2="Ram"

d1="Shiv"
d2="Shiv"
d3="shiv"

    # different values
print(id(i1))
print(id(i2))
    # same values, d3 is different
print(id(d1))
print(id(d2))
print(id(d3))


# 2 understanding object's change

list1=[1,2,3]
xl=list1
yl=xl.append(4)
print(id(list1))
print(id(xl))
print(id(yl))



a = [1, 2]
b = a
c = a
a.append(3)
b = [10, 20]
c.append(4)

    # a=b=c=[1,2]. Append add 3 in the list and make it [1,2,3]. b= refers to new object now that is [10,20] then again append 4 via c in the list and it makes a=c=[1,2,3,4]
    # it also make me understand about mutability

print(a)
print(b)
print(c)

# 4 