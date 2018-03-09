# -*- coding: utf-8 -*-


import os
from random import randrange
from donnees import *



alphabet = ['a','b','c','d','e','f','g','h','i','j'
,'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def chooseWord():
    
    global liste_mots
    # n contient le nombre des mots disponible
    n = len(liste_mots)
    # k est tiree par hasard
    k = randrange(n)
    mot = liste_mots[k]
    return mot
    
def lettreInput():
    """ cette fonction permet de lire un caractere saisi par le 
    joueur, verifier s'il a bien saisi un caractere """
    lettre = str(input("saisir une lettre : "))
    while not (lettre in alphabet):
        try:
            lettre = str(input("saisir une lettre : "))
            lettre = lettre.lower()
            if len(lettre) != 1 or not (lettre in alphabet) :
                raise TypeError
        except TypeError:
            print("vous dever saisir une et une seul lettre")
