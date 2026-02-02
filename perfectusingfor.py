n = int(input("Enter a number: "))
m = 0
for i in range(1, n):
    if n % i == 0:
        m = m + i
if m == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
