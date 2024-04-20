import streamlit as st
from db_class import DbManager

db = DbManager()
lista = db.read_db_current()
print(lista)

st.title('Lista zakupów')

# column1, column2 = st.columns(2)

for index, product in enumerate(lista):
    checkbox = st.checkbox(product[0], key=product[0])
    if checkbox:
        db.send_to_archive(product[0])
        db.del_item(product[0])
        st.rerun()

st.text_input(label='Wpisz produkt', on_change=db.add_item_db, key='new_todo')

st.button("Wyczyść liste", on_click=db.clear_current, key='clean_current')

# st.session_state
