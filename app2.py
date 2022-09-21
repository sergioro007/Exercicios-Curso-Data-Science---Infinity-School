import streamlit as st

st.title ("Cálculo do IMC")
peso = st.slider('Qual o peso do paciente?', 0, 130)
altura = st.slider('Qual a altura do paciente?', 0, 200)

altura = altura/100

imc = peso / altura ** 2

st.metric(label="Peso", value=peso)
st.metric(label="Altura", value=altura)
st.metric(label="IMC", value=imc)

if imc <= 18.5 :
    st.write ("Paciente está abaixo do peso normal")
elif imc <= 24.9 :
    st.write  ("Paciente está com peso normal")
elif imc <= 29.9 :
    st.write  ("Paciente está com sobrepeso")
elif imc <= 34.9 :
    st.write ("Paciente está com obesidade Classe I")
elif imc <= 39.9 :
    st.write ("Paciente está com obesidade Classe II")
else :
    st.write ("Paciente está com obesidade Classe III")

