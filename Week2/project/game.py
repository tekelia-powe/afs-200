answer = int(input('Please enter a number? '))

even = answer % 2
multiple = answer % 4
if even == 0:
    if multiple == 0:
        print("Your number is even and a multiple of 4")
    else:
        print("Your number is even.")

else:
    print("Your number is odd.")


num = int(input("Please enter number 1? "))
check = int(input("Please enter number 2? "))

if (num%check)==0:
    print("Number 1 is divisible by Number 2")
else:
    print("Number 1 is not divisible by Number 2")