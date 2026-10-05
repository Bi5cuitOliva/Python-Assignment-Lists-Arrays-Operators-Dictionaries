# students
student1 = {
    "name": "Alice",
    "phone": "0712345678",
    "age": 18,
    "location": "Nairobi",
    "dob": "2007-03-15"
}

student2 = {
    "name": "Bob",
    "phone": "0723456789",
    "age": 20,
    "location": "Mombasa",
    "dob": "2005-07-22"
}

student3 = {
    "name": "Charlie",
    "phone": "0734567890",
    "age": 19,
    "location": "Kisumu",
    "dob": "2006-11-08"
}

print("AllStudents:")
print(student1)
print(student2)
print(student3)

# put them in one dictionary so as to make it easy
students = {
    "s1": student1,
    "s2": student2,
    "s3": student3
}

# add a new student
students["s4"] = {
    "name": "Eve",
    "phone": "0745678901",
    "age": 17,
    "location": "Nakuru",
    "dob": "2008-01-30"
}

print("\nAfter adding Eve:")
print(students)

# edit Alice's phone
students["s1"]["phone"] = "0799999999"
print("\nAfter editing Alice's phone:")
print(students["s1"])

# delete Charlie
del students["s3"]
print("\nAfter deleting Charlie:")
print(students)