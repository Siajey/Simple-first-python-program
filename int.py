#----- version 1 -----

n = 11

# Handle small values
if n <= 1:
    print(n, "is not prime")
else:
    prime = True
    # check divisibility from 2 up to n-1
    for i in range(2, n):
        if n % i == 0:
            prime = False
            divisor = i
            break

    # The print must be done after the loop. In the original code the prints
    # were inside the loop and the 'if prime' check ran before the loop had
    # finished checking all divisors.
    if prime:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime — divisible by {divisor}")



#----- version 2 -----

# this Program to print prime numbers between 1 and 100

for number in range(2, 101):  # from 2 to 100
    is_prime = True # we assume the number is prime
    
    for i in range(2, int(number ** 0.5) + 1):  # check divisibility up to the square root of the number
        if number % i == 0:   # if divisible
            is_prime = False  # not a prime number
            break
    
    if is_prime:
        print(number)




