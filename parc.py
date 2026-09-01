# parc.py - À COMPLÉTER
#
# Ce fichier contient la ParcAnimalier : une « boîte » qui contient
# des enclos et sait répondre à des questions comme « combien
# d'enclos ? », « cet enclos est-il présent ? », « lesquels
# sont libres ? ».
#
# Le but est de rendre cette boîte utilisable avec les outils naturels de
# Python :
#   - len(parc)            -> nombre d'enclos   (__len__)
#   - x in parc            -> test de présence        (__contains__)
#   - for h in parc: ...   -> parcours                (__iter__)
#
# Les enclos peuvent être de n'importe quel type de la hiérarchie
# (Enclos, EnclosChauffe, BassinAquatique) : votre code ne doit PAS tester
# le type avec isinstance pour les ranger ou les parcourir. Il les traite
# tous de la même manière.
#
# Les tests (test_parc.py) font foi.

from enclos import Enclos


class ParcAnimalier:
    """Contient des enclos, dans leur ordre d'ajout, sans doublon."""

    def __init__(self):
        # Préparer la collection interne qui gardera les enclos dans
        # l'ordre où on les ajoute.
        ...

    # ------------------------------------------------------------------
    # Ajouter / retirer
    # ------------------------------------------------------------------

    def ajouter(self, enclos):
        # Ajouter un enclos à la parc.
        #   - refuser ce qui n'est pas un Enclos -> TypeError ;
        #   - refuser un doublon, c.-à-d. un enclos de même code déjà
        #     présent -> ValueError.
        # Astuce : « déjà présent ? » se teste élégamment avec
        # « enclos in self » (une fois __contains__ écrit).
        ...

    def retirer(self, enclos):
        # Retirer un enclos de la parc.
        #   - refuser ce qui n'est pas un Enclos -> TypeError ;
        #   - si l'enclos n'est pas présent -> KeyError.
        ...

    # ------------------------------------------------------------------
    # Protocole de conteneur
    # ------------------------------------------------------------------

    def __len__(self):
        # Nombre d'enclos actuellement dans la parc.
        ...

    def __contains__(self, item):
        # Indiquer si « item » est présent. « item » peut être :
        #   - un Enclos (comparé par code grâce à __eq__) ;
        #   - une chaîne de caractères (interprétée comme un code) ;
        #   - toute autre chose -> renvoyer False (sans lever d'erreur).
        ...

    def __iter__(self):
        # Permettre « for h in parc: ... » dans l'ordre d'ajout.
        ...

    # ------------------------------------------------------------------
    # Méthodes métier
    # ------------------------------------------------------------------

    def trouver_par_code(self, code_enclos):
        # Renvoyer l'enclos portant ce code. Si aucun ne correspond,
        # lever KeyError.
        ...

    def enclos_libres(self):
        # Renvoyer la liste des enclos actuellement libres, dans
        # l'ordre d'ajout.
        ...

    @property
    def nombre_libres(self):
        # Nombre d'enclos actuellement libres.
        ...

    # ------------------------------------------------------------------
    # Représentation
    # ------------------------------------------------------------------

    def __repr__(self):
        # Texte court résumant la parc (par exemple son nombre total
        # d'enclos et son nombre de libres).
        ...
