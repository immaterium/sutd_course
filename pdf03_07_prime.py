def is_prime(num):
    if num > 1:
    # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                return False
                print(i,"times",num//i,"is",num)
                break
        else:
            return True
            
        # if input number is less than
        # or equal to 1, it is not prime
    else:
        return False

print("is_prime(2)") 
ans=is_prime(2) 
print(ans)

print("is_prime(3)") 
ans=is_prime(3) 
print(ans)

print("is_prime(7)") 
ans=is_prime(7) 
print(ans)

print("is_prime(9)") 
ans=is_prime(9) 
print(ans)

print("is_prime(21)") 
ans=is_prime(21) 
print(ans)
