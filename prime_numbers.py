def prime(n):
    count = 0
    for each in range(2,n//2):
        if(n%each)==0:
            count +=1
            print(f'{n} isnot a prime number')
            break

    if(count == 0):
        print("THE NEXT PRIME NUMBER IS {}".format(n))
        return True


num = int(input("Enter a number to start finding the prime numbers:"))

user = 1
while (user==1):
    num +=1
    check = prime(num)
    user = int(input("Do you want to find next prime number? If Yes enter 1 and if no enter 0:"))


