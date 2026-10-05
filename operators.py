# these are the ages of students in 2 years 
students = [
    {"name": "Alice", "age": 18},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 19},
    {"name": "Diana", "age": 21}
]

print("Ages in 2 years:")
for s in students:
    future_age = s["age"] + 2
    print(s["name"], "will be", future_age)

# i'm going to add, edit and delete on the list
students.append({"name": "Eve", "age": 17})
students[1]["age"] = 21
del students[2]

