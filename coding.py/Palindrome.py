def isPalindrome(num):
    original = num
    reversedNum = 0
    
    while num > 0:
        digit = num%10
        reversedNum = reversedNum*10+digit
        num = num//10
        
        
    return reversedNum == original
    
print(isPalindrome(111))
