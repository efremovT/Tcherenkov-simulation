#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 11:17:37 2022

@author: tefrem49
"""
import numpy as np
import bruit as br
"""test proba"""
#xi=5
#yi=-10
#lambd=50
#eps =0.2
#R = 25*1e-2
#n= 1.35
#phi=-np.pi
#
#x = np.arange(0 , 10 , 1)
#y = np.arange(-10 , 10, 2)
#    
#X,Y = np.meshgrid(x,y)
#
#abso= np.zeros(X.shape)
#
##expression analytique
#aléatoire = np.random.rand()
#xlambd = -lambd * np.log(aléatoire) 
#
#
#S = (X-xi)*np.cos(phi) + (Y-yi)*np.sin(phi)
#S = S[np.where(S<xlambd)]
##Si S est négatif alors le capteurs est derriere la direction de propagation de notre photon
##il faut prendre cela en compte
#conds = np.where(S<0) 
##on a la distance entre le photon et chaque capteur
#d = abs((yi - Y + S*np.sin(phi) ) / np.cos(phi))
#d[conds] = np.sqrt((X[conds]-xi)**2 + (Y[conds]-yi)**2)
##on prend que les distance inférieur au rayon du capteur
#cond = np.where(d <= R)
#    
##et on récupère la position de ces capteurs grace a la condition
#pos_cap_traj_x = X[cond]
#pos_cap_traj_y = Y[cond]
#
#print(d[cond])
#
#
#
#cond_absorption_millieu = np.where(d[cond] <= xlambd)
#print(d[cond])
#print(d[cond]<= xlambd)
#pos_cap_traj_x = X[cond][cond_absorption_millieu]
#pos_cap_traj_y = Y[cond][cond_absorption_millieu]
#print(np.sort(d[cond][cond_absorption_millieu]))
#
#Aléa = np.random.random(size = pos_cap_traj_x.shape)
#absorb = np.where(Aléa <= eps)
#
#print(pos_cap_traj_x)
#print(absorb)
#
#
#
#if pos_cap_traj_x[absorb].size != 0 :
#    d = d[cond][cond_absorption_millieu][absorb]
#    res = np.where(np.sort(d)[0] == d)
#    xabs = pos_cap_traj_x[res]
#    yabs = pos_cap_traj_y[res]
#
#print(xabs)
#print(yabs)
#aléatoire = np.random.rand()   
#xlambd = -lambd * np.log(aléatoire) 
#print(xlambd)

# x=np.linspace(0,10,10)
# y=np.linspace(0,1,10)
# X=np.linspace(0,1,10)
# Y=np.linspace(0,1,10)
# R=1

# x_traj = np.meshgrid(x,X)[0]
# y_traj = np.meshgrid(y,X)[0]
    
# x_capteur = np.meshgrid(x,X)[1]
# y_capteur = np.meshgrid(x,Y)[1]
    
# dist = (x_traj - x_capteur)**2 - (y_traj-y_capteur)**2

# dist_traj = dist[np.where(dist <= R**2)]
# print(dist_traj)
# pos_cap_traj_x = x_capteur[np.where(dist <= R**2)]
# pos_cap_traj_y = y_capteur[np.where(dist <= R**2)]
    

#Temps_Abs = [[[n]for n in range(4)]for n in range(4) ]
#print(Temps_Abs[2]==2)

Absorbé=np.load("tab_abs.npy")
temps = float(np.load("temps_final.npy"))


plt.figure(figsize=(4,4))
plt.imshow(np.log(np.flip(Absorbé,0)))
plt.xlabel('capteur en x')
plt.ylabel('capteur en y')
plt.colorbar()
plt.show()


a=bruit(temps,Absorbé)
Absorbé = Absorbé + a

plt.figure(figsize=(4,4))
plt.imshow(np.log(np.flip(Absorbé,0)))
plt.xlabel('capteur en x')
plt.ylabel('capteur en y')
plt.colorbar()
plt.show()

            
print(filtre(Absorbé))