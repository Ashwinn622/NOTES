# '''what the function can take in as input is known as the function parameter
# what we can pass in the function or the inputs are known as parameters
# when we actually use the function and pass in values are known as arguments'''

# # print("Hello \"Friend\"")#         #used when you need double quotes under double quote
# """name=str(input("Enter your name: \n"))
# print(f"hello, {name}")"""  #the 'f' in the start lets python know that "{Name}" 
#                         #is a "format string" or "fstring" 
#                         # hence it replaces the string with user input value

# #STRINGS(str)

# name=str(input("Enter your name: \n"))
# name=name.strip() ##this line removes any thing thats inside the brackets from the 
#                   ##user input which is saved in the variable "name"
#                         ##here which is blank spaces
# name=name.capitalize() #capitalize the first letter of user's name
# name=name.title()#capitalizes 1st letter of every word
# name=name.strip().title() #by this method we can write both the commands together
# print(f"hello, {name}")

# #the strip and title can also be used in the very first line when we 
# #declare the variable for a shorter code like
# name2=str(input("Enter your name:\n")).strip().title()
# print(f"Hello, {name2}")

# #The strip function only strips from the left and the right of the text and it can be used
# # as lstrip or rstrip if any one is needed

# #spliting the string into first name and last name
# name3=str(input("Enter your name:\n")).strip().title()
# first,last=name3.split(" ") #the blank space in inverted comma's tell python to 
#                               #split the string wherever there is a blank space and assign 
#                               #it to diffrent variables (here "first" and "last")
# print(f"Hello, {first}") #we can assign which string value to print (here the first name)


# #FLOAT(float)
# x=float(input("What's x?\n"))
# y=float(input("What's y?\n"))
# z=round(x+y) #The round function is used to round off the final value 
# print(z)
# print(f"{z:,}") #this funtion helps us to add comma's in the final value if it is big 
#                   #which increases the output readablity

# #rounding off to certain decimal values
# #1)
# x=float(input("What's x?\n"))
# y=float(input("What's y?\n"))
# z=round(x/y,2) #The round function is used to round off the final value 
#                   #Here the 2 after the operator tells the function to 
#                   #round off the value to 2 decimal places
# print(z)

# x=float(input("Enter the value of x \n"))
# y=float(input("Enter the value of y \n"))
# z=(x/y)
# print(f"{z:.2f}") #by this method we can round off the value using format string


#how to use match and case statements
name=input("Enter your name:")
match name:
    case "Harry"|"Hermione"|"Ron": #we can use | as or for multiple names
        print("Garud dwar")
    case "Draco"|"Snape":
        print("naag shakti")
    case _:                         #this "_:" acts like the else statement
        print("chalbe mote")

