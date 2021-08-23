"""
Helena's Quest - Um RPG em pygame
Este jogo foi inicialmente pensado e esboçado por Felipe Caetano em 2018.
2018 - criado o esboço inicial do game, suas classe e alguns objetos
2019 - nada
2020 - nada
2021 - Refactor do codigo e andamento do projeto.

Este jogo conta a história da Princesa Helena do Reino do Ikkathya e sua
busca para salvar o império de seu pai do terrivel mal que assolou o país.
Para isso ela precisa recuperar a magia antiga do reino perdida a muito tempo
guardadas nos lendários grimoars do poder.

"""
import sys
import pickle

import pygame
from system.battle.sistema_batalha import *
from helena import Helena
from mobs import *

#from pygame.locals import * #para importar todos os eventos
pygame.init()

# eventos definidos por voce!
NEWGAME = 14        # novo jogo
LOADGAME = 15       # carregar jogo salvo
CONFIGS = 16        # exibir configurações
CREDITS = 17        # exibir creditos
EXITGAME = 18       # sair do jogo
GOTO = 24           # levar o seu personagem para posicao do evento
MESSAGE = 25        # mensagem para o cliente
SETOBJECT = 26      # colocar um objeto no mapa
SYSTEM = 27         # mensagem do sistema, provavelmente um erro
GETINFO = 28        # requisitar informacoes em um ponto do mapa
GRIMOARCHANGE = 30  # trocar o grimoar
ATTACKMODE = 31     # modo de ataque
SHOWBAG = 32        # mostrar inventario
SHOWGRIMOARCHOOSE = 35  # abrir menu de troca de grimoar
WAITSKILLSELECT = 45 # esperando escolher skill

# DESTINY = ('127.0.0.1', 5000) # para conexão com servidor

WIDTH, HEIGHT, TILE = 32, 22, 40
MIDDLE = WIDTH//2 - 1, HEIGHT//2 - 1
slide_x = 0
slide_y = 0
#selectedId = 0
running = True
isOptionSelected = False
#isBattleOptionSelected = False
moving = 0, 0
moves = {
    pygame.K_RIGHT: (1, 0),
    pygame.K_LEFT:  (-1, 0),
    pygame.K_UP:    (0, -1),
    pygame.K_DOWN:  (0, 1)
    }

def handle_intro():
    """
    function handle_intro: Gerencia os controles durante a tela de menu
    :return: None
    """
    global isOptionSelected, running, pos
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game_quit()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            pos = ev.pos[0], ev.pos[1]
            isOptionSelected = True
        elif ev.type == pygame.MOUSEMOTION:
            pos = ev.pos[0], ev.pos[1]


def goto(x, y):
    global slide_x
    global slide_y
    slide_x = x - MIDDLE[0]
    slide_y = y - MIDDLE[1]
    pygame.display.set_caption("MMORPG Client - Pos: %2d, %2d" % (x, y))


def move(movingt):
    """
    Function move: Dispara o evento GOTO de acordo com as coordenadas x e y definadas
    :param movingt:
    :return:
    """
    global slide_x
    global slide_y
    global MIDDLE
    inc_x, inc_y = movingt
    if inc_x != 0 or inc_y != 0:
        e = pygame.event.Event(GOTO, {'x': slide_x + inc_x + MIDDLE[0], 'y': slide_y + inc_y + MIDDLE[1]})
        pygame.event.post(e)


def handle():
    """
    function handle: controla a tela de mapa de jogo
    :return:
    """
    global running, moving
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_quit()
        elif e.type == pygame.KEYDOWN:
            if e.key in moves.keys():
                moving = (moving[0] + moves[e.key][0], moving[1] + moves[e.key][1])
        elif e.type == pygame.KEYUP:
            if e.key in moves.keys():
                moving = (moving[0] - moves[e.key][0], moving[1] - moves[e.key][1])
        elif e.type == GOTO:
            goto(e.x, e.y)


def reder_exit():
    pygame.quit()
    sys.exit()


def render_credits():
    screenIntro = pygame.display.set_mode((640, 480))
    fundo = pygame.image.load('imagens/fundo.png')
    while True:
        handle_intro()
        screenIntro.blit(fundo, (0, 0))
        pygame.display.flip()


def handleBattle():
    """
    function handleBattle() : verifica os controles em tela de batalha
    :return:
    """
    global running, pos
    opbat_selected = False
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game_quit()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            pos = ev.pos[0], ev.pos[1]
            opbat_selected = True

        elif ev.type == pygame.MOUSEMOTION:
            pos = ev.pos[0], ev.pos[1]
            pygame.display.set_caption("MMORPG Client - Pos: %2d, %2d" % (ev.pos[0], ev.pos[1]))
            opbat_selected = False
        return opbat_selected


def game_quit():
    global running, isBattleOptionSelected, isOptionSelected
    running = False
    isBattleOptionSelected = True
    isOptionSelected = True
    pygame.quit()
    sys.exit()


def show_grimoarChoose(helena):
    pass


def battle_screen(helena, mob):
    """
    Function battle_screen: Renderiza e controla a tela de batalha
    :param helena:
    :param mob:
    :return:
    """

    fundo = pygame.image.load('imagens/battlebackground.png').convert_alpha()
    image_mob = pygame.image.load(mob._image).convert_alpha()
    mob_hp = pygame.image.load('imagens/hp.png').convert_alpha()
    mob_hp10 = pygame.image.load('imagens/hp10.png').convert_alpha()
    painel_mob = pygame.image.load("imagens/barra.png").convert_alpha()
    battleScreen = pygame.display.set_mode((800, 600))

    global screen, isBattleOptionSelected
    battle_end = False
    action = 0
    batalha = Battle(helena, mob)

    def wait_skill():
        isBattleOptionSelected = handleBattle()
        print("fiz a primeira checada mas...", isBattleOptionSelected)
        if pos[0] in range(620, 720) and pos[1] in range(484, 500):
            pygame.draw.rect(battleScreen, (255, 0, 0), [620, 486, 110, 18], 1)
            if isBattleOptionSelected:
                return helena.grimoar[0], 40    # @TODO: colocar na lista certa. Algo como skills
        elif pos[0] in range(620, 720) and pos[1] in range(509, 524):
            pygame.draw.rect(battleScreen, (180, 20, 83), [620, 507, 110, 18], 1)
            if isBattleOptionSelected:
                return helena.grimoar[1], 40
        elif pos[0] in range(620, 720) and pos[1] in range(531, 544):
            pygame.draw.rect(battleScreen, (180, 20, 83), [620, 530, 110, 18], 1)
            if isBattleOptionSelected:
                return helena.grimoar[2], 40
        elif pos[0] in range(620, 720) and pos[1] in range(553, 570):
            pygame.draw.rect(battleScreen, (180, 20, 83), [620, 554, 110, 18], 1)
            if isBattleOptionSelected:
                return helena.grimoar[3], 40

    while not battle_end:
        isBattleOptionSelected = handleBattle()
        font = pygame.font.SysFont('maturascriptcapitals', 18)
        battleScreen.blit(fundo, (0, 0))
        for i, sk in enumerate(helena.grimoars):
            battleScreen.blit(font.render(sk, True, (255, 128, 64)), (620, 480+23*i))
        battleScreen.blit(image_mob, (530, 20))
        # battleScreen.blit(painel_mob, (530, 270))
        settext(mob.name+' - lvl: '+str(mob.level), painel_mob)
        battleScreen.blit(text, (460, 270))
        battleScreen.blit(mob_hp, (465, 327))
        battleScreen.blit(mob_hp10, (453, 316))

        if pos[0] in range(76, 190) and pos[1] in range(484, 500):
            pygame.draw.rect(battleScreen, (255, 0, 0), [76, 484, 120, 18], 1)
            selectedId = GRIMOARCHANGE
            if isBattleOptionSelected:
                action = batalha.select_action(selectedId)
        elif pos[0] in range(76, 146) and pos[1] in range(509, 524):
            pygame.draw.rect(battleScreen, (255, 0, 0), [76, 507, 110, 18], 1)
            selectedId = ATTACKMODE
            if isBattleOptionSelected:
                action = batalha.select_action(selectedId)
        elif pos[0] in range(76, 168) and pos[1] in range(531, 544):
            pygame.draw.rect(battleScreen, (255, 0, 0), [74, 530, 110, 18], 1)
            selectedId = 32
            if isBattleOptionSelected:
                action = batalha.select_action(selectedId)
        elif pos[0] in range(76, 150) and pos[1] in range(553, 570):
            pygame.draw.rect(battleScreen, (255, 0, 0), [76, 554, 110, 18], 1)
            selectedId = 33
            if isBattleOptionSelected:
                action = batalha.select_action(selectedId)

        if action:
            if action == 35:        # show grimoar choose
                show_grimoarChoose(helena)
            if action == 45:        # wait for skill select
                isBattleOptionSelected = True
                skillselected = wait_skill()
                batalha.select_skill(skillselected)

        pygame.display.flip()

    # if pos[0] in range(195, 445) and pos[1] in range(90, 154):
    #         battleScreen.blit(painel_mob, (195, 90))
    #         pygame.display.flip()
    #         selectedId = 14
    #
    #     elif pos[0] in range(195, 445) and pos[1] in range(164, 228):
    #         battleScreen.blit(painel_mob, (195, 164))
    #         pygame.display.flip()
    #         selectedId = 15


# personagem para testes
# TODO criar função para instanciar personagem??

helena = Helena()
helena.grimoars = 'ataque direto'
helena.grimoars = 'wind strike'
helena.grimoars = 'fire ball'
helena.grimoars = 'acqua wave'

def main():
    """
    Function main : Game start and configurations
    :return: None
    """
    global running
    global moving
    global isOptionSelected

    select = render_intro()

    tilemap = pickle.load(open('data/tilemap.txt', 'rb'))
    objmap = pickle.load(open('data/objmap.txt', 'rb'))

    clock = pygame.time.Clock()
    tile, obj = [], []

    # @TODO: chamada para tela de abertura
    # @TODO: chamada para o menu inicial
    for i in range(24):
        tile += [pygame.image.load('imagens/tile%s.png' % i)]
        obj += [pygame.image.load('imagens/obj%s.png' % i)]
    for i in range(24, 30):
        obj += [pygame.image.load('imagens/obj%s.png' % i)]

    if select == 14:
        global screen
        screen = pygame.display.set_mode((800, 600))
        #screenGame = pygame.display.set_mode((640, 480))
        #screen.blit(screenGame, (0, 0))
    elif select == 15:
        pass
    elif select == 16:
        pass
    elif select == 17:
        render_credits()
    elif select == 18:
        game_quit()

    while running:                                  # loop do jogo
        clock.tick(7)
        handle()
        move(moving)
        for y in range(HEIGHT):
            for x in range(WIDTH):
                i, j = (slide_x+x, slide_y+y)
                screen.blit(tile[tilemap[j][i]], (x*TILE, y*TILE))
        for y in range(-6, HEIGHT):
            for x in range(-4, WIDTH):
                i, j = (slide_x+x, slide_y+y)
                if objmap[j][i] < 24:
                    screen.blit(obj[objmap[j][i]], (x*TILE, y*TILE))
        mobchance = randint(0, 10) # @TODO trocar por uma chance mais rara
        if mobchance == 3:
            goblin = Goblin() # TODO: Usar uma função para gerar um mob aleatório
            settext(goblin.mob_msg())
            screen.blit(text, (250, 550))
            pygame.display.flip()
            import time             # TODO criar um modo melhor de realizar essa espera
            time.sleep(5)
            battle_screen(helena, goblin)
        pygame.display.flip()


def render_intro():
    """
    function render_intro: Cria a tela de menu do jogo
    :return: int
    """

    selectedId = 0

    screenIntro = pygame.display.set_mode((640, 480))
    while not isOptionSelected:
        handle_intro()
        fundo = pygame.image.load('imagens/cenario_1.png')
        btn_novo = pygame.image.load('imagens/btn_novo.png')
        btn_novo2 = pygame.image.load('imagens/btn_novo2.png')
        btn_load = pygame.image.load('imagens/btn_load.png')
        btn_load2 = pygame.image.load('imagens/btn_load2.png')
        btn_config = pygame.image.load('imagens/btn_config.png')
        btn_config2 = pygame.image.load('imagens/btn_config2.png')
        btn_credito = pygame.image.load('imagens/btn_credito.png')
        btn_credito2 = pygame.image.load('imagens/btn_credito2.png')
        btn_sair = pygame.image.load('imagens/btn_sair.png')
        btn_sair2 = pygame.image.load('imagens/btn_sair2.png')

        screenIntro.blit(fundo, (0, 0))
        screenIntro.blit(btn_novo, (195, 90))
        screenIntro.blit(btn_load, (195, 164))
        screenIntro.blit(btn_config, (195, 238))
        screenIntro.blit(btn_credito, (195, 312))
        screenIntro.blit(btn_sair, (195, 386))
        pygame.display.flip()

        if pos[0] in range(195, 445) and pos[1] in range(90, 154):
            screenIntro.blit(btn_novo2, (195, 90))
            pygame.display.flip()
            selectedId = NEWGAME
        elif pos[0] in range(195, 445) and pos[1] in range(164, 228):
            screenIntro.blit(btn_load2, (195, 164))
            pygame.display.flip()
            selectedId = LOADGAME
        elif pos[0] in range(195, 445) and pos[1] in range(238, 302):
            screenIntro.blit(btn_config2, (195, 238))
            pygame.display.flip()
            selectedId = CONFIGS
        elif pos[0] in range(195, 445) and pos[1] in range(312, 376):
            screenIntro.blit(btn_credito2, (195, 312))
            pygame.display.flip()
            selectedId = CREDITS
        elif pos[0] in range(195, 445) and pos[1] in range(386, 451):
            screenIntro.blit(btn_sair2, (195, 386))
            pygame.display.flip()
            selectedId = EXITGAME
        else:
            isCharSelected = 0

        MYID = pygame.event.Event(SYSTEM, {'id': selectedId, 'name': 'Roederick'})
    print(selectedId)
    return selectedId

# renderizador de textos na tela

def settext(msg, img=None):
    global text
    font = pygame.font.SysFont('maturascriptcapitals', 22)
    # deve ser uma surface na parte debaixo da tela, com 40 pixels (tamanho de um tile)
    if img is not None:
        text = pygame.image.load('imagens/barra.png').convert_alpha()
    else:
        text = pygame.Surface((300, 60))
        text.fill((150, 150, 150, 255))

    text.blit(font.render(msg, True, (255, 255, 255)), (10, 10))
    #tela = pygame.display.get_surface()
    #tela.blit(text, (0, 435))


if __name__ == "__main__":
    main()
