def calculator():
    print("simple calculator")
    num1=float(input("enter first number:"))
    num2=float(input("enter second number:"))
    print("select operation:")
    print("1.add")
    print("2.divide")
    choice=input("enter choice(1/2):")
    if choice=='1':
      print(f"result:{num1}+{num2}={num1+num2}")
    elif choice=='2':
      if num2!=0:
        print(f"result:{num1}/{num2}={num1/num2}")
      else:
        print("error!division by zero.")
    else: 
        print("invalid input")
calculator()
      
      
