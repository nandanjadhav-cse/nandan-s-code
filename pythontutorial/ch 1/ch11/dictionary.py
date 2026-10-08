# dictionary 
my_dict= {"name":"nandan","age": "18","clg":"geca"}
# access values of dictionary

for keys,values in my_dict.items():
    print(keys,values)



print("\n \n ---------\n \n")
for keys,values in my_dict.items():
    print(values,keys)


print("\n \n ---------\n \n")

for val,ke in my_dict.items():
    print(ke,val)

print("\n \n ---------\n \n")


# for values we need a different method

for x in my_dict.values():
    print(x)


# dict comp

dict_={f"{x} ka square":x**2 for x in range(1,10)}



print(dict_)



print("\n \n ---------\n \n")


dict_={"{} ka square".format(x):x**2 for x in range(1,10)}


print(dict_)

print("\n \n ---------\n \n")



dict_={"%d ka square"%x:x**2 for x in range(1,10)}


print(dict_)

print("\n \n ---------\n \n")




# {'1 ka square': 1, '2 ka square': 4, '3 ka square': 9, '4 ka square': 16, '5 ka square': 25, '6 ka square': 36, '7 ka square': 49, '8 ka square': 64, '9 ka square': 81}
#this is the output 





