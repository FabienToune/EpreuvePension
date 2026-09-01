"""Batterie de référence - objet-valeur TarifPension (épreuve pension).

Spécification exécutable autoportante : égalité et ordre par valeur,
garde de type sur le montant (booléen exclu), addition et comparaison
occupées aux mêmes devises, refus des opérations avec un non-TarifPension.

Programmation Orientée Objet - EICPN 2025-2026.
"""

import unittest

from tarif_pension import TarifPension


class TestTarifPensionConstruction(unittest.TestCase):

    def test_construction_nominale(self):
        t = TarifPension(85.50, "EUR")
        self.assertEqual(t.montant, 85.50)
        self.assertEqual(t.devise, "EUR")

    def test_devise_par_defaut_eur(self):
        self.assertEqual(TarifPension(50).devise, "EUR")

    def test_montant_entier_converti_en_float(self):
        t = TarifPension(85)
        self.assertIsInstance(t.montant, float)
        self.assertEqual(t.montant, 85.0)

    def test_montant_zero_accepte(self):
        self.assertEqual(TarifPension(0).montant, 0.0)

    def test_montant_non_nombre_leve_TypeError(self):
        with self.assertRaises(TypeError):
            TarifPension("85")

    def test_montant_booleen_leve_TypeError(self):
        with self.assertRaises(TypeError):
            TarifPension(True)

    def test_montant_negatif_leve_ValueError(self):
        with self.assertRaises(ValueError):
            TarifPension(-5)

    def test_attributs_en_lecture_seule(self):
        t = TarifPension(85)
        with self.assertRaises(AttributeError):
            t.montant = 90


class TestTarifPensionEgalite(unittest.TestCase):

    def test_egalite_de_valeur(self):
        self.assertEqual(TarifPension(85, "EUR"), TarifPension(85, "EUR"))

    def test_inegalite_montants(self):
        self.assertNotEqual(TarifPension(85, "EUR"), TarifPension(40, "EUR"))

    def test_inegalite_devises(self):
        self.assertNotEqual(TarifPension(85, "EUR"), TarifPension(85, "USD"))

    def test_hash_egal_pour_valeurs_egales(self):
        self.assertEqual(
            hash(TarifPension(85, "EUR")), hash(TarifPension(85, "EUR")))

    def test_utilisable_dans_un_set(self):
        ensemble = {TarifPension(85, "EUR"), TarifPension(85, "EUR"),
                    TarifPension(40, "EUR")}
        self.assertEqual(len(ensemble), 2)

    def test_eq_avec_non_tarif_retourne_notimplemented(self):
        self.assertNotEqual(TarifPension(85), 85)


class TestTarifPensionOrdre(unittest.TestCase):

    def test_inferieur(self):
        self.assertLess(TarifPension(40, "EUR"), TarifPension(85, "EUR"))

    def test_total_ordering_derive_les_autres(self):
        a, b = TarifPension(40, "EUR"), TarifPension(85, "EUR")
        self.assertLessEqual(a, b)
        self.assertGreater(b, a)
        self.assertGreaterEqual(b, a)

    def test_tri_d_une_liste(self):
        tarifs = [TarifPension(85, "EUR"), TarifPension(40, "EUR"),
                  TarifPension(60, "EUR")]
        montants = [t.montant for t in sorted(tarifs)]
        self.assertEqual(montants, [40.0, 60.0, 85.0])

    def test_comparaison_devises_differentes_leve_ValueError(self):
        with self.assertRaises(ValueError):
            TarifPension(85, "EUR") < TarifPension(85, "USD")


class TestTarifPensionAddition(unittest.TestCase):

    def test_addition_meme_devise(self):
        somme = TarifPension(85, "EUR") + TarifPension(40, "EUR")
        self.assertEqual(somme, TarifPension(125, "EUR"))

    def test_addition_retourne_nouvel_objet(self):
        a = TarifPension(85, "EUR")
        somme = a + TarifPension(40, "EUR")
        self.assertIsNot(somme, a)
        self.assertEqual(a.montant, 85.0)

    def test_addition_devises_differentes_leve_ValueError(self):
        with self.assertRaises(ValueError):
            TarifPension(85, "EUR") + TarifPension(40, "USD")

    def test_addition_avec_non_tarif_leve_TypeError(self):
        with self.assertRaises(TypeError):
            TarifPension(85, "EUR") + 40


class TestTarifPensionRepresentation(unittest.TestCase):

    def test_str_deux_decimales(self):
        self.assertEqual(str(TarifPension(85.5, "EUR")), "85.50 EUR")

    def test_repr_reconstructible(self):
        t = TarifPension(85.5, "EUR")
        reconstruit = eval(repr(t), {"TarifPension": TarifPension})
        self.assertEqual(reconstruit, t)


if __name__ == "__main__":
    unittest.main()
