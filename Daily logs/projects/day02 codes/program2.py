# Relational or Comparing operators :

a=10
b=20

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

  #Assignment operators

num=10
sum=num+20
print(sum)  # 30

num=20
num+=40
print("num :", num) #60

num=30
num-=10
print("num :",num) #20

num=40
num *= 4
print("num : ", num) #160

num=50
num /= 15
print("num: ", num) #3.3333

num=60
num %= 7
print("num: ",num) # 4 

num=10
num**=7
print("num :", num) # 10000


# Logical operators 

a=10
b=15
print(not False) #it reverse the result
print(not(b>a))  #resulr will be false 

a=10
print(not (a>5))
print(not (a<5))

value1=True
value2=True
print(" And operator :", value1 and value2)

value1=False
value2=True
print(" And operator :", value1 and value2)

value1= False
value2= False
print(" And operator :", value1 and value2)


a=30
b=15
print( " OR operator :",(a==b) or (a>b))


a=30
b=15
print( " OR operator :",(a>b) or (a>b))