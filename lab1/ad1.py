n = 5
# Upper part of the pattern
for i in range(1, n + 1):
for j in range(i):
print("* ", end="")
print()
# Lower part of the pattern
for i in range(n - 1, 0, -1):
for j in range(i):
print("* ", end="")
print()
