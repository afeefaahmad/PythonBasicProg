#sockMerchant : number of pair
def findPair(arr):
    setArr = {}
    duplicate = set()
    unique = set()
    count = 1
    
    for element in arr:
        if element in unique:
            
            count +=1
        else:
            unique.add(element)
            
    return count//2
    
sol = findPair([1,2,1,2,1,3,2])
print(sol)

#
