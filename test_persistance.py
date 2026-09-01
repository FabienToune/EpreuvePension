"""Batterie de référence - persistance du parc (épreuve pension).

Spécification exécutable autoportante : fabrique pilotée par registre
(type absent ou inconnu -> ValueError), round-trip JSON conservant le
type exact ET l'état libre / occupé, dispatch polymorphe sans isinstance.

Programmation Orientée Objet - EICPN 2025-2026.
"""

import json
import os
import tempfile
import unittest

from enclos import Enclos, EnclosChauffe, BassinAquatique
from persistance import (
    enclos_depuis_dict,
    sauvegarder_parc_json,
    charger_parc_json,
)

CODE = "ENCL1234567890ABC"
CODE2 = "CHAU000000000ABCD"
CODE3 = "BASS000000000WXYZ"


class TestFabrique(unittest.TestCase):

    def test_reconstruit_enclos(self):
        h = Enclos("Prairie", "Zone Nord", CODE, 6, 2005)
        reconstruit = enclos_depuis_dict(h.to_dict())
        self.assertIsInstance(reconstruit, Enclos)
        self.assertEqual(reconstruit, h)

    def test_reconstruit_gite(self):
        g = EnclosChauffe("Chenil", "Zone Sud", CODE2, 4, 1890, 3)
        reconstruit = enclos_depuis_dict(g.to_dict())
        self.assertIsInstance(reconstruit, EnclosChauffe)
        self.assertEqual(reconstruit.nombre_abris, 3)

    def test_reconstruit_bassin(self):
        e = BassinAquatique("Bassin", "Zone Est", CODE3, 4, 2015, 20.0)
        reconstruit = enclos_depuis_dict(e.to_dict())
        self.assertIsInstance(reconstruit, BassinAquatique)
        self.assertEqual(reconstruit.volume_m3, 20.0)

    def test_type_absent_leve_ValueError(self):
        with self.assertRaises(ValueError):
            enclos_depuis_dict({"nom": "Prairie"})

    def test_type_inconnu_leve_ValueError(self):
        with self.assertRaises(ValueError):
            enclos_depuis_dict({"type": "Chateau"})


class TestToDict(unittest.TestCase):

    def test_to_dict_enclos_porte_le_type(self):
        h = Enclos("Prairie", "Zone Nord", CODE, 6, 2005)
        self.assertEqual(h.to_dict()["type"], "Enclos")

    def test_to_dict_gite_enrichit(self):
        g = EnclosChauffe("Chenil", "Zone Sud", CODE2, 4, 1890, 3)
        donnees = g.to_dict()
        self.assertEqual(donnees["type"], "EnclosChauffe")
        self.assertEqual(donnees["nombre_abris"], 3)
        self.assertEqual(donnees["capacite_animaux"], 4)

    def test_to_dict_bassin_enrichit(self):
        e = BassinAquatique("Bassin", "Zone Est", CODE3, 4, 2015, 20.0)
        donnees = e.to_dict()
        self.assertEqual(donnees["type"], "BassinAquatique")
        self.assertEqual(donnees["volume_m3"], 20.0)


class TestRoundTripJson(unittest.TestCase):

    def setUp(self):
        self.dossier = tempfile.mkdtemp()
        self.chemin = os.path.join(self.dossier, "parc.json")

    def test_round_trip_conserve_types_et_valeurs(self):
        parc = [
            Enclos("Prairie", "Zone Nord", CODE, 6, 2005),
            EnclosChauffe("Chenil", "Zone Sud", CODE2, 4, 1890, 3),
            BassinAquatique("Bassin", "Zone Est", CODE3, 4, 2015, 20.0),
        ]
        sauvegarder_parc_json(parc, self.chemin)
        recharge = charger_parc_json(self.chemin)

        self.assertEqual([type(h).__name__ for h in recharge],
                         ["Enclos", "EnclosChauffe", "BassinAquatique"])
        self.assertEqual(recharge[1].nombre_abris, 3)
        self.assertEqual(recharge[2].volume_m3, 20.0)

    def test_round_trip_conserve_etat_reserve(self):
        h = Enclos("Prairie", "Zone Nord", CODE, 6, 2005)
        h.occuper()
        sauvegarder_parc_json([h], self.chemin)
        recharge = charger_parc_json(self.chemin)
        self.assertFalse(recharge[0].libre)

    def test_fichier_est_du_json_valide(self):
        sauvegarder_parc_json(
            [Enclos("Prairie", "Zone Nord", CODE, 6, 2005)], self.chemin)
        with open(self.chemin, encoding="utf-8") as fichier:
            donnees = json.load(fichier)
        self.assertEqual(donnees[0]["type"], "Enclos")


if __name__ == "__main__":
    unittest.main()
