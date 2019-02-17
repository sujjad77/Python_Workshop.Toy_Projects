#factorial using recursion
def factorial(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return num*factorial(num-1)


#factorial using loop
def fact(num):
    fact = 1
    if (num == 0 or num == 1):
        return 1
    else:
        for each in range(1,num+1):
            fact = fact * each
        return fact



n = int(input("Enter a number to find its factorial: "))
print(f"The factorial using recursion is : {factorial(n)}")
print(f"The factorial using loop is : {fact(n)}")




