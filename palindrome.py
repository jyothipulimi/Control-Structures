x = int(input("Enter number: "))
y = x
s = 0
while x > 0:
    d = x % 10
    s = s * 10 + d
    x = x // 10
if s == y:
    print("Palindrome")
else:
    print("Not Palindrome")
