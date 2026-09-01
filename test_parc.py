"""Batterie de référence - conteneur ParcAnimalier (épreuve pension).

Spécification exécutable autoportante : protocoles de conteneur, refus
des doublons et des mauvais types, recherche par code, sous-ensemble des
enclos libres, et comportement sur élément absent.

Programmation Orientée Objet - EICPN 2025-2026.
"""

import unittest

from enclos import Enclos, EnclosChauffe, BassinAquatique
from parc import ParcAnimalier

CODE = "ENCL1234567890ABC"
CODE2 = "CHAU000000000ABCD"
CODE3 = "BASS000000000WXYZ"


def _enclos(code=CODE, nom="Prairie Nord"):
    return Enclos(nom, "Zone Nord", code, 6, 2005)


class TestParcAjout(unittest.TestCase):

    def setUp(self):
        self.parc = ParcAnimalier()

    def test_parc_neuve_est_vide(self):
        self.assertEqual(len(self.parc), 0)

    def test_ajouter_augmente_la_taille(self):
        self.parc.ajouter(_enclos())
        self.assertEqual(len(self.parc), 1)

    def test_ajouter_non_enclos_leve_TypeError(self):
        with self.assertRaises(TypeError):
            self.parc.ajouter("pas un enclos")

    def test_ajouter_doublon_code_leve_ValueError(self):
        self.parc.ajouter(_enclos())
        with self.assertRaises(ValueError):
            self.parc.ajouter(_enclos(nom="Autre nom"))

    def test_sous_types_acceptes(self):
        self.parc.ajouter(_enclos())
        self.parc.ajouter(
            EnclosChauffe("Chenil", "Zone Sud", CODE2, 4, 1890, 3))
        self.parc.ajouter(
            BassinAquatique("Bassin", "Zone Est", CODE3, 4, 2015, 20.0))
        self.assertEqual(len(self.parc), 3)


class TestParcRetrait(unittest.TestCase):

    def setUp(self):
        self.parc = ParcAnimalier()
        self.h = _enclos()
        self.parc.ajouter(self.h)

    def test_retirer_diminue_la_taille(self):
        self.parc.retirer(self.h)
        self.assertEqual(len(self.parc), 0)

    def test_retirer_non_enclos_leve_TypeError(self):
        with self.assertRaises(TypeError):
            self.parc.retirer("pas un enclos")

    def test_retirer_absent_leve_KeyError(self):
        with self.assertRaises(KeyError):
            self.parc.retirer(_enclos(code=CODE2))


class TestParcConteneur(unittest.TestCase):

    def setUp(self):
        self.parc = ParcAnimalier()
        self.h = _enclos()
        self.parc.ajouter(self.h)

    def test_contains_par_objet(self):
        self.assertIn(self.h, self.parc)

    def test_contains_par_code(self):
        self.assertIn(CODE, self.parc)

    def test_contains_absent(self):
        self.assertNotIn(CODE2, self.parc)

    def test_contains_autre_type_retourne_false(self):
        self.assertNotIn(12345, self.parc)

    def test_iteration_ordre_d_ajout(self):
        g = EnclosChauffe("Chenil", "Zone Sud", CODE2, 4, 1890, 3)
        self.parc.ajouter(g)
        codes = [h.code_enclos for h in self.parc]
        self.assertEqual(codes, [CODE, CODE2])


class TestParcMetier(unittest.TestCase):

    def setUp(self):
        self.parc = ParcAnimalier()
        self.h1 = _enclos()
        self.h2 = _enclos(code=CODE2, nom="Prairie Sud")
        self.parc.ajouter(self.h1)
        self.parc.ajouter(self.h2)

    def test_trouver_par_code(self):
        self.assertIs(self.parc.trouver_par_code(CODE), self.h1)

    def test_trouver_par_code_absent_leve_KeyError(self):
        with self.assertRaises(KeyError):
            self.parc.trouver_par_code(CODE3)

    def test_enclos_libres(self):
        self.h1.occuper()
        libres = self.parc.enclos_libres()
        self.assertEqual(libres, [self.h2])

    def test_nombre_libres(self):
        self.assertEqual(self.parc.nombre_libres, 2)
        self.h1.occuper()
        self.assertEqual(self.parc.nombre_libres, 1)


if __name__ == "__main__":
    unittest.main()
