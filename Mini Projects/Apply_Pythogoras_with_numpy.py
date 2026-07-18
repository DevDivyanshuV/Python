import numpy as np

print(np.pi)                                                # value of pi, just to cross verify

a=float(input("Enter perpendicular of triangle (in cm): "))
b=float(input("Enter base of triangle (in cm): "))
c=np.sqrt(pow(a,2)+b**2)                                    # using 2 different approach

print(f"Hypotaneous of the triangle is {round(c,2)} cm")

