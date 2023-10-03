import sqlite3
import streamlit as st
import pandas as pd
import altair as alt

# Load data from a CSV file and store it in an SQLite database
df = pd.read_csv("output.csv")
conn = sqlite3.connect("app.db")
df.to_sql("app", conn, if_exists="replace", index=False)
conn.commit()
conn.close()

# Define the main content of your Streamlit app
def main():
    st.title("Streamlit App with Manage App Feature")
    
    # Define a sidebar section for "Manage App" actions
    st.sidebar.header("Manage App")
    
    # Add options for managing the app (e.g., load data, clear data)
    if st.sidebar.button("Load Data"):
        load_data()
    
    if st.sidebar.button("Clear Data"):
        clear_data()
    
    # Display data and charts in the main content area
    df1 = eight()
    display_data_charts(df1)

# Function to load data into the app
def load_data():
    conn = sqlite3.connect("app.db")
    
    # Load data from a different CSV file (e.g., "new_data.csv") into the "app" table
    new_data = pd.read_csv("new_data.csv")
    new_data.to_sql("app", conn, if_exists="replace", index=False)
    
    conn.commit()
    conn.close()

# Function to clear data from the app
def clear_data():
    conn = sqlite3.connect("app.db")
    
    # Clear data from the "app" table by deleting all records
    conn.execute("DELETE FROM app")
    conn.commit()
    
    conn.close()

# Define the "eight()" function as you did in your original code
def eight():
    conn = sqlite3.connect("app.db")

    # Get user input for start and end dates
    sdate = st.date_input("Start Date")
    edate = st.date_input("End Date")

    # Use parameterized query to prevent SQL injection
    query = """
    SELECT DISTINCT date, open, high, low, close, shares_traded, turnover
    FROM app
    WHERE date BETWEEN ? AND ?
    """
    df1 = pd.read_sql_query(query, conn, params=(sdate, edate))
    
    conn.close()
    
    return df1

# Define a function to display data and charts
def display_data_charts(df):
    # Display data using st.write()
    st.write(df)
    
    # Display charts using st.bar_chart()
    st.bar_chart(df.set_index('date')['turnover'])
    st.bar_chart(df.set_index('date')['shares_traded'])

if __name__ == "__main__":
    main()
