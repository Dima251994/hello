"""from prime import is_prime

print(is_prime(6))
"""

def isprime(num):
    if num > 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False
print(isprime(6))