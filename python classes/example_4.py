#Create a class named Temperature. Make two methods:
# 1 convertFahreheit -  it will take celsius and will print it into Fahrenheit.
# 2 convertCelsius - it will take Fahrenheit and will convert it into Celsius

class Temperature:
    def __init__ (self, celsius, fahrenheit):
       self.celsius = celsius
       self.fahrenheit = fahrenheit
    
    def convert_Celsius(self):
        fahrenheit = (celsius * 9/5) + 32
        celsius = (fahrenheit - 32) * 5/9
        return self.celsius ==(fahrenheit - 32) * 5/9
    
    def convert_Fahrenheit(self):
        fahrenheit = (celsius * 9/5) + 32
        celsius = (fahrenheit - 32) * 5/9
        return self.fahrenheit == (celsius * 9/5) + 32
    
Temp = Temperature(
    celsius = float(input("Enter Temperature in  fahrenheit: ")),
    fahrenheit = float(input("Enter Temperature in celsius : "))
)
print("Temperature in celsius = ", Temp.convert_Celsius())
print("Temperature in celsius = ",Temp.convert_Fahrenheit())