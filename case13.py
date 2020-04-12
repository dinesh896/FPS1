"""
Print the some of items in lise with condition-
1. do not add any 13
2. do not add any no. just after 13 for consecutive 13 also
"""

list1 = [13,13, 1, 2, 13, 2, 1, 13]
list2 = []  #for storing indexes of items to exclude
list3 = []  #for storing items to exclude from list  
set1 = {}   #for getting unique indexes
l=len(list1)

for index, item in enumerate(list1):
    if item == 13:
       list2.append (index)
       if index<l-1:
           list2.append (index+1)
set1 = set(list2)
list2 = list(set1)
print("List of Indexes to exclude:", list2)       
       
for x in list2:
    list3.append(list1[x])       
print("Result is:",sum(list1) - sum(list3))