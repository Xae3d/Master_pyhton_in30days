#  convert a string "1 2 3 4 5 " into a list of integrr

# creating the string 
string="1 2 3 4 5 "
# splits the strings into parts and converta to list 
splitlist=string.split()
#  printing it 
print(splitlist)       # output will be ['1', '2', '3', '4', '5']
# use map to convert each string to an integer 
mapped_list=map(int, splitlist)

# Step 4: Convert the map object to a list
int_list = list(mapped_list)

# Step 5: Print the final list
print(int_list)
