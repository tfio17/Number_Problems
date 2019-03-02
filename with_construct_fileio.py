#
#
#
## Tom
#
## With Construct Unit 3
#

with open("numbers.dat", 'r') as f:
    for line in f:
        print(line)


#Read and write a file !!!
of = open("outnums.dat", 'w')
with open("numbers.dat", 'r') as f:
    for line in f:
        print(line)
        of.write(str(line) + '\n')

of.close()
