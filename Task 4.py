import random 

Newfile = open("Newfile.txt", "w")# the new file is created and opened
for i in range(100):
    number=str(random.randint(0,100))# randint method is used to generate a random integer between 0 and 100.
    Newfile.write(number)# the random number is then written in the new file.
    Newfile.write("\n")
    Newfile.close
