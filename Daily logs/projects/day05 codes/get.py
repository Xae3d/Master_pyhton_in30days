#  get method 
person={
    "name":["Saeed", "irfan" , "Aftab","imran"],
        "age":[20 , 21 , 19 ,34 ]
        }
print(person)
print( person["name1"]) # it will stop code running while error so we use methods
print(person.get("name1")) # while error it print none and continue
print(person.get("age"))
print( person["name"])

