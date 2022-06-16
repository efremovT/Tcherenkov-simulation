#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:22:48 2022

@author: tefrem49
"""

import numpy as np

""" on a un muon qui se deplace et emet des photon à chaque cm de deplacement
"""

#1 Mouvement du muon

def muon(x,y,v, dt ,theta) :
    """ x,y : la position du muon à l'instant t
    v  : la vitesse du muon
    dt : le pas de temps
    theta : l'angle entre l'axe x et la vitesse du muon
    
    
    renvoie la postion du muon à l'instant t+dt
    et la distance qu'il a parcouru"""
    
    pos = [x + v*np.cos(theta)*dt , y + v*np.sin(theta)*dt ] 
    
    dist = np.sqrt(((v*np.sin(theta)*dt )**2) + ((v*np.cos(theta)*dt) **2) )
    
    return pos,dist


# 2 generation des photons  

def emission(xi , yi , xf , yf , dist,  theta, thetac = 41*2*np.pi/360 , em =350 *1e2) :
    """xi , yi : la position initiale du muon a l'instant t
    xf , yf :la position finale du muon à l'instant t+dt
    dist  :la distance parcouru par le muon en dt
    em : le nombre de photon emis par m
    theta : l'angle de propagaton du muon à l'axe x
    thetac : angle de propagation du photon par rapport au muon
    
    la fonction calcule le nombre de photon emis par le muon
    et repartit uniformement ces photons sur la droite entre la position
    initiale et finale tout en calculant leur angle de propagation.
    
    renvoie un tableau des position intiale des photons emis et leurs angle de propagation
    et le nombre de photon emis"""
   
    n_photon = int(dist * em)
    
    xpos_photon = np.linspace(xi,xf,n_photon)
    ypos_photon = np.linspace(yi,yf,n_photon)
    
    rand = np.random.randint(0,high=2,size=n_photon) *2 -1
    thetac= rand*thetac
    thetaf = theta + thetac
    
    pos_photon = [xpos_photon,ypos_photon,thetaf]
    
    return pos_photon , n_photon
    

