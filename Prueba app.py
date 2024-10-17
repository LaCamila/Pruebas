#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from io import BytesIO
from streamlit_jupyter import StreamlitPatcher

def app():
    st.title("Cargar Excel y Sumar Columnas")

    # Cargar archivo Excel
    uploaded_file = st.file_uploader("Cargar archivo Excel", type=["xlsx"])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("Datos cargados del Excel:", df)

        # Verificar que el DataFrame tenga al menos dos columnas
        if len(df.columns) >= 2:
            # Crear una nueva columna que sume las dos primeras columnas
            df['Suma'] = df.iloc[:, 0] + df.iloc[:, 1]
            st.write("DataFrame con la nueva columna 'Suma':", df)

            # Exportar resultados a Excel
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)
            output.seek(0)

            st.download_button(
                label="Descargar resultados",
                data=output,
                file_name="resultados.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.error("El archivo Excel debe tener al menos dos columnas.")

# Integrar Streamlit con Jupyter Notebook
StreamlitPatcher().jupyter()
app()

