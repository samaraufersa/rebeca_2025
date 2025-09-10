import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="DashCovid",
    layout="wide")

df = pd.read_csv('WHO_time_series.csv')

df['Date_reported'] = pd.to_datetime(df['Date_reported'])

fig1 = px.line(df,
        x = 'Date_reported',
        y = 'Cumulative_cases',
        color = 'Country',
        title = 'Número de Casos Acumulados por COVID')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Número de Casos Acumulados')
fig1.show()

st.plotly_chart(fig1, use_container_width=True)
