#
#
## Tom
#
## euler_lib is a library containing defined functions
##    for the sum or squares and square of sums


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
