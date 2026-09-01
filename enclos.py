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

        #validation des arguments
        if not isinstance(nom,str):
            raise TypeError("le nom doit étre une chaine de caractère")
        if not nom.strip():
            raise ValueError("le nom ne doit pas etre vide")

        if not isinstance(secteur,str):
            raise TypeError("le secteur doit etre une chaine de caractère")

        if not secteur.strip():
            raise ValueError("le secteur ne doit pas etre vide")

        if not Enclos.code_valide(code_enclos):
            raise ValueError("le code d'enclos n'est pas valide")

        if not isinstance(capacite_animaux, int) or isinstance(capacite_animaux,bool):
            raise TypeError("la capacité doit etre un entier")
        if capacite_animaux <=0 or capacite_animaux >50:
            raise ValueError("la capacité doit etre strictement positive")

        if not isinstance(annee_construction,int) or isinstance(annee_construction,bool):
            raise TypeError("l'annee de construction doit etre un entier")

        if annee_construction <1800 or annee_construction > 2026:
            raise ValueError("annee de construction doit etre comprise entere 1800 et 2026")

        #stock des atributs
        self._nom=nom
        self._secteur=secteur
        self._code_enclos=code_enclos
        self._capacite_animaux=capacite_animaux
        self._annee_construction=annee_construction
        self._libre=True
        
        
        
        
        

    # --- Propriétés en lecture seule ---

    @property
    def nom(self):
        """ nom (int) la lectrur seul du nom """
        return self._nom

    @property
    def secteur(self):
        """(int) :  la lecteur seule du secteur"""
        return self._secteur

    @property
    def code_enclos(self):
        """(int) : la lecteur seul du code d'enclos"""
        return self._code_enclos


    @property
    def capacite_animaux(self):
        """(int) : la lecteur seul de la capacité"""
        return self._capacite_animaux


    @property
    def annee_construction(self):
        """(int) : la lecteur seul de l'annee de construction"""
        return self._annee_construction

    @property
    def libre(self):
        """(bool) : la lecteur seul de l'etat"""
        return self._libre

    # --- Méthode statique ---

    @staticmethod
    def code_valide(chaine):
        # Vrai si la chaîne a exactement la bonne longueur et n'est faite
        # que de caractères alphanumériques. Longueur et nature exactes :
        # déductibles des tests. Une entrée non-str renvoie False.
        if not isinstance(chaine, str):
            return False
        return len(chaine) == 17 and chaine.isalnum()

    # --- Constructeur alternatif ---

    @classmethod
    def depuis_csv(cls, ligne):
        # Découper la ligne, vérifier le nombre de champs, construire via
        # cls(...). Même rôle que Livre.depuis_chaine_csv : utiliser cls
        # (et non Enclos) est ce qui donnera le TYPE EXACT dans les
        # sous-classes.
        champs = ligne.split(";")

        if len(champs) != 5:
           raise ValueError("La ligne doit contenir exactement 5 champs separes par ;")

        nom, secteur, code_enclos, capacite_animaux, annee_construction = champs

        return cls(nom,secteur,code_enclos, int(capacite_animaux),int(annee_construction))

    # --- Sérialisation JSON ---

    def to_dict(self):
        # Produire un dict marqué d'un champ « type » (le discriminateur
        # qui guidera la reconstruction). Clés attendues : voir les tests.
        return {
        "type": "Enclos",
        "nom": self._nom,
        "secteur": self._secteur,
        "code_enclos": self._code_enclos,
        "capacite_animaux": self._capacite_animaux,
        "annee_construction": self._annee_construction,
        "libre": self._libre
        }

    @classmethod
    def from_dict(cls, donnees):
        # Pendant de to_dict : reconstruire via cls(...), puis restaurer
        # l'occupation par l'API publique (jamais en écrivant l'attribut
        # privé). Même logique que Livre.from_dict.
        enclos = cls(
        donnees["nom"],
        donnees["secteur"],
        donnees["code_enclos"],
        donnees["capacite_animaux"],
        donnees["annee_construction"]
        )

        cls._restaurer_etat(enclos, donnees)

        return enclos
    
    @staticmethod
    def _restaurer_etat(enclos, donnees):
        # Si l'objet était occupé, le replacer dans cet état via la méthode
        # métier. Factorisé : toutes les sous-classes restaurent pareil.
        if not donnees["libre"]:
           enclos.occuper()
    # --- Méthodes métier ---

    def occuper(self):
        # Bascule vers « occupé » ; refuser si déjà occupé.
        if not self._libre:
           raise ValueError("l'enclos est déjà occupé")

        self._libre = False

    def liberer(self):
        # Bascule vers « libre » ; refuser si déjà libre.
        if self._libre:
           raise ValueError("l'enclos est déjà libre")

        self._libre = True

    def fiche_resume(self):
        # Description de la capacité d'un enclos générique. Format exact :
        # voir les tests. (Transposé de Livre.taille_estimee.)
        return f"{self._capacite_animaux} animaux"

    # --- Représentations ---

    def __str__(self):
        etat = "libre" if self._libre else "occupé"
        return f"{self._nom} ({self._secteur}) - {etat}"

    def __repr__(self):
        return (
        f"Enclos({self._nom!r}, "
        f"{self._secteur!r}, "
        f"{self._code_enclos!r}, "
        f"{self._capacite_animaux!r}, "
        f"{self._annee_construction!r})"
        )

    # --- Identité (entité) ---

    def __eq__(self, autre):
        # Enclos est une ENTITE : égalité par code d'enclos (comme Livre
        # par ISBN). NotImplemented si « autre » n'est pas un Enclos.
        if not isinstance(autre, Enclos):
            return NotImplemented
        return self._code_enclos == autre._code_enclos

    def __hash__(self):
        # Cohérent avec __eq__ : fondé sur le code d'enclos.
        return hash(self._code_enclos)


class EnclosChauffe(Enclos):
    # Enrichit Enclos d'un nombre d'abris. Transposé de LivreNumerique.

    def __init__(self, nom, secteur, code_enclos, capacite_animaux,
                 annee_construction, nombre_abris):
        # Déléguer la validation héritée au parent, puis valider l'attribut
        # propre (nombre d'abris : entier strictement positif).
        super().__init__(nom , secteur , code_enclos , capacite_animaux ,annee_construction)
        if not isinstance(nombre_abris, int) or isinstance(nombre_abris, bool):
            raise TypeError("le nombre doit etre un entier")
        if nombre_abris <=0:
            raise ValueError("le nombre doit etre positif")
        self._nombre_abris = nombre_abris

    @property
    def nombre_abris(self):
        return self._nombre_abris

    @classmethod
    def depuis_csv(cls, ligne):
        # Comme Enclos.depuis_csv, mais un champ de plus (les abris).
        champs=ligne.split(";")
        if len(champs) != 6:
            raise ValueError(" la ligne doit contenir 6 champs ")
        nom, secteur, code_enclos, capacite_animaux, annee_construction ,nombre_abris = champs
        return cls(nom , secteur , code_enclos , int(capacite_animaux), int(annee_construction), int(nombre_abris))


    def to_dict(self):
        # ENRICHIR le dictionnaire hérité du parent (ne pas le réécrire) :
        # corriger « type » et ajouter l'attribut propre. (Geste de
        # LivreNumerique.to_dict.)
        donnees = super().to_dict()
        donnees["type"] = "EnclosChauffe"
        donnees["nombre_abris"] = self._nombre_abris
        return donnees

    @classmethod
    def from_dict(cls, donnees):
        enclos = cls(
        donnees["nom"],
        donnees["secteur"],
        donnees["code_enclos"],
        donnees["capacite_animaux"],
        donnees["annee_construction"],
        donnees["nombre_abris"]
    )

        cls._restaurer_etat(enclos, donnees)

        return enclos

    def fiche_resume(self):
        # On REPREND la fiche de base et on la complète : la capacité reste
        # un préfixe (ENRICHISSEMENT). Format exact : voir les tests.
        return f"{super().fiche_resume()} [enclos chauffé, {self._nombre_abris} abris]"

    def __str__(self):
        return f"{super().__str__()} - {self._nombre_abris} abris"

    def __repr__(self):
        return (
                f"EnclosChauffe({self._nom!r}, "
                f"{self._secteur!r}, "
                f"{self._code_enclos!r}, "
                f"{self._capacite_animaux!r}, "
                f"{self._annee_construction!r}, "
                f"{self._nombre_abris!r})"
                )
        


class BassinAquatique(Enclos):
    # La mesure pertinente est le volume d'eau, pas le nombre d'animaux.
    # Transposé de LivreAudio (durée d'écoute plutôt que pages).

    def __init__(self, nom, secteur, code_enclos, capacite_animaux,
                 annee_construction, volume_m3):
        # Déléguer au parent, puis valider l'attribut propre (volume :
        # nombre strictement positif, stocké en float).
        super().__init__(nom , secteur , code_enclos , capacite_animaux ,annee_construction)
        if not isinstance(volume_m3, (int,float)) or isinstance(volume_m3, bool):
            raise TypeError("le volume doit etre un nombre")
        if volume_m3 <=0:
            raise ValueError(" le nombre doit etre strictment positif")

        self._volume_m3 = float(volume_m3)


    @property
    def volume_m3(self):
        return self._volume_m3

    @classmethod
    def depuis_csv(cls, ligne):
        champs= ligne.split(";")
        if len(champs)!=6:
            raise ValueError("la ligne doit contenir 6 champs")

        nom , secteur , code_enclos , capacite_animaux , annee_construction , volume_m3 = champs
        return cls( nom , secteur , code_enclos , int(capacite_animaux) , int(annee_construction),float(volume_m3))

    def to_dict(self):
        donnees= super().to_dict()
        donnees["type"]="BassinAquatique"
        donnees["volume_m3"]=self._volume_m3
        return donnees

         

    @classmethod
    def from_dict(cls, donnees):
        enclos = cls(
        donnees["nom"],
        donnees["secteur"],
        donnees["code_enclos"],
        donnees["capacite_animaux"],
        donnees["annee_construction"],
        donnees["volume_m3"]
        )
        
        cls._restaurer_etat(enclos, donnees)
        
        return enclos

    def fiche_resume(self):
        # Ici la mesure pertinente n'est PAS le nombre d'animaux : on ne
        # réutilise donc PAS la fiche de base (REMPLACEMENT). Format exact :
        # voir les tests.
        return f"{self._volume_m3} m³ de bassin"

    def __str__(self):
        etat = "libre" if self._libre else "occupé"
        return f"{self._nom} ({self._secteur}) - {etat} - {self._volume_m3} m³ de bassin"

    def __repr__(self):
            return (
            f"BassinAquatique({self._nom!r}, "
            f"{self._secteur!r}, "
            f"{self._code_enclos!r}, "
            f"{self._capacite_animaux!r}, "
            f"{self._annee_construction!r}, "
            f"{self._volume_m3!r})"
                            )
        
