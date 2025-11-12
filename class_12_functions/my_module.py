def market_(list_prod, list_values):
    carrinho = []
    meus_valores = []
    per = input('Ready to order? ')
    index = 0
    while per != 'no':
        produto = int(input(f'''
                1 - {list_prod[index+1]} - R$ {list_values[index+1]}
                2 - {list_prod[index+2]} - R$ {list_values[index+2]}
                3 - {list_prod[index+3]} - R$ {list_values[index+3]}
                4 - {list_prod[index+4]} - R$ {list_values[index+4]}
                5 - {list_prod[index+5]} - R$ {list_values[index+5]}:\n'''))
        carrinho.append(list_prod[produto])
        meus_valores.append(list_values[produto])
        print(carrinho)
        soma = sum(meus_valores)
        print('Total: ', soma)
        per = input('Press ENTER to continue OR \'no\' to proceed to the payment: ')
    else:
        print('Thanks, you\'re always welcome!')

def payments(forma_pag):
    print(forma_pag)
    escolha = int(input('Choose your preferred payment: '))
    print('You chose: ', forma_pag[escolha])

def farewell(nome):
    return f'Thanks, you\'re always welcome {nome}!'
