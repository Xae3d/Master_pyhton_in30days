ep1={ 122: 45 , 123: 56 , 567:78 , 657:98}
ep2={ 222:55 , 566:90}
ep3={ 333:564 , 666:88}

ep1.update(ep2)
ep2.update(ep3)
print(ep1)
print(ep2)

ep1.pop(123)
print(ep1)

ep2.popitem() # to delete the last item
print(ep2)