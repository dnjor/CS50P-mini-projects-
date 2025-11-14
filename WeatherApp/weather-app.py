from sys import exit
import requests
from datetime import datetime

def main():

    print("Welcome to weather app")                                                              #welcome massage
    print("Here you can know about all the weather around the world")

    while True:
        city = city_name()                                                                         #get the city name and check if it's vaild
        data = city_data(city)                                                                     #get the city data and print it

        while True:
            try:
                option = input("Do you want to check another city weather? (yes/no): ").lower()     #ask the user if he want to continue or exit
                if option == "no":
                    print("Thank you for using the weather app. Goodbye!")
                    exit(0)
                elif option == "yes":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input, please type 'yes' or 'no'")
                continue
    

def city_name():
    while True:
        try:
            city = input("Type the city here: ").title()
            if not isalpha_space(city):
                print(city, "not alpha")                                                #check if the input is valid
                raise ValueError
        except ValueError:
            print("Invalid input, you must enter the name of the city")
        else:
            return city

def city_data(city_name):
    
    api_key = api_key = "YOUR_API_KEY_HERE"                                                      #this is my api key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"             #now we create the url with f string to get the data from api
    response = requests.get(url)                                                                       #send the request to the api
    
    if response.status_code != 200:
        print("City not found. Please check the city name and try again.")
        exit(1)
    response.raise_for_status()                                                                         #check if the request was successful
    data = response.json()                                                                              #now json translata the data, so we can use it                                 

    weather_country = data["sys"]["country"]
    weather_desc = data["weather"][0]["main"]
    weather_desc2 = data["weather"][0]["description"]
    temp = data["main"]["temp"]

    weather_temp = temp - 273.15                                        #convert the temp to celsius
    
    sunrise_number = data["sys"]["sunrise"]                            #we get the nmbers from json data
    sunset_number = data["sys"]["sunset"]

    sunrise_time = datetime.fromtimestamp(sunrise_number)             #now we convert them to readable time             
    sunset_time = datetime.fromtimestamp(sunset_number)

    print(f"Weather in {city_name}, {weather_country}")
    print(f"Description : {weather_desc} - {weather_desc2}")
    print(f"Temperature : {weather_temp:.2f} °C")
    print(f"Sunrise at : {sunrise_time.strftime('%H:%M:%S')}")
    print(f"Sunset at : {sunset_time.strftime('%H:%M:%S')}")

    return data

def isalpha_space(s):                                                  #fuction to cheak if the string containe only litters and speace
    return all(char.isalpha() or char.isspace() for char in s)         #return True if all characters are letters or spaces


main()
