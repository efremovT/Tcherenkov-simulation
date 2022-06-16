#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 08:42:58 2022

@author: tefrem49
"""
import numpy as np
""" Modelisation de la geometrie du detecteur"""

#1 la position des capteurs

def def_capteurs(Nx,dx,h0x,Ny,dy,h0y) :
    """prend comme argument le nombre de capteurs sur chaque axe (Nx,Ny)
    la distance entre 2 capteurs sur chaque axe (dx,dy)
    et la position intiale du premier capteur sur chaque axe (h0x,h0y)
    
    et renvoie deux tableau numpy 2D contenant respectivement leurs positions
    sur les x et sur les y
    
    ainsi qu'un tableau 'compteur' qui servira a stocke le nombre de photons absorbe
    et une liste temps qui servira a stocke le temps d'absorbtion de chaque photon
    
    La premiere indexation correspond aux y et la seconde aux x
    compteur[y][x]"""
    
    x = np.arange(h0x , h0x + Nx*dx , dx) - ( (Nx-1)*dx / 2 ) # centre en 0
    y = np.arange(h0y , h0y + Ny*dy , dy)
    
    X,Y = np.meshgrid(x,y)  
    
    compteur = np.zeros(X.shape)

    temps = [[[]for n in range(Nx)]for n in range(Ny) ]
    
    return X,Y,compteur,temps
 
##test
#Nx = 21
#dx = 20
#h0x = 0
#Ny = 20
#dy = 10
#h0y =40
#
#capteurs = def_capteurs(Nx,dx,h0x,Ny,dy,h0y)
#plt.figure()
#plt.plot(capteurs[0],capteurs[1] ,'bx')

    
    