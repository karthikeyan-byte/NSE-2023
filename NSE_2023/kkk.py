import sqlite3
import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv("output.csv")

conn = sqlite3.connect("app.db")
df.to_sql("app", conn, if_exists="replace",index=False)

conn.commit()
conn.close()


def eight():
    # Connect to the SQLite database
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
    st.write(df1)
    st.bar_chart(df1.set_index('date')['turnover'])
    st.bar_chart(df1.set_index('date')['shares_traded'])
    
    conn.close()
    
    def nin():
        conn=sqlite3.connect("app.db")
        df.to_sql("app", conn, if_exists="replace",index=False)
    
        # Calculate the sum of turnover'
        date=df1['date'].unique()
        total_turnover = df1['turnover'].mean()
        total_shares_traded = df1['shares_traded'].mean()   

        # Display the sum of turnover in a separate table
        kk = pd.DataFrame({"date": [date],"Total Turnover": [total_turnover],
                        
                           "Total Shares Traded": [total_shares_traded]})
        
        kk.to_csv("fulloutput.csv", index=False)
        conn.commit()
        conn.close()
        
        return kk
    st.write(nin())
    return df1

df1=eight()

def save():
    if st.button("Load Data"):
        df = pd.read_csv("fulloutput.csv")

        conn = sqlite3.connect("channelinfo.db")
        df.to_sql("channelinfo", conn, if_exists="append",index=False)

        query="SELECT * FROM channelinfo"
        df1 = pd.read_sql_query(query, conn)
    
        conn.commit()
        conn.close()
    if st.button("clear"):
        conn = sqlite3.connect("channelinfo.db")
        conn.execute("DELETE FROM channelinfo")
        conn.commit()
        conn.close()
        
st.write(save())
  

def one():
    conn= sqlite3.connect("channelinfo.db")
    query ="SELECT * FROM channelinfo;"
    df=pd.read_sql_query(query, conn)
    return df
df1=one()
st.write(df1)
st.bar_chart(df1.set_index('date')['Total Turnover'])
st.bar_chart(df1.set_index('date')['Total Shares Traded'])
 
df=pd.DataFrame([open], columns=['open'], index=[1])  
source=pd.melt(df, id_vars=['model'])

chart=alt.Chart(source).mark_bar(strokeWidth=100).encode(
    x=alt.X('variable:N', title="", scale=alt.Scale(paddingOuter=0.5)),#paddingOuter - you can play with a space between 2 models 
    y='value:Q',
    color='variable:N',
    column=alt.Column('model:N', title="", spacing =0), #spacing =0 removes space between columns, column for can and st 
).properties( width = 300, height = 300, ).configure_header(labelOrient='bottom').configure_view(
    strokeOpacity=0)

st.altair_chart(chart) #, use_container_width=True)


  














 