# tarif_pension.py - À COMPLÉTER (épreuve pension)
#
# Objet-valeur TarifPension, à transposer de l'objet-valeur Argent (S11).
# Pour cette épreuve, aucune docstring n'est demandée : les indices «#»
# donnent le ROLE, et les tests (test_tarif_pension.py) fixent les
# valeurs exactes, l'ordre et les exceptions. Complétez les corps « ... ».

from functools import total_ordering


@total_ordering
class TarifPension:
    # Objet-valeur IMMUABLE : l'égalité ET l'ordre portent sur la VALEUR
    # (montant + devise), pas sur l'identité mémoire. C'est le contraste
    # avec Enclos, qui est une entité (identité par code).

    def __init__(self, montant, devise="EUR"):
        # Refuser un montant strictement négatif ; stocker le montant en float.
        ...

    @property
    def montant(self):
        ...

    @property
    def devise(self):
        ...

    def __eq__(self, autre):
        # Égalité de valeur : même montant ET même devise.
        # Renvoyer NotImplemented si « autre » n'est pas un TarifPension.
        ...

    def __hash__(self):
        # Cohérent avec __eq__ : hacher le couple (montant, devise).
        ...

    def __lt__(self, autre):
        # Comparer deux TarifPension de MÊME devise ; devises différentes
        # -> erreur. Comme Argent : __lt__ + @total_ordering suffisent à
        # dériver tout le reste de l'ordre (<=, >, >=).
        ...

    def __add__(self, autre):
        # Additionner deux TarifPension de MÊME devise -> un NOUVEAU
        # TarifPension. NotImplemented si « autre » n'est pas un
        # TarifPension (l'addition avec un nombre doit échouer, pas
        # réussir silencieusement).
        ...

    def __str__(self):
        ...

    def __repr__(self):
        ...
