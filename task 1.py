
sourceFile = 'measles.txt' # this is the source file. 
print("Enter the Name of Output File: ")
newFile = input()# the userinput is the name of the new file to be created.

fileedit = open(sourceFile, "r")# the source file is opened on read mode and the lines are read. 
texts = fileedit.readlines()
fileedit.close()

fileedit = open(newFile, "w")# the new file is opened in write mode and the contents of the source file are written into it. 
for s in texts:
    fileedit.write(s)
fileedit.close()

print("file copied!")#message to show the user that the file has been copied. 
