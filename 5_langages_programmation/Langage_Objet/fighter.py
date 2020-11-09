#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:55:17 2020

@author: yves
"""
from random import randrange
class Fighter:
    """La classe d'un fighter"""
    def __init__(self, name):
        self._name=name
        self._description=''
        self._agility=randrange(1,9)
        self._healthPoints=100 # Lors de la création d'une instance, les points de vie valent 100.
        
    def getName(self):
        """Retourne le nom du combattant."""
        return self._name
    
    def getDescription(self):
        """Retourne la description du combattant."""
        return self._description
    
    def setDescription(self, description):
        """Affecte la description du combattant."""
        self._description=description

    def getAgility(self):
        """Retourne l'agilité du combattant."""
        return self._agility
    
    def getHealthPoints(self):
        """Retourne les points de vie du combattant."""
        return self._healthPoints

    def getStrength(self):
        """Retourne la force du combattant."""
        return 10-self.getAgility()
    
    def punch(self, aFighter):
        """Attaque le combattant aFighter, et affiche les points de vie restants"""
        points=int(10*self.getStrength()/aFighter.getAgility())
        aFighter._healthPoints=aFighter.getHealthPoints()-points
        print(aFighter.getHealthPoints())
        
    def summary(self):
        name='name:'+self.getName()
        description='description:'+self.getDescription()
        agility='agility:%s'%self.getAgility()
        strenght='strenght:%s'%self.getStrength()
        healthPoints='healthPoints:%s'%self.getHealthPoints()
        return '\n'.join([name, description, agility, strenght, healthPoints])
        
    
    
    
       
    
    