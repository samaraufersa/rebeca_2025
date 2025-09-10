import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="DashCovid",
    layout="wide")

st.title("DASHCOVID: Um Dashboard sobre os Dados de COVID-19 - 2020")

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

df_brasil_eua = df.query('Country == "Brazil" or Country == "United States of America"')
fig2 = px.line(df_brasil_eua,
        x = 'Date_reported',
        y = 'Cumulative_cases',
        color = 'Country',
        title = 'Número de Casos Acumulados por COVID - Brasil x EUA')
fig2.update_layout(xaxis_title = 'Data', yaxis_title = 'Número de Casos Acumulados')
fig2.show()

st.plotly_chart(fig2, use_container_width=True)

df_brasil_eua_india = df.query('Country == "Brazil" or Country == "United States of America" or Country == "India"')
fig3 = px.pie(df_brasil_eua_india,
        values = 'Cumulative_cases',
        names = 'Country',
        title = 'Número de Casos Acumulados por COVID - Brasil x EUA x India')
fig3.show()

st.plotly_chart(fig3, use_container_width=True)

