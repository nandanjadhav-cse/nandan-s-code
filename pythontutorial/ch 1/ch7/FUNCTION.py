
# how a function is defined 

# we will see this how our print function is defined in python 

print("nandan")

# use ctrl and press the print function


# def print(
#     *values: object,
#     sep: str | None = " ",
#     end: str | None = "\n",
#     file: SupportsWrite[str] | None = None,
#     flush: Literal[False] = False,
# ) -> None: ...
# @overload
# def print(
#     *values: object, sep: str | None = " ", end: str | None = "\n", file: _SupportsWriteAndFlush[str] | None = None, flush: bool
# ) -> None: ...

# _E_contra = TypeVar("_E_contra", contravariant=True)
# _M_contra = TypeVar("_M_contra", contravariant=True)


# like this 



# FUNCTIONS IN PYTHon 


def add3num(a,b,c):
    
    print(a+b+c)




#call above function 

add3num(1,12,3)

add3num(b=1,c=3,a=4)




# USING RETURN STATEMENT 

def f_to_c(temp_in_C):
    fahrenheit= (temp_in_C *9/5)+32
    return fahrenheit




# calling this function 

print(f_to_c(25))



#WHY WE DO THIS 
# print (add3num(2,3,4)+2)



# # Traceback (most recent call last):
#   File "c:\Users\admin\Desktop\nandan's code\pythontutorial\ch 1\ch7\FUNCTION.py", line 66, in <module>
#     print (add3num(2,3,4)+2)
#            ~~~~~~~~~~~~~~^~
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# PS C:\Users\admin\Desktop\nandan's code\pythontutorial> 



#print function will give NONE TYPE VALUE 




x=f_to_c(25)

print(x+23)



# by using return statement you can do arithmetic operations on the result 


def greeting(name):
    print("HELLO",name ,"!")



greeting ("NANDAN")

#  DFAULT ARGUMENT 

def greet(name ="friend"):

    X= ("HELLO",name )
    return X

greeting_for =greet()
print (greeting_for)




# ARBITRARY ARGUMENTS


def add_numbers(*args):

    print(type(args)) #CLASS 'TUPLE'  # *args is a tuple of all the arguments passed to the function
    return sum(args)

result = add_numbers(1, 2, 3, 4, 5)    #variable number of arguments can be passed to the function using *args
print(result)


# KEYWORD ARGUMENTS 

def print_info(**kwargs):
    for key, value in kwargs.items() :
        print(f"{key}:{value}")


print_info(name="nandan", age = 18, city="delhi")


# name:nandan
# age:18
# city:delhi
# PS C:\Users\admin\Desktop\nandan's code\pythontutorial> 



