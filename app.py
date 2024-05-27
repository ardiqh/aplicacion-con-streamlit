import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Aplicación de Análisis de Datos')

# Lectura de datos
st.sidebar.header('Cargar datos')
uploaded_file = st.sidebar.file_uploader('Sube un archivo CSV', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Resumen de datos
    st.header('Resumen de Datos')
    st.write(df.describe())

    # Visualización de datos
    st.header('Visualización de Datos')
    st.subheader('Gráfico de Dispersión')
    st.write('Selecciona las variables para el gráfico de dispersión')

    # Filtrar solo columnas numéricas
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    if len(numeric_columns) < 2:
        st.write("El archivo CSV debe contener al menos dos columnas numéricas.")
    else:
        x_axis = st.selectbox('Variable en el eje X', numeric_columns)
        y_axis = st.selectbox('Variable en el eje Y', numeric_columns)

        fig, ax = plt.subplots()
        ax.scatter(df[x_axis], df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        st.pyplot(fig)

        # Técnica estadística: Correlación
        st.header('Técnica Estadística: Correlación')
        if st.checkbox('Mostrar matriz de correlación'):
            corr_matrix = df[numeric_columns].corr()
            st.write(corr_matrix)

            st.subheader('Mapa de calor de la matriz de correlación')
            fig, ax = plt.subplots()
            cax = ax.matshow(corr_matrix, cmap='coolwarm')
            fig.colorbar(cax)
            plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
            plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
            st.pyplot(fig)
else:
    st.write('Por favor, sube un archivo CSV para empezar.')
