# input functions

# basically takes input from the user and return as string 

# name= input("Enter your name: ")

# # print("Hello, " + name + "") #variable name in not in quotes

# print(f"Hello {name}") #format string 
# #also you can do this by using format function

# a = input()


# print(f"Hello{a}")

# print(a+a) #proof that it takes input as string and not as integer or float by default 

# # 11
# # Hello11
# # 1111
# # PS C:\Users\admin\Desktop\nandan's code\pythontutorial> 



# # but for addition we need to convert it into integer or float

# print(int(a)+int(a)) #this will convert the string into integer and then add it


age=input("Enter your age (in years)= ") 
print(f"so your are {int(age)+1} next year")

# Enter your age (in years)= 18
# so your are 19 next year


# to add two numbers 
x=input("Enter first number: ")
y=input("Enter second number:")

print(f"Their sum is {int(x)+int(y)}")  
print("Thanks for using this program")
