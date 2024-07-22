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