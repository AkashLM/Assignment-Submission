


#Input from the user
num = int(input("Enter a number: "))


temp = False

# prime numbers are greater than 1

if num > 1:
  
    for i in range(2, num):
        if (num % i) == 0:
            
            temp = True
            
            break


if temp:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
