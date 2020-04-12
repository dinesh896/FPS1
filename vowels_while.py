"""    Remove all the vowels from the 
    list of states using while loop  

Sample Input:
    state_name = 
    [ 'Alabama', 'California', 
    'Oklahoma', 'Florida']
Sample Output:
    ['lbm', 'clfrn', 'klhm', 'flrd'] 
"""

# NEW METHOD (USING WHILE)
  
state_name = ['Alabama', 'California', 'Oklahoma', 'Florida']

list1 = []
index=0
while index<len(state_name):
    str1 = ""
    i=0
    while i<len(state_name[index]):
        if state_name[index][i] not in "aieouAIEOU":
            str1 = str1 + state_name[index][i]
        i=i+1    
    list1.append(str1)
    index=index+1          
print("Result is:",list1)