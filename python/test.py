'''what the function can take in as input is known as the function parameter
what we can pass in the function or the inputs are known as parameters
when we actually use the function and pass in values are known as arguments'''

# print("Hello \"Friend\"")#         #used when you need double quotes under double quote
"""name=str(input("Enter your name: \n"))
print(f"hello, {name}")"""  #the 'f' in the start lets python know that "{Name}" 
                        #is a "format string" or "fstring" 
                        # hence it replaces the string with user input value

#STRINGS

name=str(input("Enter your name: \n"))
name=name.strip() ##this line removes any thing thats inside the brackets from the 
                  ##user input which is saved in the variable "name"
                        ##here which is blank spaces
name=name.capitalize() #capitalize the first letter of user's name
name=name.title()#capitalizes 1st letter of every word
name=name.strip().title() #by this method we can write both the commands together
print(f"hello, {name}")

#the strip and title can also be used in the very first line when we 
#declare the variable for a shorter code like
name2=str(input("Enter your name:\n")).strip().title()
print(f"Hello, {name2}")
