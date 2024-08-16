import phonenumbers
from phonenumbers  import timezone,carrier,geocoder
Number=input('Enter your phone number with contary code :')
phone=phonenumbers.parse(Number)
time=timezone.time_zones_for_number(phone)
carrier__=carrier.name_for_number(phone , 'en') # en stands for English 
Geo_loc=geocoder.description_for_number(phone , 'en')

print(phone)
print(time)
print(carrier__)
print(Geo_loc)