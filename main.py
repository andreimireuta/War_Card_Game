import pygame
from pygame import *
import tkinter as war
from tkinter import *
import time
import random
import gc

class Cards:
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
    "cruce_A": A,
    "cruce_J": J,
    "cruce_Q": Q,
    "cruce_K": K,

    "frunza_2": 2,
    "frunza_3": 3,
    "frunza_4": 4,
    "frunza_5": 5,
    "frunza_6": 6,
    "frunza_7": 7,
    "frunza_8": 8,
    "frunza_9": 9,
    "frunza_10": 10,
    "frunza_A": A,
    "frunza_J": J,
    "frunza_Q": Q,
    "frunza_K": K,

    "inima_2": 2,
    "inima_3": 2,
    "inima_4": 2,
    "inima_5": 2,
    "inima_6": 2,
    "inima_7": 2,
    "inima_8": 2,
    "inima_9": 2,
    "inima_10": 2,
    "inima_A": A,
    "inima_J": J,
    "inima_Q": Q,
    "inima_K": K,

    "romb_2": 2,
    "romb_3": 3,
    "romb_4": 4,
    "romb_5": 5,
    "romb_6": 6,
    "romb_7": 7,
    "romb_8": 8,
    "romb_9": 9,
    "romb_10": 10,
    "romb_A": A,
    "romb_J": J,
    "romb_Q": Q,
    "romb_K": K,

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

# Dimensiunea pachetului de carti pentru pc
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



def gameInit():
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


    display.blit(carte_curenta_pc_micsorata, (440,250))
    display.blit(carte_curenta_player_micsorata, (650,250))


    pygame.display.update()
    pygame.time.wait(500)

# Game Loop-aici se face tot
def gameLoop():

    running = True

    while running:
        pygame.event.pump()
        event = pygame.event.wait()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            gameInit()

if __name__ == '__main__':
    gameLoop()