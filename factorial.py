def factorial(a):
        if a==0:
                return 1
        else:
                return(a*factorial(a-1))
x=int(input("Enter the number"))
print("Factorial of {} is {}".format(x,factorial(x)))
