def findMinMax(arr):
    if not arr:
        return None
        
    maxNum = arr[0]
    minNum = arr[0]
    
    for a in arr:
        if(a > maxNum):
            maxNum = a
        elif(a < minNum):
            minNum = a
    return maxNum, minNum


print( findMinMax([11,22,33,44,55,66,77] ))
