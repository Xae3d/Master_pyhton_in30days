# sort a list of numbers inascending and descending order .

list1=["10" , "30" , "20" , "66" , "76" , "34" , "10","10"]

asccending=sorted(list1) #this is another method to sort
print( " The sorted list in asending order : ", asccending)
descending=sorted(list1,reverse=True)
print(" The list sorted in descending order : ",descending)
count=list1.count("10")
print(count)

