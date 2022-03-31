import collections
import string
#this is the encode function which is chosen when the user selects 'e'. The function asks the user for a word and rotation number which is then added to the end of the string the user selected. 
def encode():
  String = string.ascii_lowercase
  Userinput = input("What word would you like to encode?: ").lower()
  Rotation = int(input("Enter a number for the rotation: "))
  RotateWord = String[Rotation:] + String[:Rotation]
#In this part of the code I use the maketrans method to create a mapping table of the string and the number of rotations. I then used the translate method to return the string with the characters replaced based on the mapping table created.
  encoding = str.maketrans(String,RotateWord)
  Output = Userinput.translate(encoding)
  print("Here is the encoded text :",Output)

#this is the decode function which is run when the user selects 'd'.
def decode():
    String = string.ascii_lowercase
    userinput = input("What word do you want to decode: ").lower()
    WordString = input("What word is in the string").lower()
    decoding= str.maketrans(String,userinput)
    output= userinput.translate(decoding)
    print(output)

# this is the wile loop for the userinput this loop allows the user to pick one of the 3 options and if the option is invalid it prompts the user to select a valid option.
while True:
    user_choice = input("choose from the options below: \n"

                            "Press 'e' to encode a string\n"

                            "Press 'd' to decode a string\n"

                            "Press 'q' to quit\n").lower()

#these if statements are used to direct the user to where they have selected. 
    if user_choice == "e":

      encode()

    elif user_choice == "d":

      decode()

    elif user_choice == "q":

      print("quitting\n")

      break


    else:

      print("Invalid input please select a Valid input!")
