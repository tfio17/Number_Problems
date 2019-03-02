#
#
#
## Tom
#
## File I/O Unit 3
#

# Choose the file to read
infile = 'SmallE22.txt'

# open/read/close
f = open(infile, 'r')
data = f.read()
f.close()

# Check length
# print(len(data))

# clean the data
data = data.replace('"','')
data = data.split(',')
#print(data)

c = 0
for i in data:
    c += 1
    if i == 'SARA':
        print(i,c)
print(c)










