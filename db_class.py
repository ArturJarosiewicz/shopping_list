import streamlit as st
import sqlite3
from datetime import datetime

class DbManager:

    def __init__(self):
        self.conn = sqlite3.connect('data.db', check_same_thread=False)
        self.cur = self.conn.cursor()

    def read_db_current(self):
        """
        Return items from current item list from db
        """
        self.cur.execute('select * from current_list')
        result = self.cur.fetchall()
        return result

    def read_db_archive(self):
        """
        Return items from archive item list from db
        """
        self.cur.execute('select * from archive_items')
        result = self.cur.fetchall()
        return result

    def add_item_db(self):
        item = st.session_state['new_todo']
        self.cur.execute("INSERT INTO current_list VALUES(?, 1)", (item, ))
        self.conn.commit()
        st.session_state["new_todo"] = ''

    def del_item(self, item_name_arg):
        self.cur.execute("DELETE FROM current_list WHERE item_name=?", (item_name_arg, ))
        self.conn.commit()

    def send_to_archive(self, item_name_arg):
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.cur.execute("INSERT INTO archive_items VALUES (?,?)", (item_name_arg, date))
        self.conn.commit()

    def clear_archive(self):
        self.cur.execute("DELETE FROM archive_items")
        self.conn.commit()

    def clear_current(self):
        self.cur.execute("DELETE FROM current_items")
        self.conn.commit()
