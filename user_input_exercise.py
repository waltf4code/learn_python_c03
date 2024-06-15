# User Input Exercise
# Distance converter converting kilometers to miles
# Take two input from user
# Their first name and the distance in miles

# Print:
# Greet user by name and show km, and mile values

# 1 mile is 1.609 kilometers
# Hint: use correct types for calculating and print
# Note: Did you capitalize the name

first_name = input(str("Digit a first name: "))
distance_km = input("Digit a distance: ")
distance_mi = float(distance_km) / 1.609
print(f"Hi  {first_name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles  ")