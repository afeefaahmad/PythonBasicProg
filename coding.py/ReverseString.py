def reverse_string(str):
    reverse_str = " "
    for char in str:
        reverse_str = char + reverse_str 
    return reverse_str
print(reverse_string("hello"))  

*********************************************
def reverse_string(str):
    reversedStr = str[: : -1]
    
    return reversedStr

print(reverse_string("hello")) 
