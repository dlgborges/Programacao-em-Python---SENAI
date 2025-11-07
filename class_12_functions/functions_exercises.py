# ## Exercícios com funções:

# variáveis locais, globais e parâmetros

# ***1***
# ***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***
def compare_numbers():
    try:
        number_one = int(input('Type the first number to compare: '))
        number_two = int(input('Type the first number to compare: '))

        if number_one > number_two:
            print('The first number is greater than the second')
        elif number_one < number_two:
            print('The first number is smaller than the second')
        else:
            print('The first and second numbers are equal')                
    except ValueError as error:
        print('Exception: ', error)

keep_playing = True
while keep_playing:
    compare_numbers()
    if input('Type ENTER to compare more numbers or STOP to leave the game') == 'STOP':
        keep_playing = False


# ***2***
# ***CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***
def multiply_numbers(num_1, num_2, num_3):
    



# ***3***
# ***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***

# ***4***

# ***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.***

# ***5***

# ***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***

# ***6***

# ***DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.***

# ***7*** 

# ***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***  

# ***1 - Função -  cumprimentar o cliente***

# ***2 - Função - restaurante***

# ***3 - Sugestão utilize listas  e loops***