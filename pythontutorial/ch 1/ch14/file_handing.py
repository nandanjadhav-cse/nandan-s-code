
# here we are going to learn how to :


# 1 OPEN A FILE IN PYTHON + READING IT 

file=open(r'C:\Users\admin\Downloads\example.txt','r')

content =file.read()

# print(content)



# file.close()



# Name: Alex
# Age: 18
# Course: Computer Science
# Favorite Language: Python

# This is a simple text file for practicing Python file handling.

# You can practice:
# 1. Reading the entire file.
# 2. Reading one line at a time.
# 3. Reading all lines into a list.
# 4. Adding new text to the end of the file.
# 5. Writing new content to the file.
# 6. Counting the number of lines and words.
# 7. Searching for a word such as Python.


print("\n \n-------------\n \n")



# 2 READING LINE BY LINE FROM A FILE 

# file=open(r'C:\Users\admin\Downloads\example.txt','r')

line =file.readline()    #ONLY READS FIRST LINE 

# Python File Handling Practice



print(line)


lines=file.readlines()

print(lines)


file.close()       #GOOD PRACTICE IN PYTHON  





# write to a file 
file=open(r"C:\Users\admin\Downloads\example.txt", 'w')

file.write("hello world")   #OVER WRITES EXISTING TEXT

# USING APPEND MODE 


# WE CAN ADD  TEXT WITHOUT REMOVING EXISTING ONE
 
file=open(r"C:\Users\admin\Downloads\example.txt", 'a')

file.write("how aaaaaaer uuuuuuuuuuuuu!!!!!!!!")
file.close()



print("\n \n-------------\n \n")



# read new file 

file=open(r"C:\Users\admin\Downloads\example.txt", 'r')

new_content = file.read()



print(new_content)


file.close()




