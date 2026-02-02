#prime number program ani
n = int(input("Enter number: "))
i = 2
flag = 1

if n <= 1:
    flag = 0
else:
    while i < n:
        if n % i == 0:
            flag = 0
            break
        i += 1

if flag == 1:
    print("Prime number")
else:
    print("Not a prime number")

