import streamlit as st
import json


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
