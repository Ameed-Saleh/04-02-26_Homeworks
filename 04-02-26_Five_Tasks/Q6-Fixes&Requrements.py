

import time

last_name = str("PErETZ")
while True:
    if last_name.isupper():
        print("valid")
        break
    else:
        last_name = last_name.upper()
        break

first_name= str("daNny")
while True:
    if first_name.islower():
        print("valid")
        break
    else:
        first_name = first_name.lower()
        break

country = str("IL58")
while True:
    if country.isalpha() and len(country) <= 3 and country.isupper():
        break
    else:
        country = str(input("enter country (capital only, max letters 3): "))
        continue

city_address = str(" tEL aviV ")
while True:
    city_address = city_address.title()
    break

zipcode = str("  20128  ")
while True:
    zipcode = zipcode.strip()
    if zipcode.isdigit() and len(zipcode) >= 4:
        break
    else:
        zipcode = str(input("enter zipcode (digit only, at least 4): "))
        continue
time.sleep(2)
print(" - "*20)
print("details of post office delivery")
print(f"FOR : {last_name},{first_name}")
print(f"COUNTRY : {country}")
print(f"ADDRESS : {city_address}")
print(f"ZIPCODE :{zipcode}")