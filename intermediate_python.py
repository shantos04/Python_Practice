# TASK 1

"""
# Import pandas as pd
import pandas as pd

# Convert sales to a pandas DataFrame
sales_df = pd.DataFrame(sales)

# Preview the first five rows
print(sales_df.head())
"""

# TASK 2

"""
import pandas as pd

# Read in sales.csv
sales_df = pd.read_csv("sales.csv")
print(sales_df)

# Print the mean order_value
print(sales_df["order_value"].mean())

# Print the total value of sales
print(sales_df["order_value"].sum())
"""

# TASK 3

"""
# Create the clean_string function
def clean_string(text):
  
  # Replace spaces with underscores
  no_spaces = text.replace(" ", "_")
  
  # Convert to lowercase
  clean_text = no_spaces.lower()
  
  # Display the final text as an output
  return clean_text

converted_text = clean_string("I LoVe dATaCamP!")
print(converted_text)
"""

# TASK 4 

"""
password = "not_very_secure_2023"

# Define the password_checker function
def password_checker(submission):
  
  # Check that the password variable and the submission match
  if password == submission:
    print("Successful login!")
  
  # Otherwise, print "Incorrect password"
  else:
    print("Incorrect password")

# Call the function    
password_checker("NOT_VERY_SECURE_2023")
"""

# TASK 5

"""
# Create a custom function
def average(values, rounded = False):
    if rounded == True:
        average_value = sum(values) / len(values)
        rounded_average = round(average_value, 2)
        return rounded_average
    else:
        average_value = sum(values) / len(values)
        return average_value
"""

# TASK 6

"""
# Define clean_text
def clean_text(text, lower = True):
  if lower == False:
    clean_text = text.replace(" ", "_")
    return clean_text
  else:
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
    return clean_text
"""

# TASK 7

"""
# Create the convert_data_structure function
def convert_data_structure(data, data_type = "list"):
  
  # If data_type is "tuple"
  if data_type == "tuple":
    data = tuple(data)
  
  # Else if data_type is set, convert to a set
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

# Call the function to convert to a set
result_set = convert_data_structure({"a", 1, "b", 2, "c", 3}, data_type="set")
print(type(result_set))
"""

# TASK 8

"""
def clean_string(text):
  
  # Add a single-line docstring
    swap spaces to underscores and convert text to lowercase.
  
  no_spaces = text.replace(" ", "_")
  clean_text = no_spaces.lower()
  return clean_text

# Access the docstring
print(clean_string.__doc__)
"""

# TASK 9

"""
# Create the convert_data_type function
def convert_data_structure(data, data_type="list"):
  # Add a multi-line docstring

  Convert a data structure to a list, tuple, or set.
  
  Args:
  	data (list, tuple, or set): A data structure to be converted.
    data_type (str): String representing the type of structure to convert data to.
    
  Returns:
  	data (list, tuple, or set): Converted data structure.
  
  if data_type == "tuple":
    data = tuple(data)
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

print(help(convert_data_structure))
"""

# TASK 10

"""
# Define a function called concat
def concat(*args):
  
  # Create an empty string
  result = ''
  
  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))
"""

# TASK 11

"""
# Define a function called concat
def concat(**kwargs):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(concat(start = "Python", middle = "is", end = "great!"))
"""
# TASK 12

"""
sale_price = 29.99

# Define a lambda function called add_tax
add_tax = lambda x: x * 1.2

# Call the lambda function
print(add_tax(sale_price))

sale_price = 29.99
"""

# TASK 13

"""
import string

# Call a lambda function adding 20% to sale_price
names = ["john", "xuong"]
capitalize_name = map(lambda x: x.capitalize(), names)

print(capitalize_name)
"""

# TASK 14

"""
sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
add_taxes = map(lambda x: x * 1.2, sales_prices)

# Use add_taxes to return a new list with updated values
print(list(add_taxes))
"""

# TASK 15

"""
def snake_case(text):
  # Attempt to clean the text
  try:
    # Swap spaces for underscores
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  # Run this code if an error occurs
  except:
    print("The snake_case() function expects a string as an argument, please check the data type provided.")

snake_case("User Name 187")

def snake_case(text):
  # Check the data type
  if type(text) == str:
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The snake_case() function expects a string as an argument, please check the data type provided.")

snake_case("User Name 187")
"""

