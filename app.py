import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados
st.header('Preços de Carro')
hist_button = st.button('Criar histograma') # criar um botão

if hist_button:
    st.write ('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram (car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
fig = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão
fig.show() # exibindo
