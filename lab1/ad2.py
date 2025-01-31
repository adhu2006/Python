a, b = 0, 1
n = int(input("Enter the number of terms: "))
if n == 1:
print(a)
elif n == 2:
print(a)
print(b)
else:
print(a)
print(b)
count = 2
while count < n:
c = a + b
print(c)
a, b = b, c
count += 1
