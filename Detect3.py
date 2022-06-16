#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 12:20:42 2022

@author: tefrem49
"""

import numpy as np

""" Detection des photon par les capteur"""


def absorption(xi,yi,phi,X,Y,t_muon , lambd=50 , eps =0.2 , R = 25*1e-2 ,n= 1.35) :
    """xi et yi : Position initiale photon
    phi : angle de propagation du photon par rapport a l'axe x
    X et Y : tableau de position des  capteurs
    S : distance parcouru par le photon
    d : distance photon - capteur
    pos_cap_traj_x : la position des capteurs en x sur l'itineraire du photon
    pos_cap_traj_y : la position des capteurs en y sur l'itineraire du photon
    n: indice de refraction de l'eau
    t_abs : le temps auquel le photon est aborbe
    """
    
    """Condition sur la longueur de propagation du photon"""
    aleatoire = np.random.rand()
    xlambd = -lambd * np.log(aleatoire) 
    
    #expression analytique de la distance parcouru par le photon
    S = (X-xi)*np.cos(phi) + (Y-yi)*np.sin(phi)
    
    """ on applique la condition sur la longueur de propagation a nos tableaux"""
    cond_propag = np.where(S <= xlambd)
    S = S[cond_propag]
    X = X[cond_propag]
    Y = Y[cond_propag]
    
    #Si S est negatif alors le capteurs est derriere la direction de propagation de notre photon
    #il faut prendre cela en compte
    conds = np.where(S<0) 
    #on a la distance entre le photon et chaque capteur
    d = abs((yi - Y + S*np.sin(phi) ) / np.cos(phi))
    d[conds] = np.sqrt((X[conds]-xi)**2 + (Y[conds]-yi)**2)
    
    
    #on prend que les distance inferieur au rayon du capteur
    cond = np.where(d <= R)
    #et on recupère la position de ces capteurs grace a la condition
    pos_cap_traj_x = X[cond]
    pos_cap_traj_y = Y[cond]
    
    """on determine le temps que met le photon a arriver sur les capteurs
    de sa trajectoire"""
    v= 3*1e8 / n
    t_abs_temp = (S[cond] / v) + t_muon
    

    """ Il faut maintenant voir si le capteur à effectivement absorbe le photon
    """
    Alea = np.random.random(size = pos_cap_traj_x.shape)
    absorb = np.where(Alea <= eps)
    
    """ on à au final un tableau de booleen avec des true si le capteur
    a absorbe le photon et false sinon on va garder uniquement le premier capteur
    qui absorbe le photon
        
    on renvoie au final la position du capteur qui a absorbe donc le premier element
    de la liste des capteurs qui ont absorbe."""

    
    """ On return le premier element de la liste trie en fonction des longueurs"""
    
    
    if pos_cap_traj_x[absorb].size != 0 :
        d = d[cond][absorb]
        res = np.where(np.sort(d)[0] == d)
        
        xabs = pos_cap_traj_x[res]
        yabs = pos_cap_traj_y[res]
        t_abs=t_abs_temp[res]
        return xabs , yabs , t_abs
    else:
        return None , None , None
    

