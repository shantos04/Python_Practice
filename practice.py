# TASK 1
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

# TASK 2

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

#TASK 3

"""
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas[:]   # or use this command: areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
"""

# TASK 4

"""
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
"""

# TASK 5

"""
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)
"""

# TASK 6

"""
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)


# Print out the number of o's in place
print(place.count("o"))
"""

# TASK 7

"""
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))
"""

# TASK 8

"""
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)


# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
"""

# TASK 9

"""
import numpy as np

fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

fam_ext = fam + ["me", 1.79]

print(str(len(fam_ext)) + " elements in fam_ext")

np_fam = np.array(fam_ext)

"""

# TASK 10

"""
# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
"""

# TASK 11

"""
# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))
"""

# TASK 12

"""
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])

np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

bmi = np_weight / np_height ** 2

print(bmi)
print(bmi > 21)
"""

# TASK 13

"""
# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
"""

# TASK 14

"""
# Import numpy, Create height_in
import numpy as np
height_in = [74, 74, 72, 75, 76, 73]

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)
"""

# TASK 15

"""
import numpy as np 

np_test = np.array([True, 1, 2]) + np.array([3, 4, False])
print(np_test)
"""

# TASK 16

"""

import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
"""

# TASK 17

"""
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49, :])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np.array(np_baseball[:, 1])

# Print out height of 124th player
print(np_baseball[123, 0])
"""

# TASK 18

"""
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np.array(np_baseball[:, 0])

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))
"""