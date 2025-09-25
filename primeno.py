total = 0
for num in range(100,502):   #numbers from 100 to 501
    
    if num > 1:
     is_prime = True
     for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
            if is_prime:
                total += num
                
    print("Sum of prime numbers between 100 and 501 is:",total)
                 
            