# Grade students based on marks

name=str(input("Enter the name of student : "))
div=str(input("Enter division :"))
roll=int(input("Enter roll no :"))
print(name ,div ,roll)
marks=int(input("Enter the marks obtained : "))
 
if(marks>=90):
    print("the student got A grade ")
elif( marks>=80 and marks<90):
    print("the student got B grade .")
elif(marks>=70 and marks<80):
    print("the student got C grade ")
elif(marks<70):
    print("The student got D grade ")    


