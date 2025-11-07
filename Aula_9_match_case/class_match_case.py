import timeit

# numero = int(input('Digite um número: '))
# match numero:
#     case 1:
#         (print(f'você digitou o número: {numero}'))
#     case 2:
#         (print(f'você digitou o número: {numero}'))
#     case 3:
#         (print(f'você digitou o número: {numero}'))
#     case 4:
#         (print(f'você digitou o número: {numero}'))
#     case 5:
#         (print(f'você digitou o número: {numero}'))
#     case _: # equivalente ao else
#         (print(f'você não digitou nenhum número entre 1 a 5: {numero}'))

# ***1: Verificando se o número é par ou ímpar***

# keep_playing = True
# # print('Pressione CTRL+C para sair do jogo a qualquer momento')
# while keep_playing:
#     numero = input('Digite um número para jogar o SAIR para sair do jogo: ')
#     match numero:
#         case 'SAIR':
#             print('saindo do jogo')
#             break
#         case 'sair':
#             print('saindo do jogo')
#             break
#         case numero if int(numero) % 2 == 0:
#             print('par')
#         case _:
#             print('ímpar')
        

# ***2: Verificando se um número é positivo, negativo ou zero***
# keep_playing = True
# # print('Pressione CTRL+C para sair do jogo a qualquer momento')
# while keep_playing:
#     numero = input('Digite um número para jogar o SAIR para sair do jogo: ')
#     match numero:
#         case 'SAIR':
#             print('saindo do jogo')
#             break
#         case 'sair':
#             print('saindo do jogo')
#             break
#         case numero if int(numero) > 0:
#             print('o número é positivo')
#         case numero if int(numero) < 0:
#             print('o número é negativo')
#         case _:
#             print('O número é igual à ZERO/0.')

# ***3: Verificando se uma string é vazia ou não***
# keep_playing = True
# while keep_playing:
#     word = input('please, type a word, hit ENTER for no string or STOP to leave the game: ')
#     word_length = len(word)
#     match word:
#         case 'LEAVE':
#             print('saindo do jogo')
#             break
#         case 'leave':
#             print('saindo do jogo')
#             break
#         case word if word_length <= 0 or word.isdigit():
#             print('you either entered an empty string or a number')
#         case _:
#             print('you entered a valid word')


# ***4: Verificando se um número é maior, menor ou igual a 10***
keep_playing = True
while keep_playing:
    number = int(input('Enter a number to compare with 10 or STOP to leave the game: '))
    match number:
        case number if number == 'STOP' or number == 'stop':
            break
        case number if number > 10:
            print(f'The number {number} is greater than 10')
        case number if number < 10:
            print(f'The number {number} is smaller than 10')
        case _:
            print(f'The number {number} is 10/TEN.')


# ***5: Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)***
