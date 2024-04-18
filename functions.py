import streamlit as st
import json
import sqlite3


def read_json(filepath="list.json"):
    """
    Function read json data and return it in variable
    :param filepath:
    :return:
    """
    with open(filepath, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def write_to_json(new_list, filepath="list.json"):
    json_object = json.dumps(new_list, ensure_ascii=True)

    with open(filepath, "w") as outfile:
        outfile.write(json_object)


def add_product():
    product = st.session_state["new_todo"] + '\n'
    lista = read_json()
    lista.append(product)
    write_to_json(lista)
    st.session_state["new_todo"] = ''


def read_db_current():
    """
    Return items from current item list from db
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    cur.execute('select * from current_list')
    result = cur.fetchall()
    return result


def read_db_archive():
    """
    Return items from archive item list from db
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    cur.execute('select * from archive_items')
    result = cur.fetchall()
    return result


def add_item_db():
    item = st.session_state['new_todo']
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO current_list VALUES(?, 1)", item)
    conn.commit()
    st.session_state["new_todo"] = ''

