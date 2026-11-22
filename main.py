import python_snake_game as snake_game #lib 1
import pygame #lib 2
import turtle #lib 3
import pyglet #lib 4
#----lib 5 ---------
from ursina import *
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
#using a lib 1=>FOR PYTHON GAME PROTOTYPE
snake_game.automatic_configure_custom_key()
snake_game.manual_configure_custom_key()
snake_game.reset_key_configuration()
snake_game.play(speed=10,grid_size=(20,15),poison_mode=False,invisible_wall=True)

