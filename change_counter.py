#
#
#
## Tom
#
## change counter
# Zelle 58

# This script will sum the value of a user's change

def main():
    print("Change Counter")
    print()
    print("Please enter the value of each coin type:")
    q = int(input("Quarters:  "))
    d = int(input("Dimes:  "))
    n = int(input("Nickels:  "))
    p = int(input("Pennies:  "))

    total = .25*q + .1*d + .05*n + .01*p
    print()
    print("The total value of your change is:  ", "$", round(total, 2))
    
main()    
    
