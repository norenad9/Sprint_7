#importamos librerias necesarias
import streamlit as st
import pandas as pd
import plotly 
#extraemos los datos del csv
car_data = pd.read_csv(r"C:\Users\pargu\OneDrive\Documentos\Py Projects\Sprint_7\vehicles_us.csv")
#ver de que dato hare el analisis, en este caso el año del modelo y el precio
#print(car_data.nunique())
#prueba de que los datos se extrajeron correctamente
#print (car_data.head())
header=st.header('Análisis de datos de anuncios de venta de coches')
# Crear un botón en la aplicación Streamlit
hist_button = st.checkbox('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['model_year'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Ventas de Año deModelos de Coches')
    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.checkbox('Gráfico de dispersión')

# Lógica a ejecutar cuando se hace clic en el botón
if disp_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de dispersión
    fig = go.Figure(data=[go.Scatter(x=car_data['model_year'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Ventas de Año de Modelos de Coches')
    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)