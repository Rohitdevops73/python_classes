#with syntax

with open("README.md", "r") as f:
    data = f.read()
    print(data)

with open("README.md", "w+") as d:
    data = d.write("this is new data entered using with syntax welcome")
    

