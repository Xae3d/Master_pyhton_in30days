#  to cjeck the list is palindrome or not use copy().
#  pakindrome : ex 1,2,1 read and write it from any order it will same 1,2,1


list1=[ 2 , 1 , 2 , ]  # created th list
copyoflist1=list1.copy()   #copied the list1 
copyoflist1.reverse()     # reversed the copied list 

if( copyoflist1 == list1 ):
    print(" THe list is palindrome ")
else:
    print(" The list is not palindrome ")  

#  taking input from user 

user=input(" Enter the list here : ")

originallist=user.split() # split() converts the strings into list 
                    # user gives input is always treated as string 

copyoflist1=originallist.copy()   
reversedlist=copyoflist1.reverse()

if( originallist == reversedlist ):
    print(" THe list is palindrome ")
else:
    print(" The list is not palindrome ") 