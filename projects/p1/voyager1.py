miles_from_sun = 16637000000
miles_per_hour = 38241
au = 92955887.6 # Astronomical Units
miles_per_day = 24 * miles_per_hour

days = int(input("Number of days after 9/25/09: "))

miles_from_sun += days * miles_per_day
km_from_sun = round(miles_from_sun * 1.609344)
au_from_sun = round(miles_from_sun / au)

print("Miles from the sun:", miles_from_sun)
print("Kilometers from the sun:", km_from_sun)
print("AU from the sun:", au_from_sun)