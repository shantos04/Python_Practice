# TASK 1

"""
# Create the playlist variable
playlist = [1, "Blinding Lights", 2, "One Dance", 3, "Uptown Funk"]

# Print the list
print(playlist)

# Print all songs in the playlist
print(playlist[1::3])

# Print the song by Coldplay
print(playlist["Coldplay"])

# Add a new song
playlist["Usher"] = "Yeah!"

# Print the songs in the playlist
print(playlist.values())
"""

# TASK 2

"""
# Create a tuple
q3_financials = (325780, 1041, 4271599)

# Print the tuple
print(q3_financials)

hip_hop = ["Drake", "JAY-Z", "50 Cent", "Drake"]

# Create a set
indie_set = {"Kings of Leon", "Arctic Monkeys", "Stereophonics"}

# Convert hip_hop to a set
hip_hop_set = set(hip_hop)

# Print the indie and hip_hop sets
print(indie_set)
print(hip_hop_set)
"""

# TASK 3

"""
# Check if September inflation is less than August inflation
if inflation_september < inflation_august:
  print("Inflation decreased")

# Check if September inflation is more than August inflation
elif inflation_september > inflation_august:
  print("Inflation increased")
  
# Confirm that they are equal
else:
  print("Inflation remained stable")
"""

# TASK 4

"""
# Check the number of beds
if num_beds < min_num_beds:
  print("Insufficient bedrooms")

# Check square feet
elif sq_foot <= min_sq_foot:
  print("Too small")

  
# Check the rent
elif rent > max_rent:
  print("Too expensive")

  
# If all conditions met
else:
  print("This looks promising!")
"""