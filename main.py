# -*- coding: utf-8 -*-
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.sound import *

#cria a janela de dimensões 768, 768
janela = Window(768, 768)
#coloca o título da janela como "A fuga do DCE"
janela.set_title("A Fuga do DCE")
#cria o teclado
teclado = Window.get_keyboard()
#cria o mouse
mouse = Window.get_mouse()
#declara a velocidade do cenario
SPEED = 120
#declara a velocidade do personagem
ASPEED = 100
#declara o GameState
GAMESTATE = 0
#declara o estado dos bônus e da condição de vitória
CANTINA = False
SKOL = False
WIN = False

#declara as músicas
musica_menu = Sound("res/menu.ogg")
musica_jogo = Sound("res/malandramente.ogg")
musica_vitoria = Sound("res/vitoria.ogg")

#cria o personagem e seus atributos
amanco = Sprite("res/Amanco3.png", 3)
amanco.set_total_duration(250)
amanco.dir = 0

#desenha as mesas de sinuca e implementa a colisão com o personagem
def draw_sinucas():
    sinuca = []
    y = 120
    for i in range(3):
        sinuca.append(GameImage("res/mesa_sinuca.png"))
        sinuca[i].set_position(100, y)
        y += 150
    for i in sinuca:
        i.draw()
        if amanco.collided(i) and amanco.dir == 3:
            amanco.x -= ASPEED * janela.delta_time()
        elif amanco.collided(i) and amanco.dir == 4:
            amanco.x += ASPEED * janela.delta_time()
        if amanco.collided(i) and amanco.dir == 1:
            amanco.y += ASPEED * janela.delta_time()
        elif amanco.collided(i) and amanco.dir == 2:
            amanco.y -= ASPEED * janela.delta_time()

#implementa a movimentação do personagem e limita seus movimentos para dentro da janela
def mov_amanco():

    if teclado.key_pressed('UP'):
        amanco.y -= ASPEED * janela.delta_time()
        amanco.dir = 1
    elif teclado.key_pressed('DOWN'):
        amanco.y += ASPEED * janela.delta_time()
        amanco.dir = 2
    elif teclado.key_pressed('RIGHT'):
        amanco.x += ASPEED * janela.delta_time()
        amanco.dir = 3
    elif teclado.key_pressed('LEFT'):
        amanco.x -= ASPEED * janela.delta_time()
        amanco.dir = 4

    if amanco.x <= 0:
        amanco.x = 0
    if amanco.x >= janela.width - amanco.width:
        amanco.x = janela.width - amanco.width
    if amanco.y <= 0:
        amanco.y = 0
    if amanco.y >= janela.height - amanco.height:
        amanco.y = janela.height - amanco.height

#desenha os blocos do jogo(as partes pretas, o bar e o DJ) e implementa a colisão com o personagem
def draw_blocos():

    bloco1 = dict(img=GameImage("res/bloco_1.png"), posX=0, posY=janela.height - GameImage("res/bloco_1.png").height)
    bloco2 = dict(img=GameImage("res/bloco_2.png"), posX=314, posY=janela.height - GameImage("res/bloco_2.png").height)
    bloco3 = dict(img=GameImage("res/bloco_3.png"), posX=314+GameImage("res/bloco_2.png").width, posY=janela.height - GameImage("res/bloco_3.png").height)
    bloco4 = dict(img=GameImage("res/bloco_4.png"), posX=314 + GameImage("res/bloco_2.png").width, posY=janela.height - (GameImage("res/bloco_3.png").height + GameImage("res/bloco_4.png").height))
    balcao = dict(img=GameImage("res/balcao.png"), posX=janela.width - GameImage("res/balcao.png").width, posY=118)

    blocos= [bloco1, bloco2, bloco3, bloco4, balcao]

    for i in blocos:
        i["img"].set_position(i["posX"], i["posY"])
        i["img"].draw()
        if amanco.collided(i["img"]) and amanco.dir == 3:
            amanco.x -= ASPEED * janela.delta_time()
        elif amanco.collided(i["img"]) and amanco.dir == 4:
            amanco.x += ASPEED * janela.delta_time()
        if amanco.collided(i["img"]) and amanco.dir == 1:
            amanco.y += ASPEED * janela.delta_time()
        elif amanco.collided(i["img"]) and amanco.dir == 2:
            amanco.y -= ASPEED * janela.delta_time()

#desenha as fileiras de mesa, que farão grande parte do "labirinto", e implementa a colisão com o personagem
def draw_mesas():
    mesa = GameImage("res/mesa_grande.png")
    mesas1 = dict(img=mesa, posX=200, posY=60, incremento=50, fila=3)
    mesas2 = dict(img=mesa, posX=300, posY=200, incremento=50, fila=3)
    mesas3 = dict(img=mesa, posX=0, posY=480, incremento=50, fila=2)
    mesas4 = dict(img=mesa, posX=350, posY=200 + mesa.height, incremento=0, fila=1)
    mesas5 = dict(img=mesa, posX=mesa.width, posY=280, incremento=0, fila=1)
    mesas6 = dict(img=mesa, posX=400, posY=360, incremento=50, fila=3)
    mesas7 = dict(img=mesa, posX=450, posY=0, incremento=50, fila=4)
    mesas8 = dict(img=mesa, posX=520, posY=120, incremento=50, fila=2)

    mesas = [mesas1, mesas2, mesas3, mesas4, mesas5, mesas6, mesas7, mesas8]

    for i in mesas:
        for j in range(i["fila"]):
            i["img"].set_position(i["posX"] + j * i["incremento"], i["posY"])
            i["img"].draw()
            if amanco.collided(i["img"]) and amanco.dir == 3:
                amanco.x -= ASPEED * janela.delta_time()
            elif amanco.collided(i["img"]) and amanco.dir == 4:
                amanco.x += ASPEED * janela.delta_time()
            if amanco.collided(i["img"]) and amanco.dir == 1:
                amanco.y += ASPEED * janela.delta_time()
            elif amanco.collided(i["img"]) and amanco.dir == 2:
                amanco.y -= ASPEED * janela.delta_time()

#desenha a saida e implementa a mudança da variavel WIN
def draw_saida():
    global WIN

    saida = dict(img=GameImage("res/saida.png"), posX=310, posY=janela.height - GameImage("res/saida.png").height)

    saida["img"].set_position(saida["posX"], saida["posY"])

    saida["img"].draw()

    if amanco.collided(saida["img"]) and CANTINA and SKOL:
        WIN = True

#cria a lista de meninas
def cria_meninas():
    menina_1 = dict(img=Sprite("res/menina1.png", 3), posX=300, posY=480, deltax=200, voltando=0)
    menina_2 = dict(img=Sprite("res/menina2.png", 3), posX=0, posY=350, deltax=350, voltando=0)
    menina_3 = dict(img=Sprite("res/menina3.png", 3), posX=200, posY=120, deltax=300, voltando=0)
    menina_4 = dict(img=Sprite("res/menina4.png", 3), posX=0, posY=200, deltax=250, voltando=0)
    menina_5 = dict(img=Sprite("res/menina5.png", 3), posX=400, posY=280, deltax=180, voltando=0)
    menina_6 = dict(img=Sprite("res/menina1.png", 3), posX=350, posY=60, deltax=220, voltando=0)
    menina_7 = dict(img=Sprite("res/menina2.png", 3), posX=120, posY=500, deltax=150, voltando=0)
    menina_8 = dict(img=Sprite("res/menina3.png", 3), posX=550, posY=570, deltax=60, voltando=0)
    guardia_cantina = dict(img=Sprite("res/menina4.png", 3), posX=640, posY=60, deltax=100, voltando=0)
    guardia_skol = dict(img=Sprite("res/menina5.png", 3), posX=janela.width - GameImage("res/balcao.png").width, posY=500, deltax=100, voltando=0)

    meninas = [menina_1, menina_2, menina_3, menina_4, menina_5, menina_6, menina_7, menina_8, guardia_cantina, guardia_skol]

    for menina in meninas:
        menina["img"].set_total_duration(125)
        menina["img"].set_position(menina["posX"], menina["posY"])

    return meninas

#cria efetivamente a lista de dicionários das meninas
meninas = cria_meninas()

#desenha as meninas e implementa suas colisões
def draw_meninas():

    for menina in meninas:
        if menina["voltando"] == 0:
            menina["img"].x += SPEED * janela.delta_time()
            if menina["img"].x >= menina["posX"] + menina["deltax"]:
                menina["voltando"] = 1
        if menina["voltando"] == 1:
            menina["img"].x -= SPEED * janela.delta_time()
            if menina["img"].x <= menina["posX"]:
                menina["voltando"] = 0

        if amanco.collided(menina["img"]):
            restart()

        menina["img"].draw()
        menina["img"].update()

#desenha os bônus e implementa a mudança das variáveis CANTINA e SKOL
def draw_bonus():
    global CANTINA
    global SKOL
    global ASPEED

    if(CANTINA == False):
        cantina = GameImage("res/cantina.png")
        cantina.set_position(janela.width - cantina.width, 0)
        cantina.draw()
        if amanco.collided(cantina):
            CANTINA = True
            ASPEED += 10
    if (SKOL == False):
        skol = GameImage("res/skol.png")
        skol.set_position(janela.width - skol.width, janela.height - (GameImage("res/bloco_3.png").height + skol.height))
        skol.draw()
        if amanco.collided(skol):
            SKOL = True
            ASPEED += 10

#desenha o menu na tela e implementa suas interações
def menu():
    global GAMESTATE

    fundo = GameImage("res/menu.png")
    bt_iniciar = GameImage("res/botao_iniciar.png")
    bt_ajuda = GameImage("res/botao_ajuda.png")
    bt_sair = GameImage("res/botao_sair.png")

    fundo.draw()
    bt_iniciar.set_position(fundo.width/2 - bt_iniciar.width/2, 400)
    bt_ajuda.set_position(fundo.width/2 - bt_iniciar.width/2, 500)
    bt_sair.set_position(fundo.width/2 - bt_iniciar.width/2, 600)
    bt_ajuda.draw()
    bt_sair.draw()
    bt_iniciar.draw()

    if mouse.is_button_pressed(1) and mouse.is_over_object(bt_iniciar) or teclado.key_pressed("ENTER"):
        GAMESTATE = 1
    elif mouse.is_button_pressed(1) and mouse.is_over_object(bt_sair) or teclado.key_pressed("escape"):
        janela.close()
    elif mouse.is_button_pressed(1) and mouse.is_over_object(bt_ajuda):
        GAMESTATE = 4

#desenha a apresentação na tela e implementa sua interação
def apresentacao():
    global GAMESTATE

    fundo = GameImage("res/base_inicial.png")
    fundo.draw()

    if teclado.key_pressed("SPACE"):
        GAMESTATE = 2

#desenha a mensagem de vitória na tela e implementa sua interação
def vitoria():
    global GAMESTATE

    fundo = GameImage("res/base_vitoria.png")
    fundo.draw()

    if teclado.key_pressed("SPACE"):
        restart()

#desenha o menu de ajuda e implementa suas interações
def ajuda():
    fundo = GameImage("res/instrucoes.png")
    fundo.draw()
    if teclado.key_pressed("SPACE"):
        restart()

#define a condição de vitória
def win():
    global GAMESTATE
    if WIN:
        GAMESTATE = 3

#restarta o jogo(para a música, coloca Amanco no S0, GAMESTATE = 0, CANTINA, SKOL E WIN = False
def restart():
    global CANTINA
    global SKOL
    global WIN
    global GAMESTATE

    GAMESTATE = 0
    WIN = False
    SKOL = False
    CANTINA = False

    if musica_vitoria.is_playing():
        musica_vitoria.stop()

    if musica_jogo.is_playing():
        musica_jogo.stop()

    amanco.set_position(0, 0)


while True:

    if GAMESTATE == 0:
        if musica_menu.is_playing() == False:
            musica_menu.play()
        menu()
        janela.update()
    elif GAMESTATE == 1:
        apresentacao()
        janela.update()
    elif GAMESTATE == 2:
        if musica_menu.is_playing():
            musica_menu.stop()
        if musica_jogo.is_playing() == False:
            musica_jogo.play()
        janela.set_background_color((97, 0, 0))
        amanco.draw()
        draw_sinucas()
        draw_mesas()
        mov_amanco()
        draw_blocos()
        draw_meninas()
        draw_bonus()
        draw_saida()
        win()
        amanco.update()
        janela.update()
    elif GAMESTATE == 3:
        if musica_jogo.is_playing():
            musica_jogo.stop()
        if musica_vitoria.is_playing() == False:
            musica_vitoria.play()
        vitoria()
        janela.update()
    elif GAMESTATE == 4:
        ajuda()
        janela.update()
