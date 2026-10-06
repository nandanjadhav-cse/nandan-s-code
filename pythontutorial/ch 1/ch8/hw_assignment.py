#  1 
pi=3.14159265359
print ("{:.2f}".format(pi)) 

# {} → place where the value will be inserted
# : → tells Python that formatting instructions are coming
# .2 → keep 2 digits after decimal
# f → treat the number as a floating-point number
# .format(pi) → puts the value of pi into {}

print("my name is {}".format("nandan"))  

# % format method 
print("%.2f"% pi)


# f string method 
print(f"{pi:.2f}")


my_string="regression analysis"

print(f"{my_string[3:-3:]}") 
# ression analy  @ output

print("%s"%my_string[3:-3])



print("{}".format(my_string[3:-3]))


print(my_string[::-1])\

print("{}".format(my_string[::-1]))


print("%s"% my_string[::-1])


print(f"{my_string[::-1]}")


def palindrome(my_string):
    if my_string==my_string[::-1]:
        print("YES")
    else:
        print("NO") 


palindrome("naman")