#
#
# Tom
#
## Unit 3 Review video 4
#
#
## diff between sum of squares and square of sums
#
#

# Leaving the defined functions commented out
#    check euler_lib for definitions!!
'''
# Start with sum of the squares

def sumosq(n):
    sos = 0
    for i in range(1,n+1):
        sos = sos + i**2
    return(sos)

# Square of the sums

def sqofsum(n):
    sqos = 0
    for i in range(1,n+1):
        sqos = sqos + i
    return(sqos**2)
'''

# import euler_lib
import euler_lib

# find the difference
limit = int(input("What is the limit: "))
print("The diff is : ", euler_lib.sqofsum(limit)-euler_lib.sumosq(limit))
