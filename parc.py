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
        self._enclos = []

    # --- ajouter, retirer ---

    def ajouter(self, enclos):
        # Refuser un objet qui n'est pas un Enclos (TypeError) et un
        # doublon de code déjà présent (ValueError). Indice : « déjà
        # présent ? » se teste élégamment avec l'opérateur « in » sur self.
        if not isinstance(enclos, Enclos):
            raise TypeError("L'enclos à ajouter doit etre une instance d'Enclos.")
        if enclos in self:
            raise ValueError(f"Un enclos avec le code {Enclos.code_enclos} est déjà présent.")
        self._enclos.append(enclos)

    def retirer(self, enclos):
        # Refuser un non-Enclos (TypeError) ; absent -> KeyError.
        # __eq__ d'Enclos (par code) localise l'élément à retirer.
        if not isinstance(enclos, Enclos):
            raise TypeError("L'enclos à retirer doit etre une instance d'enclos.")
        if enclos not in self:
            raise KeyError("L'enclos n'est pas dans le parc.")
        self._enclos.remove(enclos)

    # --- Protocole de conteneur ---

    def __len__(self):
        return len(self._enclos)

    def __contains__(self, item):
        # Accepter soit un Enclos (comparé par code via __eq__), soit une
        # chaîne de code. Tout autre type -> False (sans lever).
        if isinstance(item, Enclos):
            return item in self._enclos
        elif isinstance(item, str):
            return any(i.code_enclos == item for i in self._enclos)
        return False

    def __iter__(self):
        # Itérer dans l'ordre d'ajout.
        return iter(self._enclos)

    # --- Méthodes métier ---

    def trouver_par_code(self, code_enclos):
        # Renvoyer l'enclos de ce code ; absent -> KeyError.
        for i in self._enclos:
            if i.code_enclos == code_enclos:
                return i
        raise KeyError("Aucun enclos trouve avec ce code d'enclos.")

    def enclos_libres(self):
        # Liste des enclos dont libre vaut True, dans l'ordre d'ajout.
        return [i for i in self._enclos if i.libre]

    @property
    def nombre_libres(self):
        return sum(1 for v in self._enclos if v.libre)

    # --- Représentation ---

    def __repr__(self):
        return f"ParcAnimalier(enclos={self._enclos!r})"
