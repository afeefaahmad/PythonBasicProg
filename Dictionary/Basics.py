#Creating dictionary
d1 = {'a':10, 'b':20, 'c':30}
d2 = dict(a=10, b=20, c=30)
print(d1)
print(d2)

#Accessing elements 
print(d1['b'])
print(d1.get('b'))

#Adding elements
d1['d'] = 40

#Updating elements
d1['b'] = 200

#Iterating: over-keys over-values  over-key-values
for k in d1:
    print(k)
    
for v in d1.values():
    print(v)
    
for k,v in d1.items():
    print(f"{k}:{v}")
    


#Removing elements: del pop() clear()
#del d1['b']
#print(d1)

#print(d2.pop('b'))

#d2.clear()
#print(d2)


