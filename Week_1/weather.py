import requests
API_KEY = "e50b712423fc4f898b7131042252509"
City = "Nairobi"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

URL = f"{BASE_URL}?key={API_KEY}&q={City}"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    city = data['location']['name']
    country = data['location']['country']
    temp_c = data['current']['temp_c']
    condition = data['current']['condition']['text']

    print(f"Weather in {city}, {country}:")
    print(f"Temperature: {temp_c}°C")
    print(f"Condition: {condition}")
else:
    print("Error:", response.status_code)
#weather in Nairobi:

