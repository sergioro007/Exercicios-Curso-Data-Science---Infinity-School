import streamlit as st

st.title('Sitema X')

nome = st.text_input('Digite seu nome: ')

if nome != "":
    st.write('Bem-vindo(a), ', nome)
else:
    st.write('')

