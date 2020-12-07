import pygame
from pygame import *
import tkinter as war
from tkinter import *
import time
import random
import gc,itertools
from queue import Queue

class Carti:
    cruce_2 = pygame.image.load('cards/cruce/Playing_card_club_2.png')
    cruce_3 = pygame.image.load('cards/cruce/Playing_card_club_3.png')
    cruce_4 = pygame.image.load('cards/cruce/Playing_card_club_4.png')
    cruce_5 = pygame.image.load('cards/cruce/Playing_card_club_5.png')
    cruce_6 = pygame.image.load('cards/cruce/Playing_card_club_6.png')
    cruce_7 = pygame.image.load('cards/cruce/Playing_card_club_7.png')
    cruce_8 = pygame.image.load('cards/cruce/Playing_card_club_8.png')
    cruce_9 = pygame.image.load('cards/cruce/Playing_card_club_9.png')
    cruce_10 = pygame.image.load('cards/cruce/Playing_card_club_10.png')
    cruce_A = pygame.image.load('cards/cruce/Playing_card_club_A.png')
    cruce_J = pygame.image.load('cards/cruce/Playing_card_club_J.png')
    cruce_Q = pygame.image.load('cards/cruce/Playing_card_club_Q.png')
    cruce_K = pygame.image.load('cards/cruce/Playing_card_club_K.png')

    frunza_2 = pygame.image.load('cards/frunza/Playing_card_spade_2.png')
    frunza_3 = pygame.image.load('cards/frunza/Playing_card_spade_3.png')
    frunza_4 = pygame.image.load('cards/frunza/Playing_card_spade_4.png')
    frunza_5 = pygame.image.load('cards/frunza/Playing_card_spade_5.png')
    frunza_6 = pygame.image.load('cards/frunza/Playing_card_spade_6.png')
    frunza_7 = pygame.image.load('cards/frunza/Playing_card_spade_7.png')
    frunza_8 = pygame.image.load('cards/frunza/Playing_card_spade_8.png')
    frunza_9 = pygame.image.load('cards/frunza/Playing_card_spade_9.png')
    frunza_10 = pygame.image.load('cards/frunza/Playing_card_spade_10.png')
    frunza_A = pygame.image.load('cards/frunza/Playing_card_spade_A.png')
    frunza_J = pygame.image.load('cards/frunza/Playing_card_spade_J.png')
    frunza_Q = pygame.image.load('cards/frunza/Playing_card_spade_Q.png')
    frunza_K = pygame.image.load('cards/frunza/Playing_card_spade_K.png')

    inima_2 = pygame.image.load('cards/inima/Playing_card_heart_2.png')
    inima_3 = pygame.image.load('cards/inima/Playing_card_heart_3.png')
    inima_4 = pygame.image.load('cards/inima/Playing_card_heart_4.png')
    inima_5 = pygame.image.load('cards/inima/Playing_card_heart_5.png')
    inima_6 = pygame.image.load('cards/inima/Playing_card_heart_6.png')
    inima_7 = pygame.image.load('cards/inima/Playing_card_heart_7.png')
    inima_8 = pygame.image.load('cards/inima/Playing_card_heart_8.png')
    inima_9 = pygame.image.load('cards/inima/Playing_card_heart_9.png')
    inima_10 = pygame.image.load('cards/inima/Playing_card_heart_10.png')
    inima_A = pygame.image.load('cards/inima/Playing_card_heart_A.png')
    inima_J = pygame.image.load('cards/inima/Playing_card_heart_J.png')
    inima_Q = pygame.image.load('cards/inima/Playing_card_heart_Q.png')
    inima_K = pygame.image.load('cards/inima/Playing_card_heart_K.png')

    romb_2 = pygame.image.load('cards/romb/Playing_card_diamond_2.png')
    romb_3 = pygame.image.load('cards/romb/Playing_card_diamond_3.png')
    romb_4 = pygame.image.load('cards/romb/Playing_card_diamond_4.png')
    romb_5 = pygame.image.load('cards/romb/Playing_card_diamond_5.png')
    romb_6 = pygame.image.load('cards/romb/Playing_card_diamond_6.png')
    romb_7 = pygame.image.load('cards/romb/Playing_card_diamond_7.png')
    romb_8 = pygame.image.load('cards/romb/Playing_card_diamond_8.png')
    romb_9 = pygame.image.load('cards/romb/Playing_card_diamond_9.png')
    romb_10 = pygame.image.load('cards/romb/Playing_card_diamond_10.png')
    romb_A = pygame.image.load('cards/romb/Playing_card_diamond_A.png')
    romb_J = pygame.image.load('cards/romb/Playing_card_diamond_J.png')
    romb_Q = pygame.image.load('cards/romb/Playing_card_diamond_Q.png')
    romb_K = pygame.image.load('cards/romb/Playing_card_diamond_K.png')
    romb_K = pygame.image.load('cards/romb/Playing_card_diamond_K.png')


valori = {
    "cruce_2": 2,
    "cruce_3": 3,
    "cruce_4": 4,
    "cruce_5": 5,
    "cruce_6": 6,
    "cruce_7": 7,
    "cruce_8": 8,
    "cruce_9": 9,
    "cruce_10": 10,
    "cruce_A": 15,
    "cruce_J": 12,
    "cruce_Q": 13,
    "cruce_K": 14,

    "frunza_2": 2,
    "frunza_3": 3,
    "frunza_4": 4,
    "frunza_5": 5,
    "frunza_6": 6,
    "frunza_7": 7,
    "frunza_8": 8,
    "frunza_9": 9,
    "frunza_10": 10,
    "frunza_A": 15,
    "frunza_J": 12,
    "frunza_Q": 13,
    "frunza_K": 14,

    "inima_2": 2,
    "inima_3": 3,
    "inima_4": 4,
    "inima_5": 5,
    "inima_6": 6,
    "inima_7": 7,
    "inima_8": 8,
    "inima_9": 9,
    "inima_10": 10,
    "inima_A": 15,
    "inima_J": 12,
    "inima_Q": 13,
    "inima_K": 14,

    "romb_2": 2,
    "romb_3": 3,
    "romb_4": 4,
    "romb_5": 5,
    "romb_6": 6,
    "romb_7": 7,
    "romb_8": 8,
    "romb_9": 9,
    "romb_10": 10,
    "romb_A": 15,
    "romb_J": 12,
    "romb_Q": 13,
    "romb_K": 14,

}


pygame.init()

# Fereastra care se deschide si dimensiunea acesteia
display = pygame.display.set_mode((1280, 720))

# Titlul ferestrei ce se deschide
pygame.display.set_caption("War Card Game")

# Schimbarea iconitei si pudate-ul ei
icon = pygame.image.load('card-games.png')
pygame.display.set_icon(icon)

display.fill([10, 80, 10])
pygame.display.update()

#Diverse constante
lungime_pachet = int(150*1.25)
latime_pachet = 150
lungime_carte = int(175*1.25)
latime_carte = 175

pachet = [carte
          for carte in dir(Carti)
          if not carte.startswith('__')]

pachet_carti_pc = Queue(52)
pachet_carti_player = Queue(52)
pachet_carti_razboi = Queue(52)

def creare_pachet():

    random.shuffle(pachet)
    global pachet_carti_pc, pachet_carti_player,pachet_carti_razboi

    # ia primul element din coada cat timp maia vem carti
    while not pachet_carti_razboi.empty():
        pachet_carti_razboi.get()
    while not pachet_carti_player.empty():
        pachet_carti_player.get()
    while not pachet_carti_pc.empty():
        pachet_carti_pc.get()

    const=0
    for x in pachet:
        #if const % 2 == 0 :
        if const < 26:
            pachet_carti_pc.put(x)
        else:
            pachet_carti_player.put(x)
        const += 1


# Dimensiunea pachetului de carti pentru pc si pozitionare pachetului
pachet_pc = pygame.image.load('cards/cruce/Card_back_01.svg.png')
pachet_pc_micsorat = pygame.transform.scale(pachet_pc, (latime_pachet, lungime_pachet))
pachet_pc_x = 60
pachet_pc_y = 45

#Dimensiunea pachetului de carti pentru player
pachet_player = pygame.image.load('cards/cruce/Card_back_01.svg.png')
pachet_player_micsorat = pygame.transform.scale(pachet_player, (latime_pachet,lungime_pachet))
pachet_player_x = 1050
pachet_player_y = 470

# Cartile care se afiseaza pe ecran (ale player-ului si alea pc-ului)
carte_curenta_pc = pygame.image.load('cards/inima/Playing_card_heart_2.png')
carte_curenta_player = pygame.image.load('cards/inima/Playing_card_heart_2.png')

carte_curenta_pc_micsorata = pygame.transform.scale(carte_curenta_pc, (latime_carte , lungime_carte))
carte_curenta_player_micsorata = pygame.transform.scale(carte_curenta_player,(latime_carte , lungime_carte))

# culorile folosite in button
white = (55, 120, 40)
black = (60, 160, 40)
alb = [255, 255 , 255]
red = (255, 0, 0)

clicked = False
font = pygame.font.SysFont('Arial',24)
font_razboi= pygame.font.SysFont('Arial', 50)
font_titlu = pygame.font.SysFont('Arial', 80)


class button():
    #Culoarea butoanelor si a textului
    button_col = (55,125,40)
    hover_col = (65,160,45)
    click_col = (50,150,20)
    text_col = (255,255,255)
    width = 150
    height=40

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):
        global clicked
        action = False

        #pozitia mouse-ului
        pozitie = pygame.mouse.get_pos()

        #draptunghiul pentru buton
        button_rectangle = Rect(self.x, self.y, self.width, self.height)

        #verificam ce face mouse-ul si daca este apasat butonul
        if button_rectangle.collidepoint(pozitie):
            if pygame.mouse.get_pressed()[0] == 1: # if ul acesta ne spune daca butonul a fost clickat si dupa aia i-a fost dat drumul
                clicked = True
                pygame.draw.rect(display,self.click_col,button_rectangle) # daca butonul este apasat atunci ii dam alta culoare si il redesenam
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False # resetam click ul
                action = True
            else:
                pygame.draw.rect(display, self.hover_col, button_rectangle)
        else:
            pygame.draw.rect(display, self.button_col, button_rectangle)

        #adaugam umbre la button
        pygame.draw.line(display, black, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(display, black, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(display, white, (self.x, self.y + self.height),(self.x + self.width, self.y + self.height),2)
        pygame.draw.line(display, white, (self.x + self.width, self.y),(self.x + self.width, self.y + self.height),2)

        #adaugam text butonului
        text_image = font.render(self.text,True,self.text_col)
        text_length = text_image.get_width()
        display.blit(text_image, (self.x + int(self.width/2)-int(text_length/2), self.y + 5))
        return action


razboi = False
castigator_razboi=''
dimensiunea_razboiului = 0
carti_razboi_ramase = 0
prima_runda = False

def gameInit():
    display.fill([10, 80, 10])
    pygame.display.update()

    global button, score_button, play_button,carte_curenta_player_micsorata,carte_curenta_pc,carte_curenta_player
    global razboi,dimensiunea_razboiului,castigator_razboi,carti_razboi_ramase
    # Pachetele de carti care se afiseaza in colturi
    display.blit(pachet_pc_micsorat, (pachet_pc_x, pachet_pc_y))
    display.blit(pachet_pc_micsorat, (pachet_pc_x + 3, pachet_pc_y + 3))
    display.blit(pachet_pc_micsorat, (pachet_pc_x + 6, pachet_pc_y + 6))
    display.blit(pachet_pc_micsorat, (pachet_pc_x + 9, pachet_pc_y + 9))
    display.blit(pachet_pc_micsorat, (pachet_pc_x + 12, pachet_pc_y + 12))

    display.blit(pachet_player_micsorat, (pachet_player_x, pachet_player_y))
    display.blit(pachet_player_micsorat, (pachet_player_x + 3, pachet_player_y + 3))
    display.blit(pachet_player_micsorat, (pachet_player_x + 6, pachet_player_y + 6))
    display.blit(pachet_player_micsorat, (pachet_player_x + 9, pachet_player_y + 9))
    display.blit(pachet_player_micsorat, (pachet_player_x + 12, pachet_player_y + 12))

    # cartile player-ilor care se afiseaza in centru, in mod random
    if not pachet_carti_player.empty() and not razboi:
        carte_curenta_player= pachet_carti_player.get()
        display.blit(pygame.transform.scale(getattr(Carti,carte_curenta_player),(latime_carte,lungime_carte)), (650,250))
        # display.blit(carte_curenta_player_micsorata, (650, 250))
    else:
        display.blit(carte_curenta_player_micsorata, (650, 250))
        copie= dimensiunea_razboiului
        carte_curenta_player = pachet_carti_player.get()
        carte_curenta_player_micsorata = getattr(Carti,carte_curenta_player)
        carte_curenta_player_micsorata = pygame.transform.scale(carte_curenta_player_micsorata, (latime_carte, lungime_carte))

        display.blit(carte_curenta_player_micsorata, (655, 250))
        pixeli = 5
        while copie - carti_razboi_ramase:
            display.blit(carte_curenta_player_micsorata,(655 +pixeli, 250))
            pixeli+=5
            pygame.display.update()
            copie -=1


    dimensiune_pachet_player = font.render("Carti disponibile: " + str(pachet_carti_player.qsize()), True, (255, 255, 255))
    display.blit(dimensiune_pachet_player, (pachet_player_x, pachet_player_y-40))

    if not pachet_carti_pc.empty() and not razboi:
        # afisarea cartilor in mod random pe ecran
        carte_curenta_pc = pachet_carti_pc.get()
        carte_curenta_pc_micsorata = getattr(Carti,carte_curenta_pc)
        carte_curenta_pc_micsorata = pygame.transform.scale(carte_curenta_pc_micsorata, (latime_carte, lungime_carte))
        display.blit(carte_curenta_pc_micsorata, (440,250))
    else:
        copie = dimensiunea_razboiului
        carte_curenta_pc = pachet_carti_pc.get()
        carte_curenta_pc_micsorata = getattr(Carti, carte_curenta_pc)
        carte_curenta_pc_micsorata = pygame.transform.scale(carte_curenta_pc_micsorata, (latime_carte, lungime_carte))
        display.blit(carte_curenta_pc_micsorata, (435, 250))
        display.blit(carte_curenta_pc_micsorata,(430,250))
        pixeli = 5
        while copie - carti_razboi_ramase:
            display.blit(carte_curenta_pc_micsorata,(430 - pixeli, 250))
            pixeli+=5
            pygame.display.update()
            copie -=1

    dimensiune_pachet_pc = font.render("Carti disponibile: " + str(pachet_carti_pc.qsize()), True, alb)
    # pygame.draw.rect(display,(255, 255, 255), (pachet_pc_x-20, pachet_pc_y- 30, latime_carte, lungime_carte))
    display.blit(dimensiune_pachet_pc, (pachet_pc_x, pachet_pc_y - 20 + lungime_carte + 20))
    pygame.display.update()


    #print("Dimensiunea pachetului este de :", pachet_carti_player.qsize() + pachet_carti_pc.qsize())
    #pc-ul castiga cartea
    if valori[carte_curenta_pc] > valori[carte_curenta_player]:
        if razboi == False:
            pachet_carti_pc.put(carte_curenta_pc)
            pachet_carti_pc.put(carte_curenta_player)
            #print('Pc-ul are carte mai mare,ncsf...')
        elif razboi == True:
            if pachet_carti_razboi.qsize() < dimensiunea_razboiului *2:
                #display.blit(pygame.transform.scale(getattr(Carti, carte_curenta_player), (latime_carte, lungime_carte)),(655, 255))
                pachet_carti_razboi.put(carte_curenta_pc)
                pachet_carti_razboi.put(carte_curenta_player)
                #print('pc ul te cam bate...')
            else:
                # =-//=
                razboi = False
                pachet_carti_razboi.put(carte_curenta_pc)
                pachet_carti_razboi.put(carte_curenta_player)
                print('Razboiul s-a terminat. Pc-ul a castigat')
                while not pachet_carti_razboi.empty():
                    pachet_carti_pc.put(pachet_carti_razboi.get())


    #player-ul castiga cartea
    if valori[carte_curenta_pc] < valori[carte_curenta_player]:
        if razboi == False:
            pachet_carti_player.put(carte_curenta_player)
            pachet_carti_player.put(carte_curenta_pc)
            #print('nope,playerul are cartea mai mare')
        elif razboi == True:
            if pachet_carti_razboi.qsize() < dimensiunea_razboiului *2:
                pachet_carti_razboi.put(carte_curenta_pc)
                pachet_carti_razboi.put(carte_curenta_player)
            else:
                razboi = False
                #punem cartile castigatoare in pachetul player-ului
                #print('Razboiul s-a terminat. Pc-ul a castigat')
                pachet_carti_razboi.put(carte_curenta_pc)
                pachet_carti_razboi.put(carte_curenta_player)
                while not pachet_carti_razboi.empty():
                    pachet_carti_player.put(pachet_carti_razboi.get())

    #cazul in care este RAZBOI
    if valori[carte_curenta_pc] == valori[carte_curenta_player]:
        if razboi == False:
            razboi = True
            if (valori[carte_curenta_player] == 15):
                dimensiunea_razboiului = 11
            else:
                dimensiunea_razboiului = valori[carte_curenta_player]

            print("Razboi intre carti de dimensiunea:", dimensiunea_razboiului)
            pachet_carti_razboi.put(carte_curenta_pc)
            pachet_carti_razboi.put(carte_curenta_player)

        # cazul in care avem razboi dupa razboi
        elif razboi == True:
            if pachet_carti_razboi.qsize() < dimensiunea_razboiului *2:
                pachet_carti_razboi.put(carte_curenta_pc)
                pachet_carti_razboi.put(carte_curenta_player)
            else:
                dimensiunea_razboiului += valori[carte_curenta_player]
                pachet_carti_razboi.put(carte_curenta_pc)
                pachet_carti_razboi.put(carte_curenta_player)
                print('Razboi dupa razboi ',dimensiunea_razboiului)

    if razboi == True:
        afisare_razboi = font_razboi.render("RAZBOI", True, (255, 0 ,0))
        #pygame.draw.rect(display,[10, 80, 10], (600, 350, 200, 80))
        display.blit(afisare_razboi,(535, 520))
        carti_razboi_ramase = 1+ dimensiunea_razboiului - int(pachet_carti_razboi.qsize()/2)
        if dimensiunea_razboiului >= carti_razboi_ramase:
            afisare_carti_razboi_ramase = font_razboi.render(str(carti_razboi_ramase), True, (255, 0, 0))
            display.blit(afisare_carti_razboi_ramase, (595, 570))

    #score_button = button(1080, 50, 'See the Score')
    #play_button = button(50, 650, 'Tap to quit')
    # if score_button.draw_button():
    #     pygame.draw.rect(display, white, pygame.Rect(600, 50, 100, 50))
    #     print('Play')

    pygame.display.update()
    #pygame.time.wait(500)



# Declarara globala a butoanelor
score_button = button(1300, 800, "cfm")
play_button = button(50, 650, 'Tap to play')

titlu_pagina = font_titlu.render("Jocul Razboi", True, alb)
display.blit(titlu_pagina,(450,150))

afisare_start = font_razboi.render("Click to start", True, alb)
#pygame.draw.rect(display,(0, 0, 0), (600,400,250,100))
display.blit(afisare_start, (530, 330))

pygame.display.update()
# Game Loop-aici se face tot
def gameLoop():

    global button,score_button,play_button
    running = True

    while running:

        # pygame.event.pump()
        event = pygame.event.wait()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         gameInit()

                # pachet_player_x, pachet_player_y = event.pos
                # if pachet_player.get_rect().collidepoint(pachet_player_x, pachet_player_y):
                #     print('clicked on the image')

        start_check=1
        castigator= ''

        if(start_check==0):
            start_check=1
            pygame.draw.rect(display, (0, 255, 0), (680, 380, 190, 50))

        creare_pachet()
        pygame.display.update()
        if play_button.draw_button():
            gameInit()

        while not pachet_carti_pc.empty() and not pachet_carti_player.empty():
            pygame.event.pump()
            event = pygame.event.wait()

            if(event.type == QUIT):
                exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    gameInit()

            # if play_button.draw_button():
            #     print("game has ended by quiting")
            #     exit(0)

            if pachet_carti_player.empty():
                castigator = 'Pc'
                break
            if pachet_carti_pc.empty():
                castigator= 'Player'
                break
        while castigator:
            display.blit()
            print(castigator," wins !!!!")
            castigator = ''
        pygame.display.update()

if __name__ == '__main__':
    gameLoop()