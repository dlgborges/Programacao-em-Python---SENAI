# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()



# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/




#atribuicao de valores inteiros a duas variaveis
largura, altura = 400, 400

#uso da biblioteca pygame, modulo display, metodo set_mode, que cria uma supefície (Surface) para que algo seja mostrado. Atribuído à uma variável para que superfície possa ser usada posteriormente
tela = pygame.display.set_mode((largura, altura))

#uso da biblioteca pygame, modulo display, metodo set_caption para modificar o título da janela onde está sendo executado o programa
pygame.display.set_caption("Labirinto")


# criacao de variáveis de cores utilizando tuplas com 3 valores cada, correspondentes aos valores RGB
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

#atribuindo do tamanho da celula 
tamanho_celula = 40

#atribuicao da variável 'labirinto', através de binário, usando listas dentro de outra lista. Cheio quando 1 e vazio quando 0 
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#atribuicao de valores, às variáveis de posicao x e y, através da multiplicacao da variavel tamanho da celula (atribuida mais acima) 
x, y = 1 * tamanho_celula, 1 * tamanho_celula

#atribuicao de velocidade igual ao tamanho da celula, ou seja, a cada 'passo' deslocamento de uma célula
velocidade = 40

# criacao de método para desenhar o labirinto (acima, o labirinto foi apenas definido como variavel. Agora, iremos desenhá-lo na tela)
def desenhar_labirinto():
    '''

    Paramenters: None
    Returns: None
    '''
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            cor = preto if labirinto[linha][coluna] == 1 else branco
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

#Loop para execucao contínua do jogo
# Começamos setando uma variável sempre verdadeira para que o loop/jogo permaneça ativo
executando = True

#Enquanto a variável for verdadeira e o usuário não clicar no X no canto superior direito da tela, o jogo/tela continua ativo
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    #leitura da(s) tecla(s) pressionada(s)
    #basicamente
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y

    # como a 'tela' retorna um objeto Surface, agora, utilizamos os métodos da classe Surface que foi atribuida à 'tela'
    # o método fill preenche a tela com a cor desejada. No caso, a cor branca, definida como variável mais acima
    tela.fill(branco)

    #chamada do método para desenhar o labirinto dentro da tela/superfície/Surface criada mais acima
    desenhar_labirinto()
    #desenho de um retângulo (vermelho) dentro da tela/superfície/Surface criada mais acima
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

    #método usado para atualizar a tela constantemente
    pygame.display.flip()

    # taxa de atualização de 10 quadros / segundo
    pygame.time.Clock().tick(10)

# uma vez que o usuário clica no X para fechar a janela, executando se torna False e o quit() é executado, descarregando o programa
pygame.quit()

