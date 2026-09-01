# parc.py - À COMPLÉTER (épreuve pension)
#
# Conteneur ParcAnimalier, à transposer de Bibliotheque (S12) : enveloppe
# encapsulée d'une liste d'Enclos, exposant len(), in et for.
# Aucune docstring demandée ; les tests (test_parc.py) fixent le
# comportement exact. Complétez les corps « ... ».

from enclos import Enclos


class ParcAnimalier:
    # Garde l'ordre d'ajout, refuse les doublons par code d'enclos, et
    # expose les protocoles de conteneur. La hiérarchie Enclos la traverse
    # sans aucune modification (polymorphisme) : ni isinstance ni cas
    # particulier par sous-type.

    def __init__(self):
        # Collection interne : une liste (préserve l'ordre d'ajout).
        ...

    # --- ajouter, retirer ---

    def ajouter(self, enclos):
        # Refuser un objet qui n'est pas un Enclos (TypeError) et un
        # doublon de code déjà présent (ValueError). Indice : « déjà
        # présent ? » se teste élégamment avec l'opérateur « in » sur self.
        ...

    def retirer(self, enclos):
        # Refuser un non-Enclos (TypeError) ; absent -> KeyError.
        # __eq__ d'Enclos (par code) localise l'élément à retirer.
        ...

    # --- Protocole de conteneur ---

    def __len__(self):
        ...

    def __contains__(self, item):
        # Accepter soit un Enclos (comparé par code via __eq__), soit une
        # chaîne de code. Tout autre type -> False (sans lever).
        ...

    def __iter__(self):
        # Itérer dans l'ordre d'ajout.
        ...

    # --- Méthodes métier ---

    def trouver_par_code(self, code_enclos):
        # Renvoyer l'enclos de ce code ; absent -> KeyError.
        ...

    def enclos_libres(self):
        # Liste des enclos dont libre vaut True, dans l'ordre d'ajout.
        ...

    @property
    def nombre_libres(self):
        ...

    # --- Représentation ---

    def __repr__(self):
        ...
