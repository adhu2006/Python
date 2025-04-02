def convert_temperature():
    print("Choose conversion:")
    print("1. Celsius to Fahrenheit & Kelvin")
    print("2. Fahrenheit to Celsius & Kelvin")
    print("3. Kelvin to Celsius & Fahrenheit")
    choice = input("Enter choice (1-3): ")
    temp = float(input("Enter temperature: "))
    
    if choice == '1':
        print(f"{temp}°C = {(temp * 9/5) + 32}°F")
        print(f"{temp}°C = {temp + 273.15}K")
    elif choice == '2':
        print(f"{temp}°F = {(temp - 32) * 5/9}°C")
        print(f"{temp}°F = {(temp - 32) * 5/9 + 273.15}K")
    elif choice == '3':
        print(f"{temp}K = {temp - 273.15}°C")
        print(f"{temp}K = {(temp - 273.15) * 9/5 + 32}°F")
    else:
        print("Invalid choice.")

convert_temperature()

