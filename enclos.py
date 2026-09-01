# enclos.py - À COMPLÉTER
#
# Ce fichier contient la hiérarchie d'enclos de la pension
# animalière : la classe de base Enclos et ses deux sous-classes
# EnclosChauffe et BassinAquatique.
#
# Votre travail : remplacer chaque « ... » par le code attendu. La forme
# des classes (noms, signatures, propriétés) est déjà posée pour vous ;
# il vous reste à écrire l'intérieur des méthodes.
#
# RÈGLE D'OR : les fichiers test_*.py décrivent EXACTEMENT ce qui est
# attendu (valeurs de retour, bornes, types d'erreurs, formats de texte).
# Ils sont la référence. En cas de doute, lisez le test correspondant et
# lancez « python verifier.py » pour voir où vous en êtes.


class Enclos:
    """Un enclos de la pension animalière.

    Un enclos est identifié de façon unique par son CODE
    D'ENCLOS (deux enclos de même code sont considérés comme le
    même enclos, même si leur nom diffère). Ses caractéristiques
    sont fixées une fois pour toutes à la création ; seul l'état
    « libre / occupé » change ensuite.
    """

    def __init__(self, nom, secteur, code_enclos, capacite_animaux,
                 annee_construction):
        # Vérifier chaque information reçue AVANT de la ranger dans l'objet.
        #
        # Deux familles d'erreurs à distinguer :
        #   - mauvais TYPE  -> lever TypeError
        #     (exemple : une capacité donnée sous forme de texte) ;
        #   - bon type mais mauvaise VALEUR -> lever ValueError
        #     (exemple : une capacité égale à 0).
        #
        # À contrôler, dans l'ordre :
        #   - nom et secteur : des chaînes de caractères, non vides ;
        #   - code_enclos : valide au sens de code_valide (plus bas) ;
        #     si le code n'est pas valide, lever ValueError ;
        #   - capacite_animaux : un entier (PAS un booléen) dans les
        #     bornes indiquées par l'énoncé et les tests ;
        #   - annee_construction : un entier (PAS un booléen) dans les
        #     bornes indiquées par l'énoncé et les tests.
        #
        # Astuce : en Python, True et False sont aussi des entiers. Il faut
        # donc les refuser explicitement là où on attend un « vrai » entier.
        #
        # Une fois TOUTES les vérifications passées : ranger chaque valeur
        # dans un attribut privé (préfixe « _ ») et marquer l'enclos
        # comme libre.
        ...

    # ------------------------------------------------------------------
    # Propriétés en lecture seule
    # ------------------------------------------------------------------
    # Chaque propriété donne accès EN LECTURE à l'attribut privé
    # correspondant. Aucune ne permet de modifier l'objet (pas de setter) :
    # un enclos est immuable, sauf pour son état libre / occupé.

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

    # ------------------------------------------------------------------
    # Méthode statique
    # ------------------------------------------------------------------

    @staticmethod
    def code_valide(chaine):
        # Renvoyer True si « chaine » est un code de réservation valide,
        # False sinon. Un code valide est une chaîne de caractères d'une
        # longueur précise, composée uniquement de lettres et de chiffres.
        # La longueur exacte et la nature des caractères sont fixées par
        # les tests. Une valeur qui n'est même pas une chaîne renvoie False
        # (et ne lève pas d'erreur).
        ...

    # ------------------------------------------------------------------
    # Constructeur alternatif
    # ------------------------------------------------------------------

    @classmethod
    def depuis_csv(cls, ligne):
        # Construire un enclos à partir d'une ligne de texte dont les
        # champs sont séparés par des points-virgules « ; ».
        # Vérifier d'abord que le nombre de champs est correct (sinon
        # ValueError), puis appeler le constructeur.
        #
        # Important : utiliser cls(...) et NON Enclos(...). C'est ce
        # qui permettra aux sous-classes (EnclosChauffe, BassinAquatique) de
        # réutiliser cette logique en créant le bon type.
        ...

    # ------------------------------------------------------------------
    # Sérialisation (transformation en dictionnaire)
    # ------------------------------------------------------------------

    def to_dict(self):
        # Renvoyer un dictionnaire décrivant l'enclos, prêt à être
        # enregistré en JSON. Ce dictionnaire contient un champ "type" qui
        # mémorise le nom de la classe : il servira plus tard à recréer le
        # bon type d'objet. Les noms exacts des clés sont donnés par les
        # tests.
        ...

    @classmethod
    def from_dict(cls, donnees):
        # Opération inverse de to_dict : recréer un enclos à partir
        # d'un dictionnaire. Construire l'objet via cls(...), puis
        # restaurer son état libre / occupé.
        #
        # Pour restaurer l'état, passer par la MÉTHODE prévue (voir
        # _restaurer_etat), jamais en modifiant directement l'attribut
        # privé.
        ...

    @staticmethod
    def _restaurer_etat(enclos, donnees):
        # Si le dictionnaire indique que l'enclos était occupé, le
        # replacer dans cet état EN APPELANT la méthode métier prévue à cet
        # effet (et non en écrivant l'attribut privé « à la main »).
        # Cette aide est commune à toutes les sous-classes.
        ...

    # ------------------------------------------------------------------
    # Méthodes métier (changement d'état)
    # ------------------------------------------------------------------

    def occuper(self):
        # Faire passer l'enclos de « libre » à « occupé ».
        # S'il est déjà occupé, lever ValueError.
        ...

    def liberer(self):
        # Faire passer l'enclos de « occupé » à « libre ».
        # S'il est déjà libre, lever ValueError.
        ...

    def fiche_resume(self):
        # Renvoyer une courte description de la CAPACITÉ d'accueil.
        # Pour un enclos générique, l'unité naturelle est la personne.
        # Le format exact est donné par les tests (voir l'énoncé pour un
        # exemple).
        ...

    # ------------------------------------------------------------------
    # Représentations textuelles
    # ------------------------------------------------------------------

    def __str__(self):
        # Texte lisible par un humain, qui mentionne notamment l'état
        # actuel (libre ou occupé). Format précisé par les tests/énoncé.
        ...

    def __repr__(self):
        # Texte « technique » qui, recopié tel quel dans du code Python,
        # permettrait de reconstruire un enclos équivalent. Format
        # précisé par les tests (il est vérifié qu'il est reconstructible).
        ...

    # ------------------------------------------------------------------
    # Identité (égalité et hachage)
    # ------------------------------------------------------------------

    def __eq__(self, autre):
        # Deux enclos sont égaux s'ils ont le MÊME code de
        # réservation. Si « autre » n'est pas un Enclos, renvoyer
        # NotImplemented (et non False) pour laisser Python gérer le cas.
        ...

    def __hash__(self):
        # Doit être cohérent avec __eq__ : fondé sur le code d'enclos.
        # (Nécessaire pour utiliser un enclos dans un set ou comme clé
        # de dictionnaire.)
        ...


class EnclosChauffe(Enclos):
    """Un enclos chauffé : un enclos AVEC, en plus, un nombre d'abris.

    Un enclos chauffé est un enclos comme un autre, auquel on AJOUTE une
    information (le nombre d'abris). On parle d'ENRICHISSEMENT : il
    réutilise tout ce que fait Enclos, et y ajoute sa part.
    """

    def __init__(self, nom, secteur, code_enclos, capacite_animaux,
                 annee_construction, nombre_abris):
        # 1) Laisser la classe parente valider et ranger les attributs
        #    communs (utiliser super()).
        # 2) Valider ensuite l'attribut PROPRE : nombre_abris
        #    doit être un entier (PAS un booléen) strictement positif.
        #    Mauvais type -> TypeError ; mauvaise valeur -> ValueError.
        # 3) Ranger nombre_abris dans un attribut privé.
        ...

    @property
    def nombre_abris(self):
        ...

    @classmethod
    def depuis_csv(cls, ligne):
        # Comme Enclos.depuis_csv, mais avec un champ de plus
        # (le nombre d'abris). Adapter le nombre de champs attendu.
        ...

    def to_dict(self):
        # ENRICHIR le dictionnaire du parent au lieu de tout réécrire :
        #   - récupérer le dictionnaire de base via super() ;
        #   - corriger le champ "type" ;
        #   - y ajouter le nombre d'abris.
        ...

    @classmethod
    def from_dict(cls, donnees):
        # Recréer un enclos chauffé à partir d'un dictionnaire, puis
        # restaurer son état (même principe que pour Enclos.from_dict).
        ...

    def fiche_resume(self):
        # ENRICHISSEMENT : on REPREND la fiche de base (la capacité reste
        # pertinente pour un enclos chauffé) et on la complète avec le
        # nombre d'abris. Réutiliser le travail du parent via super(). Format
        # exact donné par les tests / l'énoncé.
        ...

    def __str__(self):
        # Reprendre le texte du parent et le compléter. Format donné par
        # les tests / l'énoncé.
        ...

    def __repr__(self):
        # Comme pour Enclos, mais en incluant le nombre d'abris.
        # Doit rester reconstructible.
        ...


class BassinAquatique(Enclos):
    """Un bassin aquatique : la bonne mesure est le VOLUME d'eau.

    Dans un bassin, les animaux nagent : compter des « places » n'a plus
    de sens. La capacité de base n'est donc plus la mesure naturelle ; on
    la REMPLACE par le volume d'eau (en m³). C'est la différence avec
    l'enclos chauffé : ici, fiche_resume ne réutilise PAS la fiche de
    base, elle la remplace.
    """

    def __init__(self, nom, secteur, code_enclos, capacite_animaux,
                 annee_construction, volume_m3):
        # 1) Laisser la classe parente valider et ranger les attributs
        #    communs (super()).
        # 2) Valider l'attribut PROPRE : volume_m3 doit être un nombre
        #    (entier ou réel, mais PAS un booléen) strictement positif.
        #    Mauvais type -> TypeError ; mauvaise valeur -> ValueError.
        # 3) Ranger le volume dans un attribut privé, sous forme de
        #    nombre réel (float).
        ...

    @property
    def volume_m3(self):
        ...

    @classmethod
    def depuis_csv(cls, ligne):
        # Comme Enclos.depuis_csv, mais avec un champ de plus
        # (le volume). Adapter le nombre de champs attendu.
        ...

    def to_dict(self):
        # ENRICHIR le dictionnaire du parent : récupérer la base via
        # super(), corriger "type", ajouter le volume.
        ...

    @classmethod
    def from_dict(cls, donnees):
        # Recréer un bassin à partir d'un dictionnaire, puis restaurer
        # son état.
        ...

    def fiche_resume(self):
        # REMPLACEMENT : ici on N'UTILISE PAS la fiche de base. On décrit
        # le volume d'eau du bassin. Format exact donné par les tests /
        # l'énoncé (attention au nombre de décimales).
        ...

    def __str__(self):
        # Reprendre le texte du parent et le compléter avec la description
        # du bassin. Format donné par les tests / l'énoncé.
        ...

    def __repr__(self):
        # Comme pour Enclos, mais en incluant le volume. Doit rester
        # reconstructible.
        ...
