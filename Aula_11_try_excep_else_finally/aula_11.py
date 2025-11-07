# try:
#     n = 1/0
#     print(a)
# except ZeroDivisionError as error:
#     print(error)
# except SyntaxError as error:
#     print(error)
# finally:
#     print('Reached the end of the try except')


# Atividades para trabalhar com try and except

# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.
# try:
#     numero = int(input('Digite um numero inteiro'))
# except ValueError as error:
#     print(error)

# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.
# try:
#     division = int(input('please, enter a number: ')) / int(input('please, enter another number: '))
# except ZeroDivisionError as error:
#     print(error)
# else:
#     print(int(division))


# Exercício 3:
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

lista = [1,2,3]
    
try:
    print(lista[3])
except IndexError as error:
    print(error)