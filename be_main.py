import math
from functools import wraps

def convert_to_number(value, name = "value"):
    if isinstance(value, (int, float)):
        number = float(value)
    elif isinstance(value, str):
        try:
            number = float(value.strip())
        except ValueError:
            raise ValueError(f"{name} must be a number or a numeric string... ")
    else:
        raise ValueError(f"{name} must be a number or a numeric string... ")
    
    if math.isfinite(number) == False:
        raise ValueError(f"{name} must be a finite number... ")
    return number

def check_safe_input(name = "value"):
    def decorate_function(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            try:
                x = convert_to_number(x, name)
                result = func(x, *args, **kwargs)
                return result
            except Exception as e:
                return {"error": str(e)}
        return wrapper
    return decorate_function
        
class UnitConverter:
    @check_safe_input("celsius")
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @check_safe_input("fahrenheit")
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    @check_safe_input("celsius")
    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15
    
    @check_safe_input("kelvin")
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
    
    @check_safe_input("fahrenheit")
    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15
    
    @check_safe_input("kelvin")
    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32
    
    @check_safe_input("meters")
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084
    
    @check_safe_input("feet")
    @staticmethod
    def feet_to_meters(feet):
        return feet / 3.28084
    
    @check_safe_input("kilometers")
    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * 0.621371

    @check_safe_input("miles")
    @staticmethod
    def miles_to_kilometers(miles):
        return miles / 0.621371 
    
    @check_safe_input("kilograms")
    @staticmethod
    def kilograms_to_pounds(kilograms):
        return kilograms * 2.20462  
    
    @check_safe_input("pounds")
    @staticmethod
    def pounds_to_kilograms(pounds):
        return pounds / 2.20462 
    
    @check_safe_input("liters")
    @staticmethod
    def liters_to_gallons(liters):
        return liters * 0.264172
    
    @check_safe_input("gallons")
    @staticmethod
    def gallons_to_liters(gallons):
        return gallons / 0.264172   
    
    @check_safe_input("square_meters")
    @staticmethod
    def square_meters_to_square_feet(square_meters):
        return square_meters * 10.7639
    
    @check_safe_input("square_feet")
    @staticmethod
    def square_feet_to_square_meters(square_feet):
        return square_feet / 10.7639
    
    @check_safe_input("cubic_meters")
    @staticmethod
    def cubic_meters_to_cubic_feet(cubic_meters):
        return cubic_meters * 35.3147   
    
    @check_safe_input("cubic_feet")
    @staticmethod
    def cubic_feet_to_cubic_meters(cubic_feet):
        return cubic_feet / 35.3147
    
    @check_safe_input("pascals")
    @staticmethod
    def pascals_to_psi(pascals):
        return pascals * 0.000145038
    
    @check_safe_input("psi")
    @staticmethod
    def psi_to_pascals(psi):
        return psi / 0.000145038
    
    @check_safe_input("joules")
    @staticmethod
    def joules_to_calories(joules):
        return joules * 0.239006    
    
    @check_safe_input("calories")
    @staticmethod
    def calories_to_joules(calories):
        return calories / 0.239006
    

