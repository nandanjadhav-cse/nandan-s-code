# SYNTAX 

# OUTER_LOOP:
#     INNER_LOOP:
#         INNER LOOP CODE 
#     OUTER LOOP CODE



# FOR REPEATED PRINTING OF ANOTHER LOOP 

for i in range(3):
    print("iteration no---",i)
    for num_ in range(5):
        print(num_)



    print("___________\n   \n   ")


#  print prime numbers between range of 2 to 10 using nested loop

# 1st METHOD   
count=2
while count<10:
    x=2
    prime =True
    while x<count:
        if count%x ==0:
            prime = False
            #break you can use if want but no need
        x=x+1 

    if prime:
        print(count)

    count+=1       

# by for method 
# but the logic will be the same 
print("------------")

# 2nd METHOD
a,b=map(int,input("ENTER NUM1 NUM2:").split())

def fun_ (a,b):

    if a>=2 and b>2:
      for given_nums in range(a,b):
        is_prime = True
        for i in range(2, given_nums):
            if given_nums % i == 0:
                is_prime = False
            
        if is_prime:
            print(given_nums)
    else:                   
        print(fun_(2,10))

print("--------")

# note the syntax
# 3 METHOD 
for num in range(2,10):
    for i in range(2,num):
        if num % i == 0 :
            break
    else :
        print(num)



