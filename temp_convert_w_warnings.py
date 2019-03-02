#
#
#
## Tom
#
## Unit 3 - temp conversion w/ warnings built in
# Zelle pg 212
 
# A program to convert Celsius temps to Fahrenheit
# This version issues warnings for heat and cold

def main():
    celsius = float(input("What is the Celsius Temperature?  "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is ", fahrenheit, "degrees Fahrenheit.")

    # Print warnings for extreme temps
    if fahrenheit > 90:
        print("It's really hot out there, be careful!")
    if fahrenheit < 30:
        print("Brrrrr. It's chilly out there!")

main()
