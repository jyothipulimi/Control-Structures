n = int(input("Enter a number: "))
flag = 1

for i in range(2, n):
    if n % i == 0:
        flag = 0
        break

if flag == 1:
    print("Prime Number")
else:
    print("Not a Prime Number")
