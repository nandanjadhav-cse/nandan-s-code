#operators 
#are special symbols that are used on operands 



a=10
b=15


#comparision operators



# (printa<b) #it gives boolean value here true 

# print(a>b) # Here false 

# print(a==b)# Here false 

# print(a!=b) # true 

# # PS C:\Users\admin\Desktop\nandan's code\pythontutorial> & C:\Users\admin\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/admin/Desktop/nandan's code/pythontutorial/ch 1/chapter 5/operators"
# # True
# # False
# # False
# # True
# # PS C:\Users\admin\Desktop\nandan's code\pythontutorial> 



# # logical operatprs

# a=4 

# print(a>3 and a<10)

# print(a>3 or a<10)

# print (not (a>3 or a<10))

# # True
# # True
# # False


# # identity operators

A=[1,2,3]

B=[1,2,3]

print (A is B)  #gives false because both are different objects in memory


# A=(1,2,3)

# B=[1,2,3]

# print (A is B) gives false 

# Membership operators 

A=["apple","banana","grapes"]


print("apple" in  A ) #gives true because apple is present in A

print("mango" in  A ) #gives false because mango is not present in A

t1= (1,2,3,4,5)

print(1 in t1) #gives true because 1 is present in t1

#same for tupple and set 


# bitwise  operator 

a= 2 
b= 3  
print(a&b)


