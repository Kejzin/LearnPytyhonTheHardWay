name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_cm = height * 2.53
weight_kg = weight * 0.43

print(f"Let's talk about {name}.")
print(f"He's {height} inchess tall.")
print(f"He's {weight} pounds heavy.")
print(f"He would be {weight_kg} kg heavy and {height_cm} cm tall if he will be an European")
print("Actually that's not to heavy.")
print(f"He's hot {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffe.")

# this lineis tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
