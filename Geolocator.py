from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

Latitude = input("Enter the Latitude: ")
Longitude = input("Enter the Longitude: ")

location = geolocator.reverse(Latitude+","+Longitude)
  
address = location.raw['address']

#city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
code = address.get('country_code')
zipcode = address.get('postcode')
#print('City : ', city)
print('State : ', state)
print('Country : ', country)
print('Zip Code : ', zipcode)
