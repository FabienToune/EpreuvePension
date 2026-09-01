# Test de fin de module (seconde session) — Pension et refuge pour animaux

## Rappel : vous pouvez vous servir de vos notes de cours, de vos ateliers, et de toutes autres ressources *utilisées en classe* MAIS PAS : de votre téléphone, ni d'une IA.

## En deux mots

Vous allez écrire, en Python, les classes d'une petite **pension et
refuge pour animaux** : des enclos (enclos chauffés, bassins
aquatiques…), un tarif par jour de pension, un parc qui regroupe le
tout, et de quoi enregistrer puis relire l'ensemble dans un fichier.

Le code à écrire est déjà **structuré pour vous**. Vous ne partez pas
d'une page blanche : chaque fichier contient les classes, les noms de
méthodes et des commentaires qui expliquent ce que chaque partie doit
faire. Votre travail est de **remplacer les `...` par le code attendu**.

Tout est dans ce dépôt : vous n'avez besoin d'aucun autre document.

---

## Ce que vous devez rendre

Quatre fichiers à compléter :

| Fichier            | Ce qu'il contient                                        |
| ------------------ | -------------------------------------------------------- |
| `enclos.py`        | Les classes `Enclos`, `EnclosChauffe`, `BassinAquatique`  |
| `tarif_pension.py` | La classe `TarifPension` (un montant + une devise)        |
| `parc.py`          | La classe `ParcAnimalier` (regroupe des enclos)           |
| `persistance.py`   | L'enregistrement et la relecture en JSON                  |

Les fichiers `test_*.py` et `verifier.py` sont **déjà écrits** : vous n'y
touchez pas. Ils servent à vérifier votre travail.

---

## La règle la plus importante

> **Les tests décrivent EXACTEMENT ce qui est attendu.**

Les fichiers `test_*.py` ne sont pas un piège : ce sont la **consigne
détaillée**, écrite sous forme de code. Pour chaque méthode, ils
indiquent précisément la valeur à renvoyer, les bornes à respecter, le
type d'erreur à lever et le format de texte attendu.

Quand vous hésitez sur un détail, **ouvrez le test correspondant** : la
réponse y est. Et lancez souvent la vérification (voir plus bas) pour
suivre votre progression.

---

## Comment travailler

1. Ouvrez le dossier dans votre éditeur (par exemple VS Code).

2. Complétez les méthodes une par une (commencez par `enclos.py`).

3. À tout moment, dans un terminal ouvert dans ce dossier, lancez :

   ```
   python verifier.py
   ```

   Vous obtenez un bilan lisible : combien de tests passent, et lesquels
   restent à corriger. Recommencez aussi souvent que vous le voulez.

4. Quand tout est au vert, vous avez terminé.

> **Conseil de méthode** : lancez `python verifier.py` *très tôt* et
> *très souvent*, pas seulement à la fin. C'est en voyant les tests
> passer un à un que l'on avance le plus sûrement.

---

## Le domaine, brique par brique

### 1. `Enclos` — la classe de base

Un enclos a un **nom**, un **secteur** (la zone du parc où il se
trouve), un **code d'enclos** (son identité), une **capacité d'accueil**
en animaux et une **année de construction**. Il est **libre** au départ ;
il peut être **occupé** puis de nouveau **libéré**.

Deux enclos qui ont le **même code d'enclos** sont considérés comme le
**même** enclos (c'est son identité). C'est pour cela que l'égalité
(`==`) se fonde sur le code, et pas sur le nom.

### 2. `EnclosChauffe` — un enclos enrichi

Un enclos chauffé **est** un enclos (il en hérite), avec **une
information en plus** : son **nombre d'abris**. On parle
d'**enrichissement** : il réutilise tout ce que fait `Enclos` et **y
ajoute** sa part. Sa fiche reprend la capacité de base **et** la
complète.

### 3. `BassinAquatique` — un enclos où la mesure change

Dans un bassin, les animaux nagent : parler de « places » n'a plus de
sens. La bonne mesure devient le **volume d'eau** (en m³). Ici, la fiche
**ne réutilise pas** la capacité de base : elle la **remplace**. C'est la
différence avec l'enclos chauffé.

### 4. `TarifPension` — un objet-valeur

Un tarif est un **montant** dans une **devise** (par ex. `85.50 EUR`).
Contrairement à un enclos, il n'a pas d'identité : ce qui compte est sa
**valeur**. Deux tarifs de même montant et même devise sont **égaux**.
On peut aussi les **comparer** et les **additionner** (à condition
d'avoir la même devise).

### 5. `ParcAnimalier` — le conteneur

Le parc **regroupe** des enclos. On veut pouvoir écrire naturellement
`len(parc)`, `code in parc`, `for e in parc: ...`. Il traite tous les
types d'enclos de la même façon, **sans jamais tester leur type**.

### 6. `persistance.py` — enregistrer et relire

On enregistre le parc dans un fichier **JSON**, puis on le relit. Le
point clé : à la relecture, **chaque enclos retrouve son type exact**
(un enclos chauffé redevient un `EnclosChauffe`). C'est le champ
`"type"` et le **registre** `_FABRIQUES` qui rendent cela possible.

> **Déjà vu ?** Cette structure (une entité identifiée par un code, des
> sous-classes qui enrichissent ou remplacent, un objet-valeur, un
> conteneur, une persistance JSON) est exactement celle de la
> **bibliothèque** vue en cours et des épreuves précédentes. Le fichier
> **`PARALLELES.md`** met ces domaines côte à côte : le lire avant de
> commencer peut beaucoup vous aider.

---

## Tableau des attentes (spécification)

Les valeurs ci-dessous sont **vérifiées par les tests**. Elles ne sont
pas indicatives : ce sont les attentes exactes.

### `Enclos(nom, secteur, code_enclos, capacite_animaux, annee_construction)`

| Donnée               | Type attendu                | Contrainte                                    | Si le **type** est faux | Si la **valeur** est fausse |
| -------------------- | --------------------------- | --------------------------------------------- | ----------------------- | --------------------------- |
| `nom`                | chaîne                      | non vide                                      | `TypeError`             | `ValueError`                |
| `secteur`            | chaîne                      | non vide                                      | `TypeError`             | `ValueError`                |
| `code_enclos`        | chaîne                      | 17 caractères, lettres et chiffres uniquement | `ValueError`            | `ValueError`                |
| `capacite_animaux`   | entier (booléen **refusé**) | de 1 à 50 inclus                              | `TypeError`             | `ValueError`                |
| `annee_construction` | entier (booléen **refusé**) | de 1800 à 2026 inclus                         | `TypeError`             | `ValueError`                |

> **Cas particulier du code d'enclos.** Contrairement aux autres
> données, le code est entièrement validé par la méthode `code_valide`,
> qui renvoie `False` pour toute entrée incorrecte — y compris une valeur
> qui n'est même pas du texte. Une construction avec un code invalide
> lève donc **`ValueError`** dans tous les cas (et non `TypeError`).

### `EnclosChauffe(... , nombre_abris)`

| Donnée          | Type attendu                | Contrainte          | Type faux   | Valeur fausse |
| --------------- | --------------------------- | ------------------- | ----------- | ------------- |
| `nombre_abris`  | entier (booléen **refusé**) | strictement positif | `TypeError` | `ValueError`  |

### `BassinAquatique(... , volume_m3)`

| Donnée       | Type attendu                                | Contrainte          | Type faux   | Valeur fausse |
| ------------ | ------------------------------------------- | ------------------- | ----------- | ------------- |
| `volume_m3`  | nombre, entier ou réel (booléen **refusé**) | strictement positif | `TypeError` | `ValueError`  |

### `TarifPension(montant, devise="EUR")`

| Donnée    | Type attendu                | Contrainte     | Type faux   | Valeur fausse |
| --------- | --------------------------- | -------------- | ----------- | ------------- |
| `montant` | nombre (booléen **refusé**) | positif ou nul | `TypeError` | `ValueError`  |
| `devise`  | chaîne                      | —              | —           | —             |

### Formats de texte attendus (exemples exacts)

| Méthode                                 | Exemple de résultat                          |
| --------------------------------------- | -------------------------------------------- |
| `Enclos.fiche_resume()`                 | `4 animaux`                                  |
| `EnclosChauffe.fiche_resume()`          | `4 animaux [enclos chauffé, 3 abris]`        |
| `BassinAquatique.fiche_resume()`        | `20.0 m³ de bassin` *(une décimale)*         |
| `TarifPension.__str__` (via `str(...)`) | `85.50 EUR` *(deux décimales)*               |

Le `__repr__` de chaque classe doit être **reconstructible** : recopié
dans du code Python, il doit recréer un objet équivalent. Les tests le
vérifient — inutile de deviner le format, lisez-les.

### Format des lignes CSV (`depuis_csv`)

Les champs sont séparés par des points-virgules `;` :

```
Enclos           : nom;secteur;code;capacite;annee
EnclosChauffe    : nom;secteur;code;capacite;annee;nombre_abris
BassinAquatique  : nom;secteur;code;capacite;annee;volume_m3
```

---

## Quelques notions, en clair

- **Héritage** : `EnclosChauffe` et `BassinAquatique` sont des enclos.
  Ils reçoivent automatiquement ce que fait `Enclos`.
- **`super()`** : depuis une sous-classe, `super()` permet d'appeler le
  travail déjà écrit dans la classe parente, au lieu de le recopier.
- **Enrichir ou remplacer** : un enclos chauffé **enrichit** la fiche de
  base (il la réutilise et ajoute) ; un bassin la **remplace** (il en
  écrit une toute différente). Savoir choisir entre les deux fait partie
  de l'exercice.
- **Objet-valeur** vs **identité** : `TarifPension` se compare par sa
  valeur ; `Enclos` se compare par son identité (le code).
- **`TypeError` ou `ValueError` ?** `TypeError` = la donnée n'est **pas
  du bon type** (un texte au lieu d'un nombre). `ValueError` = le type
  est bon mais la **valeur** ne convient pas (un nombre hors des bornes).
  Les tests vérifient que vous levez **le bon des deux**.

---

## Pièges fréquents (à lire avant de commencer)

Ces points sont vérifiés par les tests. Les garder en tête vous évitera
la plupart des erreurs :

- **En Python, un booléen est un entier.** `True` vaut `1`, `False` vaut
  `0`. Là où l'on attend un « vrai » entier (capacité, année, abris), il
  faut **refuser explicitement** les booléens.
- **`TypeError` n'est pas `ValueError`.** Lisez le test pour savoir
  lequel est attendu dans chaque cas.
- **Les bornes ont deux côtés.** Une capacité de `0` est refusée… mais
  une capacité de `51` aussi. Pensez à la borne **haute** autant qu'à la
  borne basse.
- **Restaurer l'état proprement.** Pour remettre un enclos à « occupé »
  lors d'une relecture, **appelez `occuper()`**. N'écrivez jamais
  l'attribut privé `_libre` directement.
- **Toutes les classes ont `__str__` et `__repr__`.** N'oubliez pas de
  les écrire aussi pour `EnclosChauffe` et `BassinAquatique`, pas
  seulement pour la classe de base.
- **Lancez les tests avant de rendre.** Un simple `python verifier.py`
  révèle immédiatement ce qui ne va pas.
- **Ne versionnez pas les fichiers générés.** Le dossier `__pycache__`
  et les fichiers `.pyc` ne doivent pas être ajoutés (le `.gitignore`
  les exclut déjà).

---

## Comment rendre votre travail (pas à pas avec GitHub)

Le rendu se fait via GitHub. Le principe : vous faites **votre copie**
du dépôt (le *fork*), vous la récupérez **sur votre ordinateur** (le
*clone*), vous travaillez **en local**, vous enregistrez votre
progression au fur et à mesure (*commits*), vous l'envoyez sur GitHub
(*push*), et vous signalez que votre travail est prêt (*pull request*).

Vous pouvez tout faire **en ligne de commande** (les commandes sont
données ci-dessous) **ou** avec une interface graphique (l'onglet
« Source Control » de VS Code, ou l'application GitHub Desktop) : c'est
exactement la même chose, en boutons plutôt qu'en commandes.

### Étape 0 — Une fois pour toutes

- Avoir un **compte GitHub**.
- Avoir **Git installé** sur votre ordinateur (ou utiliser VS Code /
  GitHub Desktop, qui l'incluent).

### Étape 1 — Forker (créer VOTRE copie)

Sur la page de ce dépôt, cliquez sur le bouton **« Fork »** (en haut à
droite). GitHub crée une copie du dépôt **sur votre compte** : c'est la
seule sur laquelle vous avez le droit d'écrire.

### Étape 2 — Cloner (récupérer votre copie en local)

Sur la page de **votre fork**, bouton vert **« Code »**, copiez
l'adresse `https://…`. Puis, dans un terminal :

```
git clone https://github.com/VOTRE-COMPTE/NOM-DU-DEPOT.git
cd NOM-DU-DEPOT
```

Vous avez maintenant le projet sur votre machine, prêt à être ouvert
dans VS Code.

### Étape 3 — Travailler en local

Complétez les fichiers, brique par brique (voir le découpage conseillé
plus bas). Après chaque étape, vérifiez :

```
python verifier.py
```

### Étape 4 — Enregistrer une étape (commit)

Dès qu'une brique passe au vert, enregistrez-la. `git add` choisit ce
qu'on enregistre, `git commit` fige l'étape avec un message clair :

```
git add enclos.py
git commit -m "Classe Enclos complète"
```

Un *commit* est une **photo** de votre travail à un instant donné. En
faire plusieurs, au fil de l'eau, vaut bien mieux qu'un seul gros commit
à la fin (voir ci-dessous).

### Étape 5 — Envoyer sur GitHub (push / sync)

```
git push
```

(ou le bouton **« Sync »** / **« Push »** dans VS Code ou GitHub
Desktop). Vos commits locaux sont maintenant visibles sur votre fork en
ligne.

### Étape 6 — Ouvrir la pull request (le rendu)

Sur la page de **votre fork**, cliquez sur **« Contribute »** puis
**« Open pull request »** (ou l'onglet **« Pull requests »** →
**« New pull request »**).

Vérifiez bien le sens de la demande :

- **base** (la destination) = **ce dépôt-ci**, le dépôt d'origine ;
- **compare** (la source) = **votre fork**.

Validez : votre travail est rendu. Vous avez jusqu'à 21h00 dernier délai

---

## Découpage des commits conseillé

Vous **pouvez** tout enregistrer en un seul commit final, mais c'est
déconseillé. Travailler par petites étapes vous aide à avancer sans vous
perdre, et permet à votre formateur de **suivre votre progression brique
par brique** lors de la correction.

Voici un découpage naturel. À chaque ligne : complétez la partie, lancez
`python verifier.py`, et ne committez **que** lorsque le sous-ensemble
de tests correspondant est au vert.

| #  | Commit (message suggéré)      | Ce que vous complétez                          | Tests qui doivent alors passer                                    |
| -- | ----------------------------- | ---------------------------------------------- | ----------------------------------------------------------------- |
| 1  | `Classe Enclos`               | La classe de base `Enclos` dans `enclos.py`    | `test_enclos.py`, sauf les parties `EnclosChauffe` et `BassinAquatique` |
| 2  | `Sous-classe EnclosChauffe`   | La classe `EnclosChauffe`                      | la classe de test `TestEnclosChauffe`                             |
| 3  | `Sous-classe BassinAquatique` | La classe `BassinAquatique`                    | la classe de test `TestBassinAquatique`                           |
| 4  | `Objet-valeur TarifPension`   | Tout `tarif_pension.py`                        | `test_tarif_pension.py`                                           |
| 5  | `Conteneur ParcAnimalier`     | Tout `parc.py`                                 | `test_parc.py`                                                    |
| 6  | `Persistance JSON`            | Tout `persistance.py`                          | `test_persistance.py`                                             |

Quelques repères :

- `tarif_pension.py` (étape 4) est **indépendant** des autres : vous
  pouvez le traiter quand vous voulez.
- `parc.py` (étape 5) s'appuie sur `Enclos` ; `persistance.py`
  (étape 6) s'appuie sur `to_dict` / `from_dict` : il est donc logique
  de les faire **après** `enclos.py`.
- Après la dernière étape, `python verifier.py` doit afficher
  **110 / 110**.

---

## Comment vous serez évalué

Trois acquis d'apprentissage, qui doivent **tous** être atteints :

- **AA1 — Concevoir et utiliser des objets.** Vos classes sont correctes
  et fonctionnent (les enclos, le tarif, le parc, la persistance).
- **AA2 — Tester.** La batterie de tests fournie passe
  **intégralement**, sans qu'aucun test n'ait été modifié.
- **AA3 — Justifier ses choix.** Vous savez expliquer vos décisions de
  conception (pourquoi une identité par code, pourquoi enrichir ici et
  remplacer là, pourquoi passer par l'API publique pour restaurer un
  état…). Cet acquis a été vérifié tout au long de l'année, notamment à
  l'oral.

Au-delà du seuil de réussite, la qualité du travail est appréciée selon
quatre dimensions : la **cohérence** de l'ensemble, la **précision**
(types d'erreurs, bornes, formats), la bonne **intégration** des notions
du cours (héritage, `super()`, registre…) et votre **autonomie**
(finition, relecture, propreté du dépôt).

Bon travail !
