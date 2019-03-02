#
#
#
## Tom
#
## quadratic equation
# Zelle 223

import math


# This script is meant to mimic the quadratic equation
# and find all real roots from the coefficients
def main():
    print("This program finds the real solutions to the quadratic \n")

    a = float(input("Enter Coefficient a:  "))
    b = float(input("Enter Coefficient b:  "))
    c = float(input("Enter Coefficient c:  "))

    discrim = b*b - 4*a*c
    if discrim < 0:
        print("\n The equation has no real roots.")
    elif discrim == 0:
        root = -b / (2*a)
        print("\n There is a double root at ", root)
    else:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2*a)
        root2 = (-b - discRoot) / (2*a)
        print("\n The roots are: ", root1, root2 )

main()
