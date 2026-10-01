#data type 
print("Hi Shubham")

# suppose i do this 
a="1"

b="1"

sum =a+b

print(sum)

c="1"
d="3"


sum=c+d 


print(sum)

# NOTICE that the putting values in codes gives different result 

# so to check the data type we do this 

print(type(c)) #checking data types

# PS C:\Users\admin\Desktop\nandan's code\pythontutorial> & C:\Users\admin\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/admin/Desktop/nandan's code/pythontutorial/chapter 2/Data types"
# Hi Shubham
# 11
# 13
# <class 'str'>
# PS C:\Users\admin\Desktop\nandan's code\pythontutorial> 


# you will get this kind of output 

a1=26
a2=1.5
a3=complex(3,5)
a4="nandan"
a5=[1,2,3,5]
a6=(1,2,3,4)
a7={'name':"madhav",'age':26} 


print(type(a1))
print(type(a2))
print(type(a3))

print(type(a4))
print(type(a5))
print(type(a6))
print(type(a7))


# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'complex'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>

# this is how we can check the data types of different variables in python


# this is hoew we check boolean data types in python

a8= True
a9= False   
print(type(a8))
print(type(a9))



# this is how we check the data type of None


a10= None
print(type(a10))    


# <class 'NoneType'>

# this is how we check the data type of bytes in python


a11= b"nandan"
print(type(a11))    




