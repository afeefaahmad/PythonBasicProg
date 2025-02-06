def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
            
    return True


print(isPrime(15))       #To check if it's a prime
prime_num = [x for x in range(1, 101) if isPrime(x)]
print("Prime numbers from 1 to 100 :", prime_num)      #To calculate prime from 1 to 100

