import pycountry
from datetime import datetime

# Get a list of all countries
all_countries = list(pycountry.countries)

# Extract the country names from the list
country_names = [country.name for country in all_countries]

class Person:
    
    gender = ('M', 'F')
    
    def __init__(self, name:str, gender=None, citizen=None):
        self.name = name
        self.age = age
        if gender in self.gender:
            self.gender = gender
        else:
            raise ValueError("Incorrect gender")
        if citizen in all_countries:
            self.citizen = citizen
        
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nCitizenship: {self.citizen}"
    
    def BirthDay(self, dob_str):
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
            return dob
        except ValueError:
            print("Invalid date and time")
        
    def Age():
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def Citizenship():
        return self.citizen
    
    def TravelHistory():
        pass
    
    def CurrentTour():
        pass
    
    def FutureTour():
        pass

class Location:
    
    def __init__(self, lat:float, lon:float):
        pass

        
    def Place(self, name, continent,country, region, Category, Service):
        pass

    
class Outlet(Location, Person):
    def __init__():
        pass

    def Owner(self, name):
        pass

    def Contact():
        pass

    def Address():
        pass
    
    def Rating():
        pass
    
    def RatingChange():
        pass


class Product():

    cost_name = ["Price", "Fee", "Fare", "Cost"]
    def __init__():
        pass
    
    def Category():
        pass

    def Cost(cost_name:str):
        pass

    def CostChange():
        pass

        
    