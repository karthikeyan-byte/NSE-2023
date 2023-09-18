import sqlite3
import pandas as pd
import datetime
import numpy as np


import pandas as pd

import pandas as pd

# Read the CSV file into a DataFrame
csv_file = 'nse.csv'
df = pd.read_csv(csv_file)

# Create a new 'id' column with unique values
df['id'] = range(1, len(df) + 1)

# Reorder the columns so that 'id' is the first column
columns = ['id'] + [col for col in df.columns if col != 'id']
df = df[columns]


df.to_csv(csv_file, index=False)  # Set index=False to avoid saving the DataFrame index



df = pd.read_csv("output.csv")

conn = sqlite3.connect("app.db")
df.to_sql("app", conn, if_exists="replace",index=False)

conn.commit()
conn.close()