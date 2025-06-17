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
#declare the variable for a shorter code like this, but this reduces code readability
name2=str(input("Enter your name:\n")).strip().title()
print(f"Hello, {name2}")

#The strip function only strips from the left and the right of the text and it can be used
# as lstrip or rstrip if any one is needed
