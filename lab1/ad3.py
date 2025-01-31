def factorial(n):
     if n==9 or n==1:
         return 1
      else:
         result=1
         for i in range(1,n+1):
              result *= i
          return result 
          
num =int(input)("enter a number"))

