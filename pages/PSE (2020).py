import streamlit as st
import pandas as pd
import numpy as np
from plotly import express as px
from plotly import graph_objs as go

###### Páginal Inicial do Streamlit ######
st.set_page_config(layout= 'wide')

cols = st.columns(6, gap="large")
with cols[0]:
    st.image("images\Passos-magicos-icon-cor.png")
with cols[1]:
    if st.button("Home"):
        st.switch_page("home.py")
with cols[2]:
    if st.button("PSE (2020)"):
        st.switch_page("pages/PSE (2020).py")
with cols[3]:
    if st.button("Sobre"):
        st.switch_page("pages/MVP (sobre).py")
with cols[4]:
    if st.button("Referências"):
        st.switch_page("pages/Referências.py")

st.header("", divider="gray")

st.header(":mag_right: Pesquisa Sócio Econômica (2020)")

st.markdown("Em construção")

# Dados da atualização dos dados - Por enquanto apenas 2024, mas pode ser estendido para os próximos anos
# Create tabs
tab_titles = ['Metrics', 'Plot', 'Chart', 'Input']
tabs = st.tabs(tab_titles)
 
# Add content to each tab
with tabs[0]:
    st.header('Metrics')
    st.metric('Metric 1', 123)
    st.metric('Metric 2', 456)
 
with tabs[1]:
    st.header('Plot')

with tabs[2]:
    st.markdown("- Testando...")
    st.header('Chart')
 
with tabs[3]:
    st.header('Input')
    st.text_input('Enter some text')
    st.number_input('Enter a number')





# Ajustando parâmetros dos textos
    css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.5rem;
    font-weight:bold;
    }
    [data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)