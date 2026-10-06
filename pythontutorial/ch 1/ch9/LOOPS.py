
# loops in python

# printing numbers from 0 to 4



# WHILE LOOP
count=0

# while count<5:
#     print(count)
#     count+=1


# count=5
# while count> 0:
#     print(count)
#     count-=1
# else:
#     print("WHILE LOOP ENDED")



# # FOR LOOP
# # FOR STRINGS AND 
# language="PYTHON"

# for x in language:
#     print(x)



# # LOOP CONTROL STATEMENTS

# # PASS STATEMENT 

# while x in range(5):
#     # abhi mood NHI HE

#     pass


# ex2
for i in range(10):
    if i == 3:
        pass
    else:
        print(i)    



# x=1
# while x in range(10):
#     print(x)
   
##### PRODUCES AN INFINITE LOOP OF (1)

# ### BECAUSE x==1 IN RANGE(5) IS TRUE 


x=1
while x in range(10):
    print(x)
    x+=1


# NOW THIS WILL NOT GIVE YOU ANY INFINITE LOOP

# BREAK STATEMENT

# TERMINATES THE LOOP ENTIRELY AT THE SPECIFIED CONDITION

#### how to break infinite loop 

# don't run --infinite loop
# while True:
#     take_input=input("ENTER 'exit' to stop:")
#     if take_input == "exit":
#         print ("CONGRATS YOU GUESSED IT RIGHT")
#         break




