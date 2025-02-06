
#Palindrome
def is_Palindrome(str):
    if str == str[: :-1]:
        print("String is Palindrome")
    else:
        print("Not")
        
    return -1

str = "nitin"
is_Palindrome(str)

#Fibonacci series
#nth term fibonacci

#Return duplicate elements:
def find_duplicated(arr):
    
    unique = []
    duplicate = []
    
    for element in arr:
        if element in unique:
            duplicate.append(element)
        else:
            unique.append(element)
            
    return duplicate
    
    
arr = [2,1,3,4,5,6,4,3,2,8,9]
print(find_duplicated(arr))

#Return Unique elements:



    
