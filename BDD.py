"""
Ce code permet de faire fonctionner la BDD du projet
il créera toutes les tables nécessaires au bon fonctionnement du projet
"""

import MobileClass as Mobile
import FixeClass as Fixe

# on crée l'objet fixe
XY = Fixe.Fixe("XY", "rack intelligent", (0,0))
XY.set_MQTTTopic("JuniaLaboRobot/Fixe/XY")
XY.MQTTEnvoieMessage("Bonjour, je suis le rack intelligent")