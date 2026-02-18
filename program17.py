# Create a function that convert degree celsius to fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (1.8 * celsius) + 32
    return fahrenheit

temp = celsius_to_fahrenheit(67)
print(temp)

