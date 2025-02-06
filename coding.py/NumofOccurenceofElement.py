arr = [3,4,5,6,1,2,3,4,5,66,1,2,33,4,5,55]

def counter(arr):
    dict = {}
    for element in arr:
        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 1
            
    return dict
print(counter(arr))
