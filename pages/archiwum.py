import streamlit as st
from db_class import DbManager

db = DbManager()
lista = db.read_db_archive()

st.title('Poprzednie zakupy')

for index, product in enumerate(lista):
    st.text(f"{product[0]} data:{product[1]}")

st.button("Wyczyść liste", on_click=db.clear_archive, key='clear')
