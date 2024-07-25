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

# TASK 5

"""
# Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 30

# Loop through a range up to and including max_capacity's value
for i in range(1, max_capacity+1):
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1
  
print("Sold out:", tickets_sold, "tickets sold!")
"""

# TASK 6

"""
# Loop through the dictionary's keys and values
for key, value in courses.items():
  
  # Check if the value is "AI"
  if value == "AI":
    print(key, "is an AI course")
  
  # Check if the value is "Programming"
  elif value == "Programming":
    print(key, "is a Programming course")
  
  # Otherwise, print that it is a "Data Engineering" course
  else:
    print(key, "is a Data Engineering course")
"""

# TASK 7

"""
tickets_sold = 0
max_capacity = 50

# Create a while loop
while tickets_sold < max_capacity:
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1

# Print the number of tickets sold
print("Sold out:", tickets_sold, "tickets sold!")
"""

# TASK 8

"""
release_date = 26
current_date = 19

# Create a condition where current_date is less than or equal to the release_date
while current_date <= release_date:
  
  # Increment current_date by one
  current_date += 1
  
  # Promote purchases
  if current_date < 21:
    print("Purchase before the 21st for early access")
  
  # Check if the date is less than or equal to the 25th
  elif current_date <= 25:
    print("Coming soon!")
  else:
    print("Available now!")
"""

# TASK 9

"""
# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, value in authors.items():
  
  # Check for values less than 25
  if value < 25:
    
    # Append the author to the list
    authors_below_twenty_five.append(key)
    
print(authors_below_twenty_five)
"""

# TASK 10


# Create list comprehension: squares
squares = [i**2 for i in range(0,10)]

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)
