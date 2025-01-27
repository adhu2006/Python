n=int(input("enter a number: "))
t=n
rev=0
while n!=0:
 print("value of n is",n)
 r=n%10
 print("value of r is",r)
 rev=rev*10+r
 print("value of rev is",rev)
 n=n//10
 print("value of n is",n)
print("reverse of number",t,"is:",rev)
