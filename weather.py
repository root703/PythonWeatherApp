import requests

def get_weather(city):
    api_key = '4c2b74b53be4cb09ba8f752889d2fe1a'  # Replace with your actual API key
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    
    # Make the request with parameters
    response = requests.get(base_url, params={'q': city, 'appid': api_key})
    data = response.json()

    if response.status_code == 200:  # Check if the request was successful
        main = data.get('main', {})
        weather_desc = data['weather'][0]['description']
        temperature = main.get('temp', 'N/A')
        pressure = main.get('pressure', 'N/A')
        humidity = main.get('humidity', 'N/A')

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}K")
        print(f"Pressure: {pressure}hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_desc}")
    else:
        print(f"City {city} not found or API request failed.")
        print(f"Error code: {data['cod']}, Message: {data.get('message', 'No message')}")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
