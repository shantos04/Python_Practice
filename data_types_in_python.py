# TASK 1

"""
# Create a list containing the names: baby_names
baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(['Rowen', 'Sandeep'])

# Find the position of 'Rowen': position
position = baby_names.index('Rowen')

# Remove 'Rowen' from baby_names
baby_names.pop(position)

# Print baby_names
print(baby_names)
"""

# TASK 2

"""
# Create the list comprehension: baby_names
baby_names = [row[3] for row in records]
    
# Print the sorted baby names in ascending alphabetical order
print(sorted(baby_names))
"""

# TASK 3

"""
# Pair up the girl and boy names: pairs
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for rank, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print(f'Rank {rank+1}: {girl_name} and {boy_name}')
"""

# TASK 4

"""
# Create the normal variable: normal
normal = ('simple')

# Create the mistaken variable: error
error = 'trailing comma',

# Print the types of the variables
print(type(normal))
print(type(error))
"""

# TASK 5

"""
# Loop over top_ten_girl_names and unpack each tuple into top_ten_rank and name
for top_ten_rank, name in top_ten_girl_names:
  	# Print each name in the proper format
    print(f"Rank #: {top_ten_rank} - {name}")
"""

# TAKS 6

"""
# The top ten boy names are:  as preamble
preamble = "The top ten boy names are: "

# , and as conjunction
conjunction = (", and")

# Combines the first 9 names in boy_names with a comma and space as first_nine_names
first_nine_names = ", ".join(boy_names[0:9])

# Print f-string preamble, first_nine_names, conjunction, the final item in boy_names and a period
print(f"{preamble}{first_nine_names}{conjunction} {boy_names[-1]}.")
"""

# TASK 7

"""
# Store a list of girl_names that start with s: names_with_s
names_with_s = [name for name in girl_names if name.lower().startswith('s')]

print(names_with_s)

# Store a list of girl_names that contain angel: names_with_angel
names_with_angel = [name for name in girl_names if 'angel' in name.lower()]

print(names_with_angel)
"""

# TASK 8

"""
# Create an empty dictionary: squirrels_by_park
squirrels_by_park = {}

# Loop over the squirrels list and unpack each tuple
for park, squirrel_details in squirrels:
    # Add each squirrel_details to the squirrels_by_park dictionary 
    squirrels_by_park[park] = squirrel_details
    
# Sort the squirrels_by_park dict alphabetically by park
for park in sorted(squirrels_by_park):
    # Print each park and its value in squirrels_by_park
    print(f'{park}: {squirrels_by_park[park]}')
"""

# TASK 9

"""
# Safely print 'Union Square Park' from the squirrels_by_park dictionary
print(squirrels_by_park.get('Union Square Park'))

# Safely print the type of 'Fort Tryon Park' from the squirrels_by_park dictionary
print(type(squirrels_by_park.get('Fort Tryon Park')))

# Safely print 'Central Park' from the squirrels_by_park dictionary or 'Not Found'
print(squirrels_by_park.get('Central Park', 'Not Found'))
"""

# TASK 10

"""
# Assign squirrels_madison as the value to the 'Madison Square Park' key
squirrels_by_park['Madison Square Park'] = squirrels_madison

# Update squirrels_by_park with the squirrels_union tuple
squirrels_by_park.update([squirrels_union])

# Loop over the park_name in the squirrels_by_park dictionary 
for park_name in squirrels_by_park:
    # Safely print a list of the primary_fur_color for each squirrel in park_name
    print(park_name, [squirrel.get('primary_fur_color', 'N/A') for squirrel in squirrels_by_park[park_name]])  
"""

# TASK 11

"""
# Remove "Madison Square Park" from squirrels_by_park
squirrels_madison = squirrels_by_park.pop("Madison Square Park")

# Safely remove "City Hall Park" from squirrels_by_park with an empty dictionary as the default
squirrels_city_hall = squirrels_by_park.pop("City Hall Park", {})

# Delete "Union Square Park" from squirrels_by_park
del squirrels_by_park["Union Square Park"]

# Print squirrels_by_park
print(squirrels_by_park)
"""

# TASK 12

"""
# Iterate over the first squirrel entry in the Madison Square Park list
for field, value in squirrels_by_park["Madison Square Park"][0].items():
    # Print field and value
    print(field, value)

print('-' * 13)

# Iterate over the second squirrel entry in the Union Square Park list
for field, value in squirrels_by_park["Union Square Park"][1].items():
    # Print field and value
    print(field, value)
"""

# TASK 13

"""
# Check to see if Tompkins Square Park is in squirrels_by_park
if "Tompkins Square Park" in squirrels_by_park:
    # Print 'Found Tompkins Square Park'
    print('Found Tompkins Square Park')
    
# Check to see if Central Park is in squirrels_by_park
if "Central Park" in squirrels_by_park:
    # Print 'Found Central Park' if found
    print('Found Central Park')
else:
    # Print 'Central Park missing' if not found
    print('Central Park missing')
"""

# TASK 14

"""
# Print a list of keys from the squirrels_by_park dictionary
print(squirrels_by_park.keys())

# Print the keys from the squirrels_by_park dictionary for 'Union Square Park'
print(squirrels_by_park['Union Square Park'].keys())

# Loop over the dictionary
for park_name in squirrels_by_park:
    # Safely print the park_name and the highlights_in_fur_color or 'N/A'
    print(park_name, squirrels_by_park[park_name].get('highlights_in_fur_color', 'N/A'))
"""

# TASK 15

"""
# Use a for loop to iterate over the squirrels in Tompkins Square Park:
for squirrel in squirrels_by_park["Tompkins Square Park"]:
	# Safely print the activities of each squirrel or None
    print(squirrel.get("activities"))
    
# Print the list of 'Cinnamon' primary_fur_color squirrels in Union Square Park
print([squirrel for squirrel in squirrels_by_park["Union Square Park"] if squirrel["primary_fur_color"] == "Cinnamon"])
"""

# TASK 16

"""
# Print floats 1, 2, and 3
print(float1)
print(float2)
print(float3)

# Print floats 2 and 3 using the f string formatter
print(f"{float2:f}")
print(f"{float3:f}")

# Print float 3 with a 7 f string precision
print(f"{float3:.7f}")
"""

# TASK 17

"""
# Print the result of 2/1 and 1/2
print(2/1)
print(1/2)

# Print the floored division result of 2//1 and 1//2
print(2//1)
print(1//2)

# Print the type of 2/1 and 2//1
print(type(2/1))
print(type(2//1))
"""
# TASK 18

"""
# Create an empty list
my_list = []

# Check the truthiness of my_list
print(bool(my_list))

# Append the string 'cookies' to my_list
my_list.append('cookies')

# Check the truthiness of my_list
print(bool(my_list))
"""

# TASK 19

"""
# Use a for loop to iterate over the penguins list
for penguin in penguins:
  # Check the penguin entry for a body mass of more than 3300 grams
  if penguin["body_mass"] > 3300:
  	# Print the species and sex of the penguin if true
    print(f"{penguin['species']} - {penguin['sex']}")
"""

# TASK 20

"""
# Check the truthiness of penguin_305_details sex key
if penguin_305_details["sex"]:
	# If true, check if sex is True and store it as sex_is_true
    sex_is_true = penguin_305_details["sex"] is True
    # Print the sex key's value and sex_is_true
    print(f"{penguin_305_details['sex']}: {sex_is_true}")

# Check the truthiness of penguin_305_details tracked key
if penguin_305_details["tracked"]:
	# If true, check if tracked is True and store it as tracked_is_true
    tracked_is_true = penguin_305_details["tracked"] is True
    # Print the tracked key and tracked_is_true
    print(f"{penguin_305_details['tracked']}: {tracked_is_true}")
"""

# TASK 21

"""
# Use a list comprehension to iterate over each penguin in penguins saved as female_species_list
# If the the sex of the penguin is 'FEMALE', return the species value
female_species_list = [penguin["species"] for penguin in penguins if penguin["sex"] == 'FEMALE']

# Create a set using the female_species_list as female_penguin_species
female_penguin_species = set(female_species_list)

# Find the difference between female_penguin_species and male_penguin_species. Store the result as differences
differences = female_penguin_species.difference(male_penguin_species)

# Print the differences
print(differences)
"""

# TASK 22

"""
# Find the union: all_species
all_species = female_penguin_species.union(male_penguin_species)

# Print the count of names in all_species
print(len(all_species))

# Find the intersection: overlapping_species
overlapping_species = female_penguin_species.intersection(male_penguin_species)

# Print the count of species in overlapping_species
print(len(overlapping_species))
"""
