#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# importando os modulos necessarios
import pygame, cPickle, thread, socket
from pygame.locals import *

# inicializando modulos da pygame
pygame.init()

# importando a classe Event, a base do controle de nosso cliente
from pygame.event import Event

# eventos definidos por voce!
GOTO = 24 # levar o seu personagem para posicao do evento
MESSAGE = 25 # mensagem para o cliente
SETOBJECT = 26 # colocar um objeto no mapa
SYSTEM = 27 # mensagem do sistema, provavelmente um erro
GETINFO = 28 # requisitar informacoes em um ponto do mapa

# IP e porta do servidor
DESTINY = ("coca.intermidia.icmc.usp.br", 5001)

# Largura e altura da tela em tiles, e tamanho do tile (40 pixels)
WIDTH, HEIGHT, TILE = 16, 11, 40

# pegar as coordenadas do centro da tela, em tiles
MIDDLE = WIDTH/2 - 1 , HEIGHT/2 - 1

# carregando mapa de tiles e de objetos (arvores, pedras e casas)
tilemap = cPickle.load(file('data/tilemap.txt', 'r'))
objmap = cPickle.load(file('data/objmap.txt', 'r'))

# enquanto running for verdadeiro seu jogo esta rodando
running = True

isCharSelected = False

# inicializa o clock (controle de frames)
clock = pygame.time.Clock()

# vetor de imagens de tiles e objetos, inicializando
tile, obj = [], []

# carregando todos
for i in range(24):
	tile += [pygame.image.load('imagens/tile%s.png'%i)]
	obj += [pygame.image.load('imagens/obj%s.png'%i)]
    
    
    
for i in range(24, 30):
	obj += [pygame.image.load('imagens/obj%s.png'%i)]
    
pos = (0,0)
#pos2 = (0, 0)

def handleIntro():
    global isCharSelected, running, pos
    for ev in pygame.event.get():
        if ev.type == QUIT:
            running = False
            isCharSelected = True
        elif ev.type == MOUSEBUTTONDOWN:
            pos = ev.pos[0], ev.pos[1]
            isCharSelected = True
        elif ev.type == MOUSEMOTION:
            pos = ev.pos[0], ev.pos[1]
            
screenIntro = pygame.display.set_mode((640,480))

while not isCharSelected:
    selectedId = 15
    handleIntro()
    fundo = pygame.image.load('imagens/fundo.png')
    screenIntro.blit(fundo, (0, 0))
    screenIntro.blit(obj[14], (50, 350))
    screenIntro.blit(obj[15], (150, 350))
    screenIntro.blit(obj[16], (250, 350))
    screenIntro.blit(obj[17], (350, 350))
    screenIntro.blit(obj[18], (450, 350))
    screenIntro.blit(obj[19], (550, 350))
    pygame.display.flip()
    
    if pos[0] in range(50, 90) and pos[1] in range(350, 390):
        screenIntro.blit(obj[24], (50, 350))
        pygame.display.flip()
        selectedId = 14
    elif pos[0] in range(150, 190) and pos[1] in range(350, 390):
        screenIntro.blit(obj[25], (150, 350))
        pygame.display.flip()
        selectedId = 15
    elif pos[0] in range(250, 290) and pos[1] in range(350, 390):
        screenIntro.blit(obj[26], (250, 350))
        pygame.display.flip()
        selectedId = 16
    elif pos[0] in range(350, 390) and pos[1] in range(350, 390):
        screenIntro.blit(obj[27], (350, 350))
        pygame.display.flip()
        selectedId = 17
    elif pos[0] in range(450, 490) and pos[1] in range(350, 390):
        screenIntro.blit(obj[28], (450, 350))
        pygame.display.flip()
        selectedId = 18
    elif pos[0] in range(550, 590) and pos[1] in range(350, 390):
        screenIntro.blit(obj[29], (550, 350))
        pygame.display.flip()
        selectedId = 19
    else:
        isCharSelected = 0
    
    MYID = Event(SYSTEM, {'id': selectedId, 'name': 'Roederick'})


if isCharSelected == True:
    screen = pygame.display.set_mode((640,480))

# renderizador de textos na tela
font = pygame.font.SysFont("default", 16)
def settext(msg):
    global text
    # deve ser uma surface na parte debaixo da tela, com 40 pixels (tamanho de um tile)
    text = pygame.Surface((640, 40))
    text.blit(font.render(msg, True, (255,255,255)), (5,12))

# inicializar text
settext("")

# variaveis de deslocamento da tela
slide_x = 0
slide_y = 0

# funcao goto move a ''tela''
def goto(x, y):
    global slide_x, slide_y
    slide_x = x - MIDDLE[0]
    slide_y = y - MIDDLE[1]
    pygame.display.set_caption("MMORPG Client - Pos: %2d, %2d"%(x, y))

# funcao move movimenta o personagem, nesse caso envia para o servidor processar o movimento
def move((inc_x, inc_y)):
    # se realmente houve um movimento
    if inc_x != 0 or inc_y != 0:
        e = Event(GOTO, {'x': slide_x + inc_x + MIDDLE[0], 'y': slide_y + inc_y + MIDDLE[1]})
        send(str(e))

# a funcao que 'escuta' o servidor
def listener():
    while running:
        # espera vir uma mensagem. Quando vem, trata-a tentando postar como evento, caso contrario imprime na tela.
        msg = conn.recv(999999)
        if msg != "":
            try:
                for m in eval(msg):
                    pygame.event.post(m)
            except:

                print "Servidor: ",msg

# enviar um evento para o servidor
def send(event):
    conn.send(str(event))

# criando uma conexao TCP
conn = socket.socket()
# conectando com o destino
conn.connect(DESTINY)
thread.start_new_thread(listener, tuple())

# enviar apresentacao - actor, name
conn.send(str(MYID))

# movimentacao e eventos
MOVES = {
    K_RIGHT: ( 1, 0),
    K_LEFT : (-1, 0),
    K_UP   : ( 0,-1),
    K_DOWN : ( 0, 1)
}

moving = (0,0)

# tratar os eventos localmente
def handle():
    global running, moving
    for e in pygame.event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key in MOVES.keys():
                moving = (moving[0] + MOVES[e.key][0], moving[1] + MOVES[e.key][1]) 
        elif e.type == KEYUP:
            if e.key in MOVES.keys():
                moving = (moving[0] - MOVES[e.key][0], moving[1] - MOVES[e.key][1])
                
        elif e.type == MOUSEBUTTONDOWN:
            pos = slide_x + e.pos[0]/TILE, slide_y + e.pos[1]/TILE
            send(Event(GETINFO, {'pos':pos}))
            
        elif e.type == GOTO:
            goto(e.x, e.y)
        elif e.type == MESSAGE:
            settext(e.msg)
        elif e.type == SYSTEM:
            print e.msg
        elif e.type == SETOBJECT:
            objmap[e.y][e.x] = e.obj


#loop principal:
while running:
    # limitando a 7 quadros por segundo no maximo
    clock.tick(7)
    # tratar eventos da pygame
    handle()
    # movimentar tela e personagem
    move(moving)
    
    # renderizar a tela
    for y in range(HEIGHT):
        for x in range(WIDTH):
            i,j = (slide_x+x,slide_y+y)
            screen.blit(tile[tilemap[j][i]], (x*TILE, y*TILE))
    for y in range(-6,HEIGHT):
        for x in range(-4,WIDTH):
            i, j = (x+slide_x,slide_y+y)
            if objmap[j][i] < 24:
                screen.blit(obj[objmap[j][i]], (x*TILE, y*TILE))
    screen.blit(text, (0,440))
    pygame.display.flip()

# enviar despedida
conn.send("bye bye")
conn.close()
