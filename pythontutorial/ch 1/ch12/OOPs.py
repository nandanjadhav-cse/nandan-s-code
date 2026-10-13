
# how to use OOPs in python 

class anything():
    def __init__(self,mo_number,name):
        self.mo_number=mo_number
        self.name=name


ob1=anything(9021422083,"nandan")


ob2=anything(9503817990,"gopal")

print(ob1.name)
print(ob1.__dict__)

# supose i want to find the memory location of variable like x 

class variable:
   pass 



x=variable()


print(x) #<__main__.variable object at 0x000001F12B1E8590>



# class // this is the blueprint /properties of the objects

class clg_student :
    name="nandan"
    age=18



student1= clg_student()    #here object is been created 

print(student1)  #<__main__.clg_student object at 0x000001F12B1E86E0>

print("MY NAME IS {} I'M {} YEARS OLD" .format(student1.name,student1.age))


# MY NAME IS nandan I'M 18 YEARS OLD  this is the output 


print("\n \n ---------\n \n  ")



class clg_student :
    def __init__(self, name, age):
        
     self.name= name
     self.age= age

    def modify(i):  #this also called method 
    
    
            students[i].name=input("ENTER NAME TO BE MODIFIED :")
    
            students[i].age=input("ENTER AGE TO BE MODIFIED :")
    
    
            return

students=[]

# now we will create a for loop for taking input of the object
n=int(input("enter total number of the students :"))



for i in range(n):    #this will also define i to an object of class clg_students
    name= input("enter the name of the student :")
    age= input("enter the age of the student :")
    
    students.append(clg_student(name,age))

# here we are going to print all the data in prefered format 
    
for i in students:
    print ("MY NAME IS {} I'M {} YEARS OLD".format(i.name,i.age ))
    print("\n -----------\n ")

print("\n-----------\n")

print(i.__dict__)    
# hiw to make a dictionary of this all objects \\different because data and object are different 



# FOR ACCESSING THE DATA  WE DO  
print(students[0].name)


# also
 

for i in students:
    print(i.name)




# how to modify using aself made method


    # def modify(i):  #this also called method 


    #     students[i].name=input("ENTER NAME TO BE MODIFIED :")

    #     students[i].age=input("ENTER AGE TO BE MODIFIED :")


    #     return



clg_student.modify(0)

print(students[0].name)

print(students[0].age)


class graduate_students(clg_student):
    def __init__(self,name,age,percentage):
        super().__init__(name,age)
        self.percentage=percentage 

    def modify(self)                                                             #define previous methods 
for i in students :

    percentage=int(input(f"ENTER PERCENTAGE YOU WANT TO ADD {i}:"))
    i.percentage=graduate_students(i.name,i.age,percentage)

# also you can try this :


# for i in students :

    # percentage=int(input(f"ENTER PERCENTAGE YOU WANT TO ADD {i}:"))
    # i.percentage=percentage



# TO ADD METHODS THAT EXISTS IN PARENTS CLASS 










