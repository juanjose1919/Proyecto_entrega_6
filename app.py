import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title('Titulo')
st.header('Trabajo')


data = pd.read_csv('https://raw.githubusercontent.com/labeconometria/MLxE/main/proyectos2do/datasets3.csv')
pot = data['Potability'].value_counts()
pot.index = ['NO', 'SI']
fig, ax = plt.subplots(1,1)
ax.set_title('Proporción de potabilidad')
ax.bar(pot.index, pot.values, color = 'orange')

st.pyplot(fig)

