#WAF that replace all occurrences of "java with Python in above file"

with open("Practice/practice.txt","r") as f:
    data=f.read()
new_data=data.replace("java" ,"python")
print(new_data)

with open("Practice/practice.txt","w") as f:
    f.write(new_data)