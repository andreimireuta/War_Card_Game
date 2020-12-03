import pygame
from pygame import *
import tkinter as war
from tkinter import *
from PIL import ImageTk, Image
import time
import random
from tkinter import *
import time
import gc

pygame.init()

display = pygame.display.set_mode((1280, 720))  # Fereastra care se deschide si dimensiunea acesteia
pygame.display.set_caption("War Card Game")    # Titlul ferestrei ce se deschide


running = True
while running