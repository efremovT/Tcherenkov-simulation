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
import datetime
import bruit as br
from mpl_toolkits.axes_grid1 import make_axes_locatable
import sys

name = int(sys.argv[1])
""" On definis notre tableau de capteur de taille 420m * 240m """
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
            

#plt.figure()
#plt.plot(capteurs[0],capteurs[1] ,'bx')


""" et un tableau vide qui s'incremente pour chaque absorbtion
et un tableau de tableau qui stocke le temps d'arriver de chaque photon"""
Absorbe = capteurs[2]
Temps_Abs = capteurs[3]

""" on definis la position intiale et la direction et la vitesse du muon par 
un tirage aleatoire"""
D = 5 * 50 #marge de distance de creation
xmuon = np.random.uniform(low = pos_capx[0,0] - D , high = pos_capx[0,-1] + D)
ymuon = np.random.uniform(low = pos_capy[0,0] - D , high = pos_capy[-1,0] + D)

# xmuon=20
# ymuon=0

pos = [xmuon,ymuon]


vmuon = 3*1e8
theta = np.random.uniform(low=0,high=2*np.pi) #angle par rapport a x
# theta=np.pi/2
""" on definis le pas de temps et la duree de temps d'etude de sorte qu'a chaque
pas de temps le muon parcoure 2 m et qu'a la fin du temps d'etude il soit eloigne
d'au moins 300 m du detecteur donc qu'il ai parcouru grossièrement 1000m """

#dt = 50/vmuon 
#Tfin = 50/vmuon

dt = 1/vmuon
Tfin = 1000/vmuon
T = np.arange(0,Tfin,dt)

begin_time = datetime.datetime.now()
"""maintenant on fais boucler notr'Non valide'e code pour un pas de temps dt"""
compteur = 0 #compteur d'iteration ou rien ne se passe
for i in range(0,len(T)) :
    
    """ on actualise la positon du muon et on calcule sa distaénce parcouru"""
    posf , dist = mu.muon(pos[0],pos[1],vmuon, dt ,theta)
    """ on caracterise le nombre de photon emis et leurs position"""
    
    pos_photon , n_photon = mu.emission(pos[0] , pos[1] , posf[0] , posf[1] , dist ,theta, em = 350)
    
    """ on verifie si les photon sont Absorbe
    et on incremente a notre tableau vide Absorbe"""
    Absorbe_new = Absorbe.copy()
    for n in range(n_photon) :
        
        pos_absorption_x , pos_absorption_y ,t_absorption = detect.absorption(pos_photon[0][n] , pos_photon[1][n] ,pos_photon[2][n], pos_capx , pos_capy , T[i],lambd=50 , eps =0.2 , R = 25*1e-2)

        indice = np.where( (pos_capx == pos_absorption_x) & (pos_capy == pos_absorption_y ) )
        
        if indice[0].size != 0 :
            Temps_Abs[indice[0][0]][indice[1][0]].append(t_absorption)
            
        Absorbe[indice] = Absorbe[indice] + 1
    


    pos = posf   
    """ on verifie si ca fait au moins 100 temps que l'on a rien Absorbe.
    Si c'est le cas on arrete le code"""
    if (Absorbe_new == Absorbe).all() :
        compteur += 1
#        print(compteur)
    else :
        compteur = 0
    if compteur >=100 :
        break
        
    """ plot dynamique"""
    # if i % 10 == 0 :
    #     print(i)
    #     plt.figure(figsize=(10,10))
    #     plt.imshow(np.flip(Absorbe,0))
    #     plt.title("pos x {}m y {}m temps :{}".format(posf[0],posf[1],T[i]))
    #     plt.show()
#fini
        
""" on a donc Absorbe le tableau du nombre de photon Absorbe par chaque detecteur
et Temps_Abs la nested list du temps auquel est Absorbe les photons sur chaque detecteur""" 
if br.filtre(Absorbe) == 1 :
#    np.save("tab_abs",Absorbe)
#    np.save("temps_final",T[i])
#    
    a=br.bruit(T[i],Absorbe)
    Absorbe_bruit = Absorbe + a
    
    print(Absorbe)
    fig = plt.figure(figsize=(20, 20))
    ax1 = fig.add_subplot(121)
    im1 = ax1.imshow(np.flip(Absorbe,0), interpolation='None')
#    im1 = ax1.imshow(np.log(np.flip(Absorbe,0)), interpolation='None')
    ax1.set_xlabel('capteur en x')
    ax1.set_ylabel('capteur en y')
    ax1.set_title("Trace du muon dans le detecteur sans bruit")
    

    divider = make_axes_locatable(ax1)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im1, cax=cax, orientation='vertical')

    ax2 = fig.add_subplot(122)
    im2 = ax2.imshow(np.flip(Absorbe_bruit,0), interpolation='None')
#    im2 = ax2.imshow(np.log(np.flip(Absorbe_bruit,0)), interpolation='None')
    ax2.set_xlabel('capteur en x')
    ax2.set_ylabel('capteur en y')
    ax2.set_title("Trace du muon dans le detecteur avec bruit")
    
    divider = make_axes_locatable(ax2)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im2, cax=cax, orientation='vertical');
    
    fig.savefig('/mnt/c/projetf/projet_6_f/fig/bam{}'.format(name))
else :
    print("Pas valide")
#    a=br.bruit(T[i],Absorbe)
#    Absorbe_bruit = Absorbe + a

#    fig = plt.figure(figsize=(16, 12))
#    ax1 = fig.add_subplot(121)
#    im1 = ax1.imshow(np.flip(Absorbe,0), interpolation='None')
##    im1 = ax1.imshow(np.log(np.flip(Absorbe,0)), interpolation='None')
#    ax1.set_xlabel('capteur en x')
#    ax1.set_ylabel('capteur en y')
#    ax1.set_title("Trace du muon dans le detecteur sans bruit")
#    
#
#    divider = make_axes_locatable(ax1)
#    cax = divider.append_axes('right', size='5%', pad=0.05)
#    fig.colorbar(im1, cax=cax, orientation='vertical')
#
#    ax2 = fig.add_subplot(122)
#    im2 = ax2.imshow(np.flip(Absorbe_bruit,0), interpolation='None')
##    im2 = ax2.imshow(np.log(np.flip(Absorbe_bruit,0)), interpolation='None')
#    ax2.set_xlabel('capteur en x')
#    ax2.set_ylabel('capteur en y')
#    ax2.set_title("Trace du muon dans le detecteur avec bruit")
#    
#    divider = make_axes_locatable(ax2)
#    cax = divider.append_axes('right', size='5%', pad=0.05)
#    fig.colorbar(im2, cax=cax, orientation='vertical');
#temps de compilation = em * 0.03125 donc 18min pour em = 350*1e2
    
print(datetime.datetime.now() - begin_time)
