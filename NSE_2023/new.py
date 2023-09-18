import sqlite3
import json
from datetime import datetime
import csv
import pandas as pd


# Connect to the database
conn = sqlite3.connect('app.db')
cursor = conn.cursor()

# Query the database (replace 'your_table' and 'your_columns' with your specific table and columns)
cursor.execute("SELECT * FROM app")
data = cursor.fetchall()

# Convert the data to a JSON format
json_data = []

# Function to convert date format
def convert_date_format(date_str):
    # Parse the date in the current format
    date_obj = datetime.strptime(date_str, "%d-%b-%Y")
    # Format the date in the desired format
    return date_obj.strftime("%Y-%m-%d")

for row in data:
    # Assuming your columns are named 'column1', 'column2', etc.
    record = {
        'id': row[0],
        'date': convert_date_format(row[1]),
        'open': row[2],
        'high': row[3],
        'low': row[4],
        'close': row[5],
        'shares_traded': row[6],
        'turnover':(row[7]),
        # Add more columns as needed
    }
    json_data.append(record)

# Close the database connection
conn.close()

# Save the JSON data to a file or do further processing
with open('output.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

input_file_path = 'output.json'
output_file_path = 'output.csv'

df = pd.read_json(input_file_path)
df.to_csv(output_file_path, index=False)      
