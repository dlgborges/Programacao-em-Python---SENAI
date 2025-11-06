# 1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.

# number = 0

# while number <= 1000:
#     print(number)
#     number += 1 


# 2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

# usernames = []

# while len(usernames) < 10:
#     usernames.append(input('Insira o nome do novo usuário: '))
#     print(usernames)

# print(usernames)

## 

## Crie um sistema de notas alunos, com as seguintes operações:
# ***Utilize While ou for***

#  **Sistema de notas de alunos**

# - ***Visão do professor***

# - Acesso a conta com condicionais

# - 3 chances de acessar o sistema
# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
for i in range(3):
    print(i)

usernames = []
usernames.append(input('Digite o nome do usuário a cadastrar: '))
users_passwords = []
users_passwords.append(input('Digite a senha do usuário: '))

print('Página de login do sistema de Notas dos Alunos - Visão do Professor')

login_user = input('Digite o nome do usuário: ')
login_user_password = input('Digite a senha do usuário: ')
chances = 3

usernames.index(login_user)

for n in range(1, chances):
    print(chances)
    if (login_user in usernames) and (login_user_password == users_passwords[usernames.index(login_user)]):
        print('Bem-vindo ao sistema de Notas dos Alunos - Visão do Professor')

        # - Inserir notas (se Senha correta)
        print('Agora, vamos inserir as notas dos alunos no sistema:')

        more_grades = input('Digite SAIR quando não tiver mais notas a inserir.Pressione qualquer tecla para continuar.')
        students_grades = []
        #leave = input('Digite SAIR quando não tiver mais notas a inserir.Pressione qualquer tecla para continuar.')
        while more_grades != 'SAIR':
            students_grades.append(int(input('Insira a nota do aluno:')))
            more_grades = input('Você quer adicionar mais notas?\nSe sim, pressione qualquer tecla para continuar. Caso contrário, digite SAIR')
        break
    else:
        chances -= 1
        print(f'Você errou o nome do usuário, senha ou os dois.\nVocê tem mais {chances} chances.')
        login_user = input('Digite o nome do usuário: ')
        login_user_password = input('Digite a senha do usuário: ')
    print('Usuário bloqueado. Entre em contato com o depto. de segurança.')

# - Fazer a média
media = sum(students_grades) / len(students_grades)
print('A média da nota dos alunos é: ', media)

# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***

# ***IMPORTANTE:***

# - Ao finalizar o código, insira na borda do script, no última linha:

# input(’Digite enter para sair’)