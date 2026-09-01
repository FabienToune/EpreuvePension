# persistance.py - À COMPLÉTER
#
# Ce fichier sait ENREGISTRER une parc dans un fichier JSON et la
# RELIRE plus tard. Le point délicat : quand on relit le fichier, chaque
# enclos doit retrouver son TYPE EXACT d'origine (un EnclosChauffe redevient
# un EnclosChauffe, un BassinAquatique redevient un BassinAquatique).
#
# Pour cela, on s'appuie sur le champ "type" écrit par to_dict, et sur un
# REGISTRE qui associe chaque nom de type à sa classe. Ajouter un nouveau
# type d'enclos demain ne demandera qu'une ligne dans ce registre,
# sans rien changer d'autre.
#
# Remarque : c'est ICI qu'on importe json et qu'on touche aux fichiers.
# Le fichier enclos.py, lui, ne s'occupe JAMAIS de fichiers ni de
# JSON : chaque fichier a son rôle.
#
# Les tests (test_persistance.py) font foi.

import json

from enclos import Enclos, EnclosChauffe, BassinAquatique


# Registre « nom de type -> classe ».
# À COMPLÉTER : associez chaque valeur possible du champ "type" à la
# classe correspondante.
_FABRIQUES = {
    ...
}


def enclos_depuis_dict(donnees):
    # À partir d'un dictionnaire (issu de to_dict), recréer le bon type
    # d'enclos :
    #   - lire le champ "type" ;
    #   - si ce type est absent ou inconnu du registre -> ValueError ;
    #   - sinon, déléguer la reconstruction à la méthode from_dict de la
    #     classe trouvée dans le registre.
    ...


# ----------------------------------------------------------------------
# Enregistrement et lecture au format JSON
# ----------------------------------------------------------------------

def sauvegarder_parc_json(enclos, chemin):
    # Transformer chaque enclos en dictionnaire (chacun sait le faire
    # via to_dict, sans qu'on ait à tester son type), puis écrire la liste
    # obtenue dans le fichier « chemin » au format JSON.
    ...


def charger_parc_json(chemin):
    # Lire le fichier JSON « chemin », puis reconstruire chaque enclos
    # avec enclos_depuis_dict. Renvoyer la liste des enclos,
    # chacun ayant retrouvé son type exact d'origine.
    ...
