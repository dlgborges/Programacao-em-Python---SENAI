# ## Exercícios com funções:

# variáveis locais, globais e parâmetros

# ***1***
# ***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***
# def compare_numbers():
#     try:
#         number_one = int(input('Type the first number to compare: '))
#         number_two = int(input('Type the first number to compare: '))

#         if number_one > number_two:
#             print('The first number is greater than the second')
#         elif number_one < number_two:
#             print('The first number is smaller than the second')
#         else:
#             print('The first and second numbers are equal')                
#     except ValueError as error:
#         print('Exception: ', error)

# keep_playing = True
# while keep_playing:
#     compare_numbers()
#     if input('Type ENTER to compare more numbers or STOP to leave the game') == 'STOP':
#         keep_playing = False


# # ***2***
# # ***CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***
# def multiply_numbers(num_1, num_2, num_3):
#         return num_1 * num_2 * num_3

# keep_playing = True
# while keep_playing:
#     number_1 = int(input('Enter the first number to be multiplied: '))
#     number_2 = int(input('Enter the second number to be multiplied: '))
#     number_3 = int(input('Enter the third number to be multiplied: '))
#     print('The result of the multiplication is equals to: ', multiply_numbers(number_1, number_2, number_3))
#     if input('Hit ENTER to keep multiplying more numbers or type STOP to leave the game') == 'STOP':
#         keep_playing = False


# ***3***
# ***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***
# def number_to_power(base_number, power):
#     return pow(base_number, power) #number ** power
# print('The result of number to power is equals to:', number_to_power(10, 3))


# # ***4***
# # ***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.***
# age_number  = int(input('Digite sua idade: '))

# def print_special_message(age_number):
#     match age_number:
#         case 18:
#             print('Parabéns, já pode ser preso.')
#         case _ :
#             pass

# print_special_message(age_number)


# ***5***
# ***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***
# from datetime import datetime

# year_of_birth = int(input('Type the year you were born in: '))

# def find_out_age(year_of_birth):
#     current_year = datetime.now().year
#     users_age = current_year - year_of_birth
#     print(f'You are {users_age} old')

# find_out_age(year_of_birth)

# ***6***
# ***DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.***
# year_to_check = int(input('Type the year you want to check whether Brazil\'s national soccer team won the World Cup: '))

# def find_out_year_team_champion(year_to_check):
#     years_brazil_won_world_cup = [1958, 1962, 1970, 1994, 2002]
#     print(f'Indeed, Brazil\'s national soccer team won the World Cup in:', year_to_check) if year_to_check in years_brazil_won_world_cup else print(f'No, Brazil\'s national soccer team didn\'t win the world cup in:', year_to_check)

# find_out_year_team_champion(year_to_check)

# ***7*** 
# ***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***  
customer_name = input('Hello! Welcome to Dash\'s restaurant!\n\nPlease, inform your name: ')

# ***1 - Função -  cumprimentar o cliente***
def greet_customer(customer_name):
    print(f'{customer_name}, it\'s a pleasure to serve you!')

# ***2 - Função - restaurante***


def _get_menu():
    menu = ['Salad', 'Pasta', 'Sandwich', 'Ice Cream']
    return menu


def _menu_choice():
    choice = input('Please, let me know your order: ')
    return choice

def 

def restaurant():
    menu = _get_menu()
    print('Here\'s our menu: ', menu)

    choice = _menu_choice()
    print(f'Order successful! We\'re preparing your {choice}') if choice in menu else print(f'Sorry! {choice} is not in our menu.')
    
    while True:
        choice = input('Type MENU to view the menu again or STOP to leave the system: ')
        match choice:
            case 'MENU':
                restaurant()
            case 'STOP':
                print('Thank you for ordering with us today!')
            case _:
                print('Invalid option!')
                


# ***3 - Sugestão utilize listas  e loops***

greet_customer(customer_name)
restaurant()