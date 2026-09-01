# enclos.py - À COMPLÉTER (épreuve pension)
#
# Hiérarchie Enclos / EnclosChauffe / BassinAquatique, à transposer de la
# hiérarchie Livre / LivreNumerique / LivreAudio (S12-S18).
# Pour cette épreuve, aucune docstring n'est demandée : les indices «#»
# donnent le RÔLE (et parfois le cas analogue à transposer), et les
# tests (test_enclos.py) fixent les valeurs et exceptions exactes.
# Complétez les corps « ... ».


class Enclos:
    # ENTITE largement immuable. Identité métier : le code d'enclos (qui
    # ne change jamais, contrairement au nom). Seule l'occupation évolue.
    # Transposé de Livre (identité par ISBN).

    def __init__(self, nom, secteur, code_enclos, capacite_animaux,
                 annee_construction):
        # Valider chaque caractéristique avant de la stocker :
        #   - nom, secteur : chaînes non vides ;
        #   - code : utiliser la méthode de validation dédiée ;
        #   - capacité, année : entiers, bornes exactes dans les tests.
        # Distinguer TypeError (mauvais type) et ValueError (mauvaise valeur).
        # À la création, l'enclos est libre.
        ...

    # --- Propriétés en lecture seule ---

    @property
    def nom(self):
        ...

    @property
    def secteur(self):
        ...

    @property
    def code_enclos(self):
        ...

    @property
    def capacite_animaux(self):
        ...

    @property
    def annee_construction(self):
        ...

    @property
    def libre(self):
        ...

    # --- Méthode statique ---

    @staticmethod
    def code_valide(chaine):
        # Vrai si la chaîne a exactement la bonne longueur et n'est faite
        # que de caractères alphanumériques. Longueur et nature exactes :
        # déductibles des tests. Une entrée non-str renvoie False.
        ...

    # --- Constructeur alternatif ---

    @classmethod
    def depuis_csv(cls, ligne):
        # Découper la ligne, vérifier le nombre de champs, construire via
        # cls(...). Même rôle que Livre.depuis_chaine_csv : utiliser cls
        # (et non Enclos) est ce qui donnera le TYPE EXACT dans les
        # sous-classes.
        ...

    # --- Sérialisation JSON ---

    def to_dict(self):
        # Produire un dict marqué d'un champ « type » (le discriminateur
        # qui guidera la reconstruction). Clés attendues : voir les tests.
        ...

    @classmethod
    def from_dict(cls, donnees):
        # Pendant de to_dict : reconstruire via cls(...), puis restaurer
        # l'occupation par l'API publique (jamais en écrivant l'attribut
        # privé). Même logique que Livre.from_dict.
        ...

    @staticmethod
    def _restaurer_etat(enclos, donnees):
        # Si l'objet était occupé, le replacer dans cet état via la méthode
        # métier. Factorisé : toutes les sous-classes restaurent pareil.
        ...

    # --- Méthodes métier ---

    def occuper(self):
        # Bascule vers « occupé » ; refuser si déjà occupé.
        ...

    def liberer(self):
        # Bascule vers « libre » ; refuser si déjà libre.
        ...

    def fiche_resume(self):
        # Description de la capacité d'un enclos générique. Format exact :
        # voir les tests. (Transposé de Livre.taille_estimee.)
        ...

    # --- Représentations ---

    def __str__(self):
        ...

    def __repr__(self):
        ...

    # --- Identité (entité) ---

    def __eq__(self, autre):
        # Enclos est une ENTITE : égalité par code d'enclos (comme Livre
        # par ISBN). NotImplemented si « autre » n'est pas un Enclos.
        ...

    def __hash__(self):
        # Cohérent avec __eq__ : fondé sur le code d'enclos.
        ...


class EnclosChauffe(Enclos):
    # Enrichit Enclos d'un nombre d'abris. Transposé de LivreNumerique.

    def __init__(self, nom, secteur, code_enclos, capacite_animaux,
                 annee_construction, nombre_abris):
        # Déléguer la validation héritée au parent, puis valider l'attribut
        # propre (nombre d'abris : entier strictement positif).
        ...

    @property
    def nombre_abris(self):
        ...

    @classmethod
    def depuis_csv(cls, ligne):
        # Comme Enclos.depuis_csv, mais un champ de plus (les abris).
        ...

    def to_dict(self):
        # ENRICHIR le dictionnaire hérité du parent (ne pas le réécrire) :
        # corriger « type » et ajouter l'attribut propre. (Geste de
        # LivreNumerique.to_dict.)
        ...

    @classmethod
    def from_dict(cls, donnees):
        ...

    def fiche_resume(self):
        # On REPREND la fiche de base et on la complète : la capacité reste
        # un préfixe (ENRICHISSEMENT). Format exact : voir les tests.
        ...

    def __str__(self):
        ...

    def __repr__(self):
        ...


class BassinAquatique(Enclos):
    # La mesure pertinente est le volume d'eau, pas le nombre d'animaux.
    # Transposé de LivreAudio (durée d'écoute plutôt que pages).

    def __init__(self, nom, secteur, code_enclos, capacite_animaux,
                 annee_construction, volume_m3):
        # Déléguer au parent, puis valider l'attribut propre (volume :
        # nombre strictement positif, stocké en float).
        ...

    @property
    def volume_m3(self):
        ...

    @classmethod
    def depuis_csv(cls, ligne):
        ...

    def to_dict(self):
        ...

    @classmethod
    def from_dict(cls, donnees):
        ...

    def fiche_resume(self):
        # Ici la mesure pertinente n'est PAS le nombre d'animaux : on ne
        # réutilise donc PAS la fiche de base (REMPLACEMENT). Format exact :
        # voir les tests.
        ...

    def __str__(self):
        ...

    def __repr__(self):
        ...
