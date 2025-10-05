n=17
prime=True

for i in range(2,n):
    if n%i==0:
        prime=False
        break
    if prime:
        print("it is prime",i)
    else:
        print("it is not prime")
