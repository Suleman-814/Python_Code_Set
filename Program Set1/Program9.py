# Program to convert temperatures to and from Celsius, Fahrenheit

def celsius_to_fahrenheit(c):
    # find temperature in Fahrenheit
    f = (c * 9)/5 + 32
    return f

def fahrenheit_to_celsius(f):
    # find temperature in Celsius
    c = (f - 32) * 5 / 9
    return c

print("Enter a temperature value:")
temperature = float(input())

# Assuming the input temperature is in Celsius and converting it to Fahrenheit
fahrenheit = celsius_to_fahrenheit(temperature)
print(f"{temperature}°C is {fahrenheit}°F")

# Assuming the input temperature is in Fahrenheit and converting it to Celsius
celsius = fahrenheit_to_celsius(temperature)
print(f"{temperature}°F is {celsius:.2f}°C")

