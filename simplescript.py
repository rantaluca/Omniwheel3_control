"""
Robert ANTALUCA 2023

Ce script permet de calculer la consigne de vitesse à appliquer à chaque moteur du robot omniwheel en fonction d'une vitesse désirée sur l'axe X/Y/w du robot. 

This script allows to calculate the speed to apply to each motor of the omniwheel robot according to a desired speed on the X/Y/w axis of the robot.

(cf. theory.pdf pour plus d'informations sur le calcul) 

"""

import math as m
import numpy as np


#### definiton des constantes ####


#matrice de calcul 

dict_matrice ={
    'a': m.cos(240), 'b': m.cos(120) ,'c': m.cos(0),
    'd': m.sin(270), 'e': m.sin(120), 'f': m.sin(0),
    'g': 1, 'h': 1, 'i': 1
}

det = dict_matrice['a'] * dict_matrice['e'] * dict_matrice['i'] + dict_matrice['b'] * dict_matrice['f'] * dict_matrice['g'] + dict_matrice['c'] * dict_matrice['d'] * dict_matrice['h'] - dict_matrice['c'] * dict_matrice['e'] * dict_matrice['g'] - dict_matrice['b'] * dict_matrice['d'] * dict_matrice['i'] - dict_matrice['a'] * dict_matrice['f'] * dict_matrice['h']

#matrice inverse de la matrice de calcul
inversed_dict_matrice = {
    'a': (dict_matrice['e']*dict_matrice['i'] - dict_matrice['f']*dict_matrice['h'])/det, 'b': (dict_matrice['h']*dict_matrice['c'] - dict_matrice['i']*dict_matrice['b'])/det ,'c': (dict_matrice['b']*dict_matrice['f'] - dict_matrice['c']*dict_matrice['e'])/det,
    'd': (dict_matrice['g']*dict_matrice['f'] - dict_matrice['d']*dict_matrice['i'])/det, 'e': (dict_matrice['a']*dict_matrice['i'] - dict_matrice['g']*dict_matrice['c'])/det, 'f': (dict_matrice['d']*dict_matrice['c'] - dict_matrice['a']*dict_matrice['f'])/det,
    'g': (dict_matrice['d']*dict_matrice['h'] - dict_matrice['g']*dict_matrice['e'])/det, 'h': (dict_matrice['g']*dict_matrice['b'] - dict_matrice['a']*dict_matrice['h'])/det, 'i': (dict_matrice['a']*dict_matrice['e'] - dict_matrice['d']*dict_matrice['b'])/det
}


class omni_bot:
    def __init__(self):
        
        self.matrix = {
        'a': m.cos(240), 'b': m.cos(120) ,'c': m.cos(0),
        'd': m.sin(270), 'e': m.sin(120), 'f': m.sin(0),
        'g': 1, 'h': 1, 'i': 1
        }
        
        self.det = self.matrix['a'] * self.matrix['e'] * self.matrix['i'] + self.matrix['b'] * self.matrix['f'] * self.matrix['g'] + self.matrix['c'] * self.matrix['d'] * self.matrix['h'] - self.matrix['c'] * self.matrix['e'] * self.matrix['g'] - self.matrix['b'] * self.matrix['d'] * self.matrix['i'] - self.matrix['a'] * self.matrix['f'] * self.matrix['h']
        
        self.inversed_matrix = {
        'a': (self.matrix['e']*self.matrix['i'] - self.matrix['f']*self.matrix['h'])/self.det, 'b': (self.matrix['h']*self.matrix['c'] - self.matrix['i']*self.matrix['b'])/self.det ,'c': (self.matrix['b']*self.matrix['f'] - self.matrix['c']*self.matrix['e'])/self.det,
        'd': (self.matrix['g']*self.matrix['f'] - self.matrix['d']*self.matrix['i'])/self.det, 'e': (self.matrix['a']*self.matrix['i'] - self.matrix['g']*self.matrix['c'])/self.det, 'f': (self.matrix['d']*self.matrix['c'] - self.matrix['a']*self.matrix['f'])/self.det,
        'g': (self.matrix['d']*self.matrix['h'] - self.matrix['g']*self.matrix['e'])/self.det, 'h': (self.matrix['g']*self.matrix['b'] - self.matrix['a']*self.matrix['h'])/self.det, 'i': (self.matrix['a']*self.matrix['e'] - self.matrix['d']*self.matrix['b'])/self.det
        }

        self.speed = [0,0,0]

    def set_speed_m1(self, v):
        self.speed[0] = v

    def set_speed_m2(self, v):
        self.speed[1] = v

    def set_speed_m3(self, v):
        self.speed[2] = v

    def set_speed(self, v1, v2, v3):
        self.speed[0] = v1
        self.speed[1] = v2
        self.speed[2] = v3  

    def get_speed(self):
        return self.speed
        
    def set_speed_robot(self, x, y, w):
        self.speed[0] = self.inversed_matrix['a']*x + self.inversed_matrix['b']*y + self.inversed_matrix['c']*w
        self.speed[1] = self.inversed_matrix['d']*x + self.inversed_matrix['e']*y + self.inversed_matrix['f']*w
        self.speed[2] = self.inversed_matrix['g']*x + self.inversed_matrix['h']*y + self.inversed_matrix['i']*w


my_robot = omni_bot()

print(my_robot.get_speed())
      
my_robot.set_speed_robot(20,0,0)

print(my_robot.get_speed())