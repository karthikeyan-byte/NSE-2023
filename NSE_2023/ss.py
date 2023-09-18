import pandas as pd
import altair as alt
import streamlit as st

df = pd.DataFrame([['sst', '100', '1000'],['can','500','600']], columns=['model','0','1'])

#transform dataframe 
source=pd.melt(df, id_vars=['model'])

chart=alt.Chart(source).mark_bar(strokeWidth=100).encode(
    x=alt.X('variable:N', title="", scale=alt.Scale(paddingOuter=0.5)),#paddingOuter - you can play with a space between 2 models 
    y='value:Q',
    color='variable:N',
    column=alt.Column('model:N', title="", spacing =0), #spacing =0 removes space between columns, column for can and st 
).properties( width = 300, height = 300, ).configure_header(labelOrient='bottom').configure_view(
    strokeOpacity=0)

st.altair_chart(chart) #, use_container_width=True)
