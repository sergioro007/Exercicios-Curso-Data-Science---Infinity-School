import streamlit as st

st.title ("Calculadora de Adição")

number1 = st.number_input('Digite o primeiro número: ')
number2 = st.number_input('Digite o segundo número: ')

st.write("Resultado:")
st.write(number1, " + ", number2, " = ", number1+number2   )
st.write("")
st.write("OU")
st.write(number1)
st.write(number2, " + ")
st.write(number1+number2, " = ")