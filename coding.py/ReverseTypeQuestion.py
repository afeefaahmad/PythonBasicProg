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


#Armstrong  
def isArmstrong(num):
    original = num
    sol=0
    
    while original > 0:
        digit = original%10
        original = original//10
        sol = sol + digit**3
        
    return sol == num
    
print(isArmstrong(153))


#Sum of Digits
def DigitSum(num):
    original = num
    sol=0
    
    while original > 0:
        digit = original%10
        original = original//10
        sol = sol + digit
        
    return sol
    
print(DigitSum(153))
