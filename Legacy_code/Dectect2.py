#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:49:55 2022

@author: tefrem49
"""

"""
Created on Thu Mar 17 10:44:11 2022

@author: tefrem49
"""

import numpy as np

""" Détection des photon par les capteur"""

def absorption(x,y,X,Y , lambd=50 , eps =0.2 , R = 25*1e-2) :
    """x et y : trajectoire du photon de taille Ntrajectoire
    X et Y : position des capteurs de tailles Ncapteur
    lambd :  la longueur d'absorption
    eps: l'efficacité du capteur
    R : rayon des capteurs
    
    calcul les capteurs qui peuvent absorbé le photon
    
    dist la liste des distance aux capteurs, de taille Ncapteur * Ntrajectoire"""
    
    x_traj = np.meshgrid(x,X)[0]
    y_traj = np.meshgrid(y,Y)[0]
    
    x_capteur = np.meshgrid(x,X)[1]
    y_capteur = np.meshgrid(x,Y)[1]
    
    dist = (x_traj - x_capteur)**2 + (y_traj-y_capteur)**2
    
    dist_traj = dist[np.where(dist <= R**2)]
    pos_cap_traj_x = x_capteur[np.where(dist <= R**2)]
    pos_cap_traj_y = y_capteur[np.where(dist <= R**2)]
    
    
    
    """ verifions si le photon est absorbé 
    pour ce faire on va vérifier la probabilité d'arriver jusqu'au capteur
    
    on va d'abord définir la distance entre le photon et le capteur puis 
    calculer la probabiliter d'arriver jusqu'a cette distance sans se faire
    absorber par le milleu. 
    On rajoutera une condition sur la distance max
    parcouru avant d'avoir 99pourcent de chance de se faire absorbé.(a faire)"""


    
    Plambd = np.exp(-dist_traj/lambd) 
    
    """ on a maintenant la proba d'etre arriver en chaque capteur
    chaque capteur a une proba eps de capter le photon

    On va combiner les proba Plambd et eps pour savoir la probabilité de se 
    faire absorbé."""
        
    Ptotale = Plambd * eps
        
    """ Il faut maintenant voir si le capteur à effectivement absorbé le photon
    """
    Aléa = np.random.randint(0,high=1, size = len(Ptotale))
        
    """ on à au final un tableau de booléen avec des true si le capteur
    a absorbé le photon et false sinon on va garder uniquement le premier capteur
    qui absorbe le photon , par chance le tableau de l est déja trié par distance
    car on parcoure la trajectoire de manière croissante.
        
    on renvoie au final la position du capteur qui a absorbé donc le premier element
    de la liste des capteurs qui ont absorbé."""
    absorb = np.where(Aléa < Ptotale)
    
    if pos_cap_traj_x[absorb].size != 0 :
        xabs = pos_cap_traj_x[absorb][0]
        yabs = pos_cap_traj_y[absorb][0]
    else:
        xabs=-1000
        yabs=-10000
    
    return xabs , yabs

