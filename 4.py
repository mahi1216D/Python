list1 = [5,9,3,7,9,1]
#oddoreven(list)
list1 = [5,9,3,79,9,1]
print(list1[-1], list1[3])
print(len(list1),type(list1))
list1[2]=30
print(list1)
list1.insert(3,70)
print(list1)
list1.pop(4)
print(list1)
list2=list1.copy()
list1.extend([10,20,30])
print(list1)
list1.sort()
print (list1)