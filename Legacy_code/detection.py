#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:44:11 2022

@author: tefrem49
"""

import numpy as np
import Muon as mu
import Capteur as cap

""" Détection des photon par les capteur"""



def absorption(x,y,X,Y , lambd=50 , eps =0.2) :
    """x et y : trajectoire du photon
    X et Y : position des capteurs
    lambd :  la longueur d'absorption
    
    calcul les capteurs qui peuvent absorbé le photon"""
    
    
    """xi yi les positions initiales
    pos_abs la position des capteur sur la trajectoire du photon"""
    xi = x[0]
    yi = y[0]
    
    
    pos_absx = []
    pos_absy = []
    for i in range(0,len(x)) :
        
        """ on verifie si on obtient pas une liste vide"""
        if type(cap.interieur_capteur(x[i],y[i],X,Y,25*1e-2)) == list :
            pos_absx.append(cap.interieur_capteur(x[i],y[i],X,Y,25*1e-2))[0]
            pos_absy.append(cap.interieur_capteur(x[i],y[i],X,Y,25*1e-2))[1]
    
    print(pos_absx)
    if len(pos_absx) == 0 :
        return  None
    
    else :
        xcapt = pos_absx
        ycapt = pos_absy
    
    
        """ verifions si le photon est absorbé 
        pour ce faire on va vérifier la probabilité d'arriver jusqu'au capteur
    
        on va d'abord définir la distance entre le photon et le capteur puis 
        calculer la probabiliter d'arriver jusqu'a cette distance sans se faire
        absorber par le milleu. 
        On rajoutera une condition sur la distance max
        parcouru avant d'avoir 99pourcent de chance de se faire absorbé.(a faire)"""
    
    
        l = np.sqrt((abs(xcapt-xi))**2+(abs(ycapt-yi))**2)#distance photon capteur
        Plambd = np.exp(-l/lambd) 
    
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
        absorb = Aléa < Ptotale
        
        xabs = xcapt[absorb][0]
        yabs = ycapt[absorb][0]
    

        return xabs , yabs




    
    