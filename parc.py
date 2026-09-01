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
        self._enclos=[]


    # --- ajouter, retirer ---

    def ajouter(self, enclos):
        # Refuser un objet qui n'est pas un Enclos (TypeError) et un
        # doublon de code déjà présent (ValueError). Indice : « déjà
        # présent ? » se teste élégamment avec l'opérateur « in » sur self.
        if not isinstance(enclos,Enclos):
            raise TypeError("l'objet n'est pa un enclos")
        if enclos in self:
            raise ValueError("l'enclos est deja present")
        self._enclos.append(enclos)


    def retirer(self, enclos):
        # Refuser un non-Enclos (TypeError) ; absent -> KeyError.
        # __eq__ d'Enclos (par code) localise l'élément à retirer.
        if not isinstance(enclos, Enclos):
            raise TypeError("lobjet n'est pas un enclos")
        if enclos not in self:
            raise KeyError("enclos est absent")
        self._enclos.remove(enclos)


    # --- Protocole de conteneur ---

    def __len__(self):
        return len(self._enclos)
    

    def __contains__(self, item):
        # Accepter soit un Enclos (comparé par code via __eq__), soit une
        # chaîne de code. Tout autre type -> False (sans lever).
        if isinstance(item, Enclos):
            return item in self._enclos
        
        elif isinstance (item, str):
            return any(enclos._code_enclos == item for enclos in self._enclos)
        return False
        
    

    def __iter__(self):
        # Itérer dans l'ordre d'ajout.
        return iter(self._enclos)

    # --- Méthodes métier ---

    def trouver_par_code(self, code_enclos):
        # Renvoyer l'enclos de ce code ; absent -> KeyError.
        for enclos in self._enclos:
            if enclos._code_enclos == code_enclos:
                return enclos
        raise KeyError("enclos absent")

    def enclos_libres(self):
        # Liste des enclos dont libre vaut True, dans l'ordre d'ajout.
        return [enclos for enclos in self._enclos if enclos._libre]
    
    @property
    def nombre_libres(self):
        return len(self.enclos_libres())

    # --- Représentation ---

    def __repr__(self):
        return f"ParcAnimalier({self._enclos!r})"
