#
#
## Tom
#
## read in random numbers and determine
#    how many palindromes there are
#

import random_palendromes

# read in data

ifile = 'rand.txt'
f = open(ifile,'r')
data = f.read()
f.close()

# clean data

data = data.replace('\n','\t') # replace all new lines with tabs

data = data.split('\t')

# check for palindromes
pallist = []
for i in data:
    if random_palendromes.isPal(i) == True:
        pallist.append(i)

print(pallist)
print("There were ", len(pallist), "palendromes.")
