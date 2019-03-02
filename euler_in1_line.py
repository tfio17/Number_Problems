#
#
#
## Tom
#
## Using list comprehensions to do euler in 1 line for n=10!

print([((sum(x for x in range(1,11)))**2) - (sum(x**2 for x in range(1,11)))])
