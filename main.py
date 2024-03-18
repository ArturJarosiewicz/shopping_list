import streamlit as st
import functions


lista = functions.read_json()

st.title('Lista zakupów')

for index, product in enumerate(lista):
    checkbox = st.checkbox(product, key=product)
    if checkbox:
        lista.pop(index)
        functions.write_to_json(lista)
        del st.session_state[product]
        st.experimental_rerun()

st.text_input(label='Wpisz produkt', on_change=functions.add_product, key='new_todo')


st.session_state