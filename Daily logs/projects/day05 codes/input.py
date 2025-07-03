#  take input from user to create dictionary 

n=int(input(" Enter how many students  :"))

students={}  #is an emoty dictionary 

for i in range(n):  #this will repeat the code n times means :
                    #  for each student 
    name=input(" Enter the name :")
    marks=int(input(" Enter the marks here :"))

    students[name]=marks #this adds the name & marks to dictionary 

print("student marks : ",marks)   
print(students) 