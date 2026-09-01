# persistance.py - À COMPLÉTER (épreuve pension)
#
# Persistance du parc, à transposer de catalogue_persistance (S18).
# Les FONCTIONS de ce module orchestrent fichiers et format (JSON) ; ce
# sont les CLASSES (to_dict / from_dict) qui connaissent leurs attributs.
# Le module enclos, lui, n'importe pas json.
# Aucune docstring demandée ; test_persistance.py fixe le comportement.
# Complétez les corps « ... ».

import json

from enclos import Enclos, EnclosChauffe, BassinAquatique


# Registre de reconstruction : associe le discriminateur « type » à la
# classe. Le compléter est ce qui rend la reconstruction polymorphe
# possible. Comme la fabrique du catalogue de livres, il illustre le
# principe ouvert/fermé : ajouter un type = une ligne ici, sans toucher
# à la fabrique (vs une cascade if/elif à éditer en son cœur).
_FABRIQUES = {
    "Enclos" : Enclos,
    "EnclosChauffe" : EnclosChauffe,
    "BassinAquatique" : BassinAquatique,
    }


def enclos_depuis_dict(donnees):
    # Lire le champ « type », choisir la classe dans le registre, puis
    # déléguer à sa classmethod from_dict. Type absent ou inconnu -> erreur.
    # Même rôle que livre_depuis_dict.
    type_enclos = donnees.get("type")
    if type_enclos not in _FABRIQUES:
        raise ValueError(f"Type d'enclos inconnu : {type_enclos!r}")
    classe = _FABRIQUES[type_enclos]
    return classe.from_dict(donnees)


# --- Persistance JSON ---

def sauvegarder_parc_json(enclos, chemin):
    # Transformer chaque enclos par SON to_dict (dispatch polymorphe,
    # sans test de type), puis écrire la liste de dicts en JSON.
    donnees = [enclos.to_dict() for enclos in enclos]
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)


def charger_parc_json(chemin):
    # Relire le JSON et confier chaque dict à la fabrique, qui restitue le
    # type exact d'origine. Un parc mélangé revient à l'identique.
    with open(chemin, "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)
    return [enclos_depuis_dict(entree) for entree in donnees]
