import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as cttk
from .class_18_sw_development_tkinter.customer_management_system import field_with_box_same_row

def connect():
    return sqlite3.connect('C:/Users/Aluno/Downloads/Programacao-em-Python---SENAI/class_19_db/db_system.db')

def create_table():
    conn = connect()
    c = conn.cursor()
    c.execute(f'''CREATE TABLE IF NOT EXISTS users(
            cpf TEXT,
            nome TEXT,
            email TEXT
              )
              ''')
    conn.commit()
    conn.close()

def user_insert(username):
    pass

def user_show(username):
    pass

def user_update(username):
    pass

def user_delete(username):
    pass

#UI
#grid

#create window
window = tk.Tk()

window.geometry('800x630')
window.title('CRUD - FORM')

icon_path = 'C:/Users/Aluno/Downloads/Programacao-em-Python---SENAI/class_19_db/icons/forms-google-data.ico'
window.iconbitmap(icon_path)

name_field, name_field_box = field_with_box_same_row('Nome', 1, 1)
cpf_field, cpf_field_box = field_with_box_same_row('CPF', 2, 1)
email_field, email_field_box = field_with_box_same_row('Email', 3, 1)


window.mainloop()

