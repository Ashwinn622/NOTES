# # # a=float(input("Enter an number:\n"))
# # # b=float(input("Enter another number:\n"))
# # # if(a>b):
# # #     print(b*b,a*a*a)
# # # elif(b>a):
# # #     print(a*a*a,b*b)
# # # else:
# # #     print("both are equal")

# # '''2). write a program to enter a number. if the number is positive even,
# #     display three succeeding even numbers, if the number is negative odd
# #     display three preceding odd numbers otherwise
# #     display the message "number is neither a positive even nor a negative odd".'''

# # a=int(input("Enter a number:"))
# # if(a>0 and a%2==0):
# #     print("Three succeeding even numbers are: \n",a+2,a+4,a+6)
# # elif(a<0 and a%2!=0):
# #     print("Three preceding odd numbers are: \n",a-2,a-4,a-6)
# # else:
# #     print("number is neither a positive even nor a negative odd")

# """3). write a program to enter three numbers and a choice
# find and display the sum of the numbers if the choice is 1
# and product of the number if given choice is 2
# the program must display the message "wrong choice" if user enters a letter
# or any other number than 1 or 2"""

# a=float(input("Enter the first number:\n"))
# b=float(input("Enter the second number:\n"))
# c=float(input("Enter the third number:\n"))
# d=list(input("Enter choice 1 for sum and 2 for product:\n"))

# if(d==1):
#     print("sum of the numbers is:",a+b+c)
# elif(d==2):
#     print("product of the numbers is:",a*b*c)
# else:
#     print("wrong choice")

p=float(input("Enter the marks obtained in physics:\n"))
c=float(input("Enter the marks obtained in chemistry:\n"))
b=float(input("Enter the marks obtained in biology:\n"))
grade=(p+c+b)/3
g=(grade/100)*100
print("Percentage of the student is:",g,"%")
if(g>=80):
    print("Distinction")
elif(80>g>=60):
    print("First division")
elif(60>g>=45):
    print("Second Division")
elif(45>g>=40):
    print("Pass")
else:
    print("Promotion not granted")







