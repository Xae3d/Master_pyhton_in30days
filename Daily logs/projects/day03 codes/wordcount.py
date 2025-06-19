#  senetence word count checker 

sentence=input("Enter the sentence : ")
words=sentence.split()  # .split it coverts full sentence into lists 

if(len(words)>=10):
    print(" thats a long sentence ")
elif(len(words)<=5):
    print(" Its an short senetencs ")
else:
    print(" senetencs is short and sweet ")