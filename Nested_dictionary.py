#nested dictionary

student = {

    "name" : "rohit",
    "subjects" : {
        "maths" : 34,
        "english" : 89
    },
    "Age" : 33,         
}

# print(student["subjects"])

# print(student["subjects"]["maths"])


#nested methods

# print(len(list(student.keys())))
# pairs =list( student.items())

# print(pairs[1])
print(student["name"])
print(student.get("name"))