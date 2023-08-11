# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.

import pygame as pg

pg.init()
pg.mixer.music.load("ex021.mp3")
pg.mixer.music.play()
pg.event.wait
