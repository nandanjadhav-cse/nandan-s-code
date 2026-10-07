# modyfying lists 

# initial list 

fruits_list=["apple","banana","cherry"]

# add an element
fruits_list.append("mango")


# changing an element 
fruits_list[1]=("blue_berry")

print(fruits_list)

# removing an element
fruits_list.remove("cherry")
print("\n    \n  \n   \n-----------")
print (fruits_list)


# ['apple', 'blue_berry', 'mango']   final  output 


# extend the string 
more_fruits =["papaya","orange",""]
fruits_list.extend(more_fruits)
print(fruits_list)

print("\n \n-----------")
# insert modification 

fruits_list.insert(2,"nandan")

print(fruits_list)

# ['apple', 'blue_berry', 'nandan', 'mango', 'papaya', 'orange', '']

print("\n \n ---------")
# finding index 

fruits_list.index("nandan")




print("\n \n ---------")


# remove modification in lists

fruits=["apple","banana","cherry","banana"]

fruits.remove("banana")
print(fruits)
print("\n \n ---------")


# removes the first occurence of a specified positiion here banana

print(fruits)
# insert an element 
fruits.insert(1,"grapes")


# you can insert an element at specified index using insert 

print(fruits)


print("\n \n ---------")


# clear 

fruits.clear()

print(fruits)

print("\n \n ---------")



# finding index 
fruits_list.append("banana")

print(fruits_list)
print(fruits_list.index("banana"))

# output will be 7

print("\n \n ---------")


# reverse the string / but also done by slicing 

fruits_list.reverse()
# will be reversed permanently 


print(fruits_list)


print("\n \n ---------")

# by slicing 
fruits_1=["apple","mango","grapes"]

print(fruits_1[::-1])
# ['grapes', 'mango', 'apple'] output is reversed


print ("BUT FRUIT_1 DOES NOT CHANGES PERMANENTLY \n THIS THE DIFFERENCE BETWEEN REVERSE AND SLICING  ")


print(fruits_1)
print ("here value  of the list remains same")
print("\n \n ---------")


# sorting lists 

# default order is ascending 
fruits_1.sort() 
print(fruits_1)


# ['apple', 'grapes', 'mango']

print("\n \n ---------")


numbers=["2","1","a","A","b",""]

(numbers.sort())

print(numbers)

# 

print("\n \n ---------")

num_2=["A","a",""]
 
num_2.sort()
print(num_2)

#same output is obtained 
print("\n \n ---------")

# for descending order 

fruits_1.sort(reverse=True)

print (fruits_1)

# ['mango', 'grapes', 'apple']

print("\n \n ---------")



# sorting on the basis of the length of the words

fruits_1.sort(key=len)

print(fruits_1)


print("\n \n ---------")


# join lists 

print(fruits_list)


print(fruits_1)

for x in fruits_1:
    fruits_list.append(x)

# output 

# ['banana', '', 'orange', 'papaya', 'mango', 'nandan', 'blue_berry', 'apple']
# ['mango', 'apple', 'grapes']


print("\n \n ---------")




# LISTS COMPREHENSIONS 

#CREATE LISTS  USING FUNCTIONS 

print(" 1] square numbers list")   


b=int(input("upto no:"))

if b :

    x=square_list=[x**2 for x in range(1,b)]

else :
    x=square_list=[x**2 for x in range(1,10)]

print(x)
print("\n \n ---------")


# filtering even numbers 

b=int(input("upto:"))

new_list1=[x for x in range(1,b) if x%2==0]

print(new_list1)


# [2, 4, 6, 8, 10, 12, 14, 16, 18]  output

print("\n \n ---------")



# using string methods on list

# print(new_list1.upper())  wrong  

new_list=[y.upper() for y in fruits_list ]

print(new_list)


print("\n \n ---------")

#  flattening a nested list using list comp

# nested_list=[]


def function_(a):
    for b in range(1,10):
        fun_=[a,b]


nested_list =[function_(a) for a in range(1,10)]

print(nested_list)


print("\n \n ---------")


# iterating over lists
print(fruits_1)



print("\n \n ---------")



# using for loop
for fruits in fruits_1:
    print(fruits)

print("\n \n ---------")



for items in fruits_1:
    print(items)



    # using while loop


print("\n \n ---------")

i=0
while i<len(fruits_1):
    print(fruits_1[i])
    i+=1




