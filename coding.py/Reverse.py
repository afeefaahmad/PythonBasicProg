#Reverse a number
#Check Palindrome
def isPalindrome(n):
    original = n
    rev = 0
    
    while original > 0:
        rem = original%10
        rev = rev*10 + rem
        original = original//10
        
    return rev==n
    
n = int(input("Enter number: "))
print(isPalindrome(n)) 

