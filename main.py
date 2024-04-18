import streamlit as st
import functions

lista = functions.read_db_current()
print(lista)

st.title('Lista zakupów')

for index, product in enumerate(lista):
    checkbox = st.checkbox(product[0], key=product[0])
#   st.experimental_rerun()

st.text_input(label='Wpisz produkt', on_change=functions.add_item_db, key='new_todo')

st.session_state
