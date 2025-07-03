# .values method 
student={
    "name ":["rahul k","abhi"],
    "subject":{
        "phy":97,
        "chem":97,
        "Bio":97,
    }
}
print(student.values())
# we can convert it list

print(list(student.values()))

print(student.items())

pairs=list(student.items())
print(pairs[0])
print(pairs[1])