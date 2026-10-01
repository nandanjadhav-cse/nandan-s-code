# ways to insert the variables in the string 


#FORMATTED  STRINGS 

#1]  % OPERATOR  like %d, %s  same as that of c language    
# name ="NANDAN"
# age = 18
# print("MY NAME IS %s and MY AGE IS %d"%(name,age )) 



# # str.format method ##advance one 

# print("MY NAME IS {} AND MY AGE IS{}.".format (name,age))

# print("MY NAME IS {1} AND MY AGE IS {0}.".format (name,age))


# print("MY NAME IS {name} AND MY AGE IS {age}.".format (name="nandan",age=18))


# print("MY NAME IS {1} AND MY AGE IS {0}.".format (name="nandan",age=18))

##will give error because we are using positional arguments 


#  string operators in python 

A="nandan"
B="jadhav"

print(A+B)

print(A*2)  # WILL PRINT NANDANNANDNAN 

# print(A*B)   WILL GIVE ERROR AS WE CANNOT MULTIPLY TWO STRINGS    

print(A[0])  # will print first char of the string that is "n"

print (A[0:4])  #will print first 4 char of the string  that is "nand"

if "n" not in A:
    print ("yes n is present in A")
else:
    print("no n is not present in A")



# raw string 
print ("this is normal string \nthis will be printed in new line\n    \n \n   \n                    ")
print (r"this is raw string \nthis will not be printed in new line ")    


# STRING INDEXING

name ="nandan"

print(A[0])   
print(A[1])   
print(A[2])   
print(A[3])   
print(A[4])   
print(A[5])   

# *arg 

def my_function(*args):
    for arg in args:
        for char in arg:
            print(char)

x =input ("Enter the string :")

my_function(x)



# STRING SLICING  

my_name = "nandan jadhav"
print(my_name [0:6])
print(my_name [0:9])

print(my_name [0:6:2])  # will print every second char from 0 to 6