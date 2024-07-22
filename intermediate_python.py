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