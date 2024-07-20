"""" PRACTICE DELETE IN PYTHON
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[-4:-2]

# Print the updated list
print(areas)
"""

""" Currently, the first element in the areas_copy list is changed and the areas list is printed out.
 If you hit the run code button you'll see that, although you've changed areas_copy,
 the change also takes effect in the areas list. That's because areas and areas_copy point to the same list.
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas[:]   # or use this command: areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)