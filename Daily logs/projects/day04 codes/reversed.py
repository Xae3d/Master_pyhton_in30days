# Reversed a list using slicing and and using reverse 
 
fruits=["mango","apple","banana","pineapple","mango","grapes",]

slicing=fruits[::-1]
print(" reverse the list using slicing : \n",slicing)
fruits.reverse()
print("reverse the list using reverse method :\n",fruits)

#  another way to use reversed function

reverselist=list(reversed(fruits))
print("the reversed list is : ",reverselist)
