#list creation
a = ['a','b','c']
b = list(('a','b','c'))

print(type(a))
print(type(b))

#Accessing : Indexing 
print(a[0])

#Adding element: append, extend, insert
a.append('d')
print(a)
a.extend(['e','f'])
print(a)
a.insert(0,'z')
print(a)

#Updating element:
a[0]="new"
print(a)

#Removing element: pop, del,remove
a.insert(0,'a') 
print(a)
a.remove('a') #Removes first occurence
print(a)
a.pop()
print(a)
del a[1] #del at specific index
print(a)

#Iterate
for i in a:
    print(i)
    
#List comprehension for creating new list 
b = [3,4,5,6,7,8]
evenNum = [val for val in b if val%2 == 0]
print(evenNum)
