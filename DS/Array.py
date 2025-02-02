🎈 Q1. Find position of element=40  for arr=[10,20,30,40]

  
🧩sol1. #search 
arr=[10,20,30,40]
def search(arr, data):
    for i in range(len(arr)):
        if (arr[i] == data):
            return i
            
    return -1
    
print(search(arr, 40))

🧩sol2. #binary search

arr=[10,20,30,40]
def binary_search(arr,data):
    low,high =0, len(arr)-1
    
    while low<=high:
        mid = (low+high)//2
        
        if mid == data:
            return mid
            
        elif arr[mid] < data:
            low = mid+1
            
        else:
            high = mid-1
            
    return -1
            
print(binary_search(arr, 30))           
            
