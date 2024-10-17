#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st
import pandas as pd
from streamlit_jupyter import StreamlitPatcher

# Patching Streamlit to work in Jupyter
StreamlitPatcher().jupyter()

# Función para cargar el archivo Excel y procesarlo
def process_excel(file):
    df = pd.read_excel(file)
    df['Suma'] = df.iloc[:, 0] + df.iloc[:, 1]
    return df

# Aplicación de Streamlit
st.title('Procesador de Excel')

uploaded_file = st.file_uploader("Elige un archivo Excel", type="xlsx")

if uploaded_file is not None:
    df = process_excel(uploaded_file)
    st.write(df)
    
    # Botón para descargar el archivo procesado
    processed_file = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Descargar archivo procesado",
        data=processed_file,
        file_name='archivo_procesado.csv',
        mime='text/csv',
    )

from streamlit_jupyter import StreamlitPatcher

StreamlitPatcher().jupyter()


# In[7]:





# In[ ]:




