#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:28:02 2022

@author: tefrem49
"""

import Capteur as capt
import Muon as mu
import Detect3 as detect
import matplotlib.pyplot as plt
import numpy as np

detectv=np.vectorize(detect.absorption,excluded=[3,4])

""" On définis notre tableau de capteur de taille 420m * 240m """
Nx = 21
dx = 20
h0x = 0
Ny = 20
dy = 10
h0y =40
#
#Nx = 200
#dx = 20
#h0x = 0
#Ny = 200
#dy = 10
#h0y =40

capteurs = capt.def_capteurs(Nx,dx,h0x,Ny,dy,h0y)
pos_capx = capteurs[0]
pos_capy = capteurs[1]

plt.figure()
plt.plot(capteurs[0],capteurs[1] ,'bx')


""" et un tableau vide qui s'incrémente pour chaque absorbtion
et un tableau de tableau qui stocke le temps d'arriver de chaque photon"""
Absorbé = capteurs[2]
Temps_Abs = capteurs[3]

""" on définis la position intiale et la direction et la vitesse du muon par 
un tirage aléatoire"""
D = 5 * 50 #marge de distance de création
#xmuon = np.random.uniform(low = pos_capx[0,0] - D , high = pos_capx[0,-1] + D)
#ymuon = np.random.uniform(low = pos_capy[0,0] - D , high = pos_capy[-1,0] + D)

xmuon=20
ymuon=0
 
pos = [xmuon,ymuon]


vmuon = 3*1e8
#theta = np.random.uniform(low=0,high=2*np.pi) #angle par rapport a x
theta=np.pi/2
""" on définis le pas de temps et la durée de temps d'étude de sorte qu'a chaque
pas de temps le muon parcoure 2 m et qu'a la fin du temps d'étude il soit éloigné
d'au moins 300 m du detecteur donc qu'il ai parcouru grossièrement 1000m """

#dt = 50/vmuon 
#Tfin = 50/vmuon

dt = 0.5/vmuon
Tfin = 1000/vmuon
T = np.arange(0,Tfin,dt)


"""maintenant on fais boucler notre code pour un pas de temps dt"""
compteur = 0 #compteur d'itération ou rien ne se passe
for i in range(0,len(T)) :
    
    """ on actualise la positon du muon et on calcule sa distance parcouru"""
    posf , dist = mu.muon(pos[0],pos[1],vmuon, dt ,theta)
    """ on caractérise le nombre de photon émis et leurs position"""
    
    pos_photon , n_photon = mu.émission(pos[0] , pos[1] , posf[0] , posf[1] , dist ,theta, em = 350)
    
    """ on vérifie si les photon sont absorbé
    et on incrémente a notre tableau vide Absorbé"""
    Absorbé_new = Absorbé.copy()
        
    pos_absorption_x , pos_absorption_y ,t_absorption = detectv(pos_photon[0] , pos_photon[1] ,pos_photon[2], pos_capx , pos_capy , T[i],lambd=50 , eps =0.2 , R = 25*1e-2)

    indice = np.where( (pos_capx == pos_absorption_x) & (pos_capy == pos_absorption_y ) )
        
    if indice[0].size != 0 :
        Temps_Abs[indice[0][0]][indice[1][0]].append(t_absorption)
            
        Absorbé[indice] = Absorbé[indice] + 1
    
    """ on vérifie si ca fait au moins 100 temps que l'on a rien absorbé.
    Si c'est le cas on arrete le code"""
    if (Absorbé_new == Absorbé).all() :
        compteur += 1
#        print(compteur)
    else :
        compteur = 0
    if compteur >=50 :
        break
        
    
    if i % 10 == 0 :
        print(i)
        plt.figure(figsize=(12,12))
        plt.imshow(np.flip(Absorbé,0))
        plt.title("pos x y{} temps{}".format(posf,T[i]))
        plt.show()

    pos = posf
#fini
        
print(Absorbé)
    
plt.figure(figsize=(12,12))
plt.imshow(np.flip(Absorbé,0))
plt.xlabel('capteur en x')
plt.ylabel('capteur en y')
plt.colorbar()
plt.show()
    
