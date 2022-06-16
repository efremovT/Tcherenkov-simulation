#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 09:08:12 2022

@author: tefrem49
"""

import numpy as np



def bruit(temps,Absorbe,freqbruit=5*1e4,c=3*1e8,eff_cap = 0.2) :
     """ temps: temps que met le muons a se deplacer
     freqbruit : le taux de photon de bruit detecter par s
     Absorbe: le tableau des detection"""
     
     proba_bruit = freqbruit * temps
     proba_abs_bruit = proba_bruit * eff_cap
     
     rand = np.random.random(size = Absorbe.shape)
     
     Nphoton = np.zeros(Absorbe.shape)
     Nphoton[rand < proba_abs_bruit] = Nphoton[rand < proba_abs_bruit] + 1
     return Nphoton
    

#

def filtre(Absorbe) :
    cond_photon = np.where(Absorbe >= 3)
    if len(cond_photon[0]) < 5 :
        return(0)
    else :
        """ on teste si tout est sur une meme ligne"""
        x_cond = len(cond_photon[0])
        # Put all array elements in a map
        s_x = set()
        for i in range(0, x_cond):
            s_x.add(cond_photon[0][i])
            
        y_cond = len(cond_photon[1])
        # Put all array elements in a map
        s_y = set()
        for i in range(0, y_cond):
            s_y.add(cond_photon[1][i])
        
        # If all elements are distinct,
        # size of set should be same array.
        if (len(s_x) !=1) and (len(s_y) !=1):
            return(1)
            
        else : 
            return(0)
