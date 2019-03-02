# This is a comment
#
# Author Lars
#
# Playing w pickle

import pickle

# create a list
myList = [ 3,2,4,5,6,7,8,54,2,4,56,12,'four',23,23.4,56,22.4,55,'six']
print("My list before Pickling")
print(myList)

# save my list to a pickle file
oFile = "picklefile.dat"
# open the file for writing
myFile = open(oFile,'wb') 

# this writes the object a to the
# file named 'testfile'
pickle.dump(myList,myFile)
# here we close the fileObject
myFile.close()

# We have saved the List and maintained the structure
# Now we test
# we open the file for reading
fileObject = open(oFile,'rb')  
# load the object from the file into var b
b = pickle.load(fileObject)
print("Back from pickling:")
print(b)


    


