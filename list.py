#Here is a list of students with age
students = [
    {"name": "Alice", "age": 18},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 19},
    {"name": "Diana", "age": 21}
]

print("Original list:")
print(students)

# add a student
students.append({"name": "Eve", "age": 17})
print("\nAfter adding Eve:")
print(students)

# edit Bob's age
students[1]["age"] = 21
print("\nAfter editing Bob's age:")
print(students)

# delete Charlie
del students[2]
print("\nAfter deleting Charlie:")
print(students)