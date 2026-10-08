# set operations

set_he=set ([1,2,3,4,5,6,7,8,9,0])   #USE SQUARE BRACKETS FOR ENTERING EACH ELEMENT
 
# addition of elements

set_he.add(1000)


print(set_he)


print("\n\ \n -----------------\n  \n ")


# SET METHODS

# SYMMETRIC DIFFERENCE


set_a={1,2,3}

set_b={3,4,5}

set_new=set_a.symmetric_difference(set_b)

# {1, 2} output for just difference 
print(set_new)
# {1, 2, 4, 5} tis is the output


print("\n\ \n -----------------\n \n ")



# list comprehension 
# set of square numbers from 1 to 10
new_set={x**2 for x in range(1,int(10**0.5))}


print (new_set)

# loop over loop method 

print("\n\ \n -----------------\n \n ")

new_set2={i for i in range(1,10) for n in range(1,10)  if i == n**2  }


print(new_set)

print("\n\ \n -----------------\n \n ")


# deflatten the sets

for i in new_set:
    print(i) 



print("\n\ \n -----------------\n \n ")

# by while loop 


# but we have to convert in it to list 

new_list =list (new_set)

i=0

while i< len(new_set):
    print(new_list[i]) #HERE new_set[i] is not used because set has no index
    i+=1



print("\n\ \n -----------------\n \n ")



print(1 in new_list)