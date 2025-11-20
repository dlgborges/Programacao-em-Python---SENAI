import tkinter as tk

root = tk.Tk()

fields_names = ['Nome', 'Idade', 'Email', 'Endereço', 'Celular', 'CEP', 'Cidade', 'Cursos']

def field_with_box_generator(label_text, label_position_row, label_position_column, text_entry_box_row, text_entry_box_column):
    '''
    '''
    text = tk.Label(root, text=f'{label_text}: ')
    text.grid(row=label_position_row, column=label_position_column)

    text_entry_box = tk.Entry(root, width=10)
    text_entry_box.grid(row=text_entry_box_row, column=text_entry_box_column)
    return text, text_entry_box


def field_with_box_same_row(label_text, field_row, label_position_column):
    '''
    '''
    text = tk.Label(root, text=f'{label_text}: ')
    text.grid(row=field_row, column=label_position_column)

    text_entry_box = tk.Entry(root, width=10)
    text_entry_box.grid(row=field_row, column=label_position_column + 1)
    return text, text_entry_box


def fields_with_box_generator(fields_names):
    field_row = 1
    label_position_column = 1
    for field in fields_names:
        field_with_box_same_row(field, field_row, label_position_column)
        field_row += 1


def send():
    print_data.config(text=f'''
                      Nome: {name_field_box.get()}
                      Idade: {age_field_box.get()}
                      Email: {email_field_box.get()}
                      Endereço: {address_field_box.get()}
                      Celular: {cellphone_field_box.get()}
                      CEP: {postcode_field_box.get()}
                      Cidade: {city_field_box.get()}
                      Cursos: {courses_field_box.get()}''')


root.geometry('1700x750')
root.title('Sistema de Gerenciamento de Clientes - Dash Systems')

name_field, name_field_box = field_with_box_same_row('Nome', 1, 1)
age_field, age_field_box = field_with_box_same_row('Idade', 2, 1)
email_field, email_field_box = field_with_box_same_row('Email', 3, 1)
address_field, address_field_box = field_with_box_same_row('Endereço', 4, 1)
cellphone_field, cellphone_field_box = field_with_box_same_row('Celular', 5, 1)
postcode_field, postcode_field_box = field_with_box_same_row('CEP', 6, 1)
city_field, city_field_box = field_with_box_same_row('Cidade', 7, 1)
courses_field, courses_field_box = field_with_box_same_row('Cursos', 8, 1)

button = tk.Button(root, text='Enviar', width = 25, command=send)
button.grid(row=11, column=2, padx=10, pady=10)



print_data = tk.Label(root, text='Dados do cliente: ')
print_data.grid(row=12, column=2)

root.mainloop()
