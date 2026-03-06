import pandas as pd
import plotly.graph_objects as go
import scipy.stats
import streamlit as st

df_vehicles = pd.read_csv(
    "F:/Users/Luis Alberto/Documents/Proyecto_S7/vehicles_us.csv")

st.header("Vehiculos")

hist_price_button = st.checkbox("Construir histograma del precio")

if hist_price_button:
    st.write(
        "Creación de un histograma para el precio del conjunto de datos de venta de coches")

    fig = go.Figure()

    fig.add_trace(
        go.Histogram(
            x=df_vehicles["price"],
            nbinsx=50
        )
    )

    fig.update_layout(
        title="Distribución del Precio de los Vehículos",
        xaxis_title="Precio",
        yaxis_title="Frecuencia"
    )

    st.plotly_chart(fig, use_container_width=True)

hist_odo_button = st.checkbox("Construir histograma del kilometraje")

if hist_odo_button:
    st.write(
        "Creación de un histograma para el kilometraje del conjunto de datos de venta de coches")

    fig = go.Figure()

    fig.add_trace(
        go.Histogram(
            x=df_vehicles["odometer"],
            nbinsx=50
        )
    )

    fig.update_layout(
        title="Distribución del Kilometraje",
        xaxis_title="Kilometraje",
        yaxis_title="Frecuencia"
    )

    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button(
    "Construir un gráfico de dispersión entre el precio y el kilometraje")

if scatter_button:
    st.write("Creación de grafico de dispersión Precio VS Kilometraje")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df_vehicles["odometer"],
            y=df_vehicles["price"],
            mode="markers"
        )
    )

    fig.update_layout(
        title="Relación entre Precio y Kilometraje",
        xaxis_title="Kilometraje",
        yaxis_title="Precio"
    )

    st.plotly_chart(fig, use_container_width=True)
