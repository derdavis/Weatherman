Derrick's Weatherman weather program draft
Date 5/2/2021
Intro to programming


import requests
import json

welcome message = input("Welcome to the Weatherman Weather forecast: Press Enter to Continue")

#After hitting enter, the use can enter a zip code or city.

def ww_zip():
    zip_code = int(input('Enter Your Zip code: '))
    response = requests.get('api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}')
    api_data = response.json()
    display_data(data)

    question = input('Do you want to do another search ? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Thank you for using the program. Good Bye!")
        exit()

#Or if they choose to enter a city

def ww_city():
    city = input('Enter name of city: ')
    response = requests.get(api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key})
    api_data = response.json()
    display_data(data)

    question = input('View another city? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Thank you for using the program. Good Bye!")
        exit()

#Below we can see the different weather information displayed.

def display_data(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    press = data['main']['pressure']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    humid = data['main']['humidity']
    description = data['weather'][0]['description']

    print('Current Temperature : {} degree fahrenheit'.format[temp])
    print('High Temperature : {} degree fahrenheit'.format[hightemp])
    print('Low Temperature : {} degree fahrenheit'.format[lowtemp])
    print('Humidity : {} %'.format[humid])
    print('Wind Speed : {} m/s'.format[wind_speed])
    print('Pressure : {} hPa'.format[press])
    print('Latitude : {}'.format[latitude])
    print('Longitude : {}'.format[longitude])

    print('Description : {}'.format(description))


#The main function that I'm going to use will work similar to how it's shown below and also includes the try blocks.


def main():
   while True:
    answer = input("Would you like to check another area? Type city to enter a city or zip to enter a new zip code: ")
      if answer = 'zip':
          try:
              print("Perfect! Let's continue.")
              ww_zip()

          except:
              print("Response was invalid. Please try again")
              ww_zip()

      if answer = 'city':
          try:
             print("Perfect! Let's continue.")
             ww_city()

          except:
             print("hmm, You did not enter a valid name. Try again")
             ww_city()

          else:
            print("Oops. Let's try that again.")
