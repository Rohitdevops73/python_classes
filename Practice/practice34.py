#create a new file practice.txt using pythong. add the follow data in it:

# Hi everyone 
# we are learning file I/O 
# using java. 
# I like programming in java

# f= open("practice.txt","w+")

# data=f.write("Hi everyone\nwe are learning file I/O\nusing java.\nI like programming in java")


with open("Practice/practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning file I/O\nusing java.\nI like programming in java\n updated")
