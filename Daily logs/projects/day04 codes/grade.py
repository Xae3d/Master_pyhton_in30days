#  count no of students with A grade in following tuple .

grade=( "C","D","A", "A", "B" , "B" , "A")
students=grade.count("A")
print(" The number os students with grade A in the tuple is ", students)

# store the above values in list and sort them froom A to B .

grade=( "C","D","A", "A", "B" , "B" , "A")

newlist=list(grade) # list() functions conerts the tuple into the list .
print(newlist)
newlist.sort()
print(newlist)
#  now here we can chnage the list that we convertes from tuple .
newlist.append(20)
newlist[3]=5
print(newlist)
