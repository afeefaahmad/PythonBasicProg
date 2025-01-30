def find_middle(str):
    str_length = len(str)
    mid = str_length//2
    if(str_length%2!=0):
        return str[mid]
    else:
        return str[mid-1:mid+1]


str = input("Enter string : ")
print("Middle of string:", find_middle(str))
