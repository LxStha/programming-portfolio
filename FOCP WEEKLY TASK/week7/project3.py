"""Write a program that manages a list of countries and their capital cities. 
It should prompt the user to enter the name of a country. If the program already 
"knows" the name of the capital city, it should display it. Otherwise it should 
ask the user to enter it. This should carry on until the user terminates the
 program (how this happens is up to you)."""

countries_capitals = {
    "England": "London",
    "USA": "Washington, D.C.",
    "India": "New Delhi",
    "Nepal": "Kathmandu",
    "China": "Beijing",
    "Germany": "Berlin",
    "Norway": "Oslo"
}

def get_capital(country):
    standardized_country = country.strip().title()
    
    return countries_capitals.get(standardized_country, "IDK the capital")

get_country = input("Enter a country to get its capital: ")
print(get_capital(get_country))