unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    fahrenheit = round((9 * temp) / 5 + 32, 2)
    kelvin = round(temp + 273.15, 2)
    print(f"Temperature in Fahrenheit: {fahrenheit}°F")
    print(f"Temperature in Kelvin: {kelvin}K")

elif unit == "F":
    celsius = round((temp - 32) * 5 / 9, 2)
    kelvin = round(celsius + 273.15, 2)
    print(f"Temperature in Celsius: {celsius}°C")
    print(f"Temperature in Kelvin: {kelvin}K")

else:
    print("Invalid unit! Please enter 'C' or 'F'.")
