"""Batterie de référence - hiérarchie Enclos (épreuve pension).

Spécification exécutable AUTOPORTANTE : tout ce qui est attendu est
testé ici, y compris les types d'exceptions, les bornes hautes ET
basses, le rejet du booléen, et les représentations de TOUTES les
classes. Aucun attendu n'est laissé implicite.

Programmation Orientée Objet - EICPN 2025-2026.
"""

import unittest

from enclos import Enclos, EnclosChauffe, BassinAquatique

CODE = "ENCL1234567890ABC"
CODE2 = "CHAU000000000ABCD"
CODE3 = "BASS000000000WXYZ"


class TestCodeValide(unittest.TestCase):
    """Validation statique du code de réservation."""

    def test_code_valide_accepte_17_alphanum(self):
        self.assertTrue(Enclos.code_valide("ENC4567890123DEFG"))

    def test_code_valide_refuse_trop_court(self):
        self.assertFalse(Enclos.code_valide("ABC123"))

    def test_code_valide_refuse_trop_long(self):
        self.assertFalse(Enclos.code_valide("A" * 18))

    def test_code_valide_refuse_non_alphanumerique(self):
        self.assertFalse(Enclos.code_valide("ENCL-234567890ABC"))

    def test_code_valide_refuse_non_str(self):
        self.assertFalse(Enclos.code_valide(12345678901234567))


class TestEnclosConstruction(unittest.TestCase):
    """Construction nominale et lecture des attributs."""

    def test_construction_nominale(self):
        h = Enclos("Prairie Nord", "Zone Nord", CODE, 6, 2005)
        self.assertEqual(h.nom, "Prairie Nord")
        self.assertEqual(h.secteur, "Zone Nord")
        self.assertEqual(h.code_enclos, CODE)
        self.assertEqual(h.capacite_animaux, 6)
        self.assertEqual(h.annee_construction, 2005)

    def test_neuf_est_libre(self):
        h = Enclos("Prairie Nord", "Zone Nord", CODE, 6, 2005)
        self.assertTrue(h.libre)

    def test_attributs_en_lecture_seule(self):
        h = Enclos("Prairie Nord", "Zone Nord", CODE, 6, 2005)
        with self.assertRaises(AttributeError):
            h.nom = "Autre"
        with self.assertRaises(AttributeError):
            h.capacite_animaux = 8


class TestEnclosValidationTypes(unittest.TestCase):
    """Distinction stricte TypeError (type) / ValueError (valeur)."""

    def test_nom_non_str_leve_TypeError(self):
        with self.assertRaises(TypeError):
            Enclos(123, "Zone Nord", CODE, 6, 2005)

    def test_nom_vide_leve_ValueError(self):
        with self.assertRaises(ValueError):
            Enclos("   ", "Zone Nord", CODE, 6, 2005)

    def test_secteur_non_str_leve_TypeError(self):
        with self.assertRaises(TypeError):
            Enclos("Prairie", 456, CODE, 6, 2005)

    def test_secteur_vide_leve_ValueError(self):
        with self.assertRaises(ValueError):
            Enclos("Prairie", "", CODE, 6, 2005)

    def test_code_invalide_leve_ValueError(self):
        with self.assertRaises(ValueError):
            Enclos("Prairie", "Zone Nord", "TROP_COURT", 6, 2005)

    def test_capacite_non_int_leve_TypeError(self):
        with self.assertRaises(TypeError):
            Enclos("Prairie", "Zone Nord", CODE, 6.0, 2005)

    def test_capacite_booleen_leve_TypeError(self):
        with self.assertRaises(TypeError):
            Enclos("Prairie", "Zone Nord", CODE, True, 2005)

    def test_capacite_zero_leve_ValueError(self):
        with self.assertRaises(ValueError):
            Enclos("Prairie", "Zone Nord", CODE, 0, 2005)

    def test_capacite_au_dessus_borne_leve_ValueError(self):
        with self.assertRaises(ValueError):
            Enclos("Prairie", "Zone Nord", CODE, 51, 2005)

    def test_capacite_borne_haute_acceptee(self):
        h = Enclos("Prairie", "Zone Nord", CODE, 50, 2005)
        self.assertEqual(h.capacite_animaux, 50)

    def test_annee_non_int_leve_TypeError(self):
        with self.assertRaises(TypeError):
            Enclos("Prairie", "Zone Nord", CODE, 6, "2005")

    def test_annee_booleen_leve_TypeError(self):
        with self.assertRaises(TypeError):
            Enclos("Prairie", "Zone Nord", CODE, 6, True)

    def test_annee_sous_borne_leve_ValueError(self):
        with self.assertRaises(ValueError):
            Enclos("Prairie", "Zone Nord", CODE, 6, 1799)

    def test_annee_au_dessus_borne_leve_ValueError(self):
        with self.assertRaises(ValueError):
            Enclos("Prairie", "Zone Nord", CODE, 6, 2027)

    def test_annee_bornes_acceptees(self):
        self.assertEqual(
            Enclos("V", "D", CODE, 6, 1800).annee_construction, 1800)
        self.assertEqual(
            Enclos("V", "D", CODE, 6, 2026).annee_construction, 2026)


class TestEnclosMetier(unittest.TestCase):
    """Cycle de vie libre / occupé."""

    def setUp(self):
        self.h = Enclos("Prairie Nord", "Zone Nord", CODE, 6, 2005)

    def test_occuper_rend_indisponible(self):
        self.h.occuper()
        self.assertFalse(self.h.libre)

    def test_occuper_deja_reserve_leve_ValueError(self):
        self.h.occuper()
        with self.assertRaises(ValueError):
            self.h.occuper()

    def test_liberer_rend_disponible(self):
        self.h.occuper()
        self.h.liberer()
        self.assertTrue(self.h.libre)

    def test_liberer_deja_libre_leve_ValueError(self):
        with self.assertRaises(ValueError):
            self.h.liberer()


class TestEnclosFicheResume(unittest.TestCase):
    """Format exact de fiche_resume."""

    def test_fiche_resume_enclos(self):
        h = Enclos("Prairie Nord", "Zone Nord", CODE, 4, 2005)
        self.assertEqual(h.fiche_resume(), "4 animaux")


class TestEnclosDepuisCsv(unittest.TestCase):
    """Constructeur alternatif depuis_csv."""

    def test_depuis_csv_nominal(self):
        h = Enclos.depuis_csv(f"Prairie Nord;Zone Nord;{CODE};6;2005")
        self.assertIsInstance(h, Enclos)
        self.assertEqual(h.capacite_animaux, 6)
        self.assertEqual(h.annee_construction, 2005)

    def test_depuis_csv_mauvais_nombre_de_champs(self):
        with self.assertRaises(ValueError):
            Enclos.depuis_csv(f"Prairie;Zone Nord;{CODE};6")


class TestEnclosRepr(unittest.TestCase):
    """__str__ et __repr__ : présents et, pour repr, reconstructible."""

    def test_str_mentionne_etat(self):
        h = Enclos("Prairie Nord", "Zone Nord", CODE, 6, 2005)
        self.assertIn("libre", str(h))
        h.occuper()
        self.assertIn("occupé", str(h))

    def test_repr_reconstructible(self):
        h = Enclos("Prairie Nord", "Zone Nord", CODE, 6, 2005)
        reconstruit = eval(
            repr(h),
            {"Enclos": Enclos, "EnclosChauffe": EnclosChauffe,
             "BassinAquatique": BassinAquatique},
        )
        self.assertEqual(reconstruit, h)
        self.assertEqual(reconstruit.capacite_animaux, 6)


class TestEnclosIdentite(unittest.TestCase):
    """Égalité et hachage par code de réservation (entité)."""

    def test_egalite_par_code(self):
        h1 = Enclos("Prairie Nord", "Zone Nord", CODE, 6, 2005)
        h2 = Enclos("Autre Nom", "Zone Ouest", CODE, 2, 1990)
        self.assertEqual(h1, h2)

    def test_inegalite_codes_differents(self):
        h1 = Enclos("Prairie Nord", "Zone Nord", CODE, 6, 2005)
        h2 = Enclos("Prairie Nord", "Zone Nord", CODE2, 6, 2005)
        self.assertNotEqual(h1, h2)

    def test_hash_par_code(self):
        h1 = Enclos("Prairie Nord", "Zone Nord", CODE, 6, 2005)
        h2 = Enclos("Autre Nom", "Zone Ouest", CODE, 2, 1990)
        self.assertEqual(hash(h1), hash(h2))

    def test_eq_avec_autre_type_retourne_notimplemented(self):
        h = Enclos("Prairie Nord", "Zone Nord", CODE, 6, 2005)
        self.assertNotEqual(h, "une chaîne")


class TestEnclosChauffe(unittest.TestCase):
    """Sous-classe EnclosChauffe : enrichissement."""

    def test_construction_nominale(self):
        g = EnclosChauffe("Le Chenil", "Zone Sud", CODE2, 4, 1890, 3)
        self.assertEqual(g.nombre_abris, 3)
        self.assertEqual(g.capacite_animaux, 4)

    def test_est_un_enclos(self):
        g = EnclosChauffe("Le Chenil", "Zone Sud", CODE2, 4, 1890, 3)
        self.assertIsInstance(g, Enclos)

    def test_abris_non_int_leve_TypeError(self):
        with self.assertRaises(TypeError):
            EnclosChauffe("Le Chenil", "Zone Sud", CODE2, 4, 1890, 3.0)

    def test_abris_booleen_leve_TypeError(self):
        with self.assertRaises(TypeError):
            EnclosChauffe("Le Chenil", "Zone Sud", CODE2, 4, 1890, True)

    def test_abris_zero_leve_ValueError(self):
        with self.assertRaises(ValueError):
            EnclosChauffe("Le Chenil", "Zone Sud", CODE2, 4, 1890, 0)

    def test_validation_heritee_appliquee(self):
        with self.assertRaises(ValueError):
            EnclosChauffe("Le Chenil", "Zone Sud", CODE2, 51, 1890, 3)

    def test_fiche_resume_enrichit(self):
        g = EnclosChauffe("Le Chenil", "Zone Sud", CODE2, 4, 1890, 3)
        self.assertEqual(
            g.fiche_resume(), "4 animaux [enclos chauffé, 3 abris]")

    def test_repr_reconstructible(self):
        g = EnclosChauffe("Le Chenil", "Zone Sud", CODE2, 4, 1890, 3)
        reconstruit = eval(
            repr(g),
            {"Enclos": Enclos, "EnclosChauffe": EnclosChauffe,
             "BassinAquatique": BassinAquatique},
        )
        self.assertEqual(reconstruit, g)
        self.assertEqual(reconstruit.nombre_abris, 3)

    def test_depuis_csv_donne_un_gite(self):
        g = EnclosChauffe.depuis_csv(f"Le Chenil;Zone Sud;{CODE2};4;1890;3")
        self.assertIsInstance(g, EnclosChauffe)
        self.assertEqual(g.nombre_abris, 3)

    def test_str_renvoie_une_chaine_mentionnant_etat(self):
        g = EnclosChauffe("Le Chenil", "Zone Sud", CODE2, 4, 1890, 3)
        self.assertIsInstance(str(g), str)
        self.assertIn("libre", str(g))


class TestBassinAquatique(unittest.TestCase):
    """Sous-classe BassinAquatique : remplacement."""

    def test_construction_nominale(self):
        e = BassinAquatique("Grand Bassin", "Zone Est", CODE3, 4, 2015, 20.0)
        self.assertEqual(e.volume_m3, 20.0)

    def test_est_un_enclos(self):
        e = BassinAquatique("Grand Bassin", "Zone Est", CODE3, 4, 2015, 20.0)
        self.assertIsInstance(e, Enclos)

    def test_volume_acceptee_en_int(self):
        e = BassinAquatique("Grand Bassin", "Zone Est", CODE3, 4, 2015, 18)
        self.assertEqual(e.volume_m3, 18.0)
        self.assertIsInstance(e.volume_m3, float)

    def test_volume_non_nombre_leve_TypeError(self):
        with self.assertRaises(TypeError):
            BassinAquatique("Grand Bassin", "Zone Est", CODE3, 4, 2015, "20")

    def test_volume_booleen_leve_TypeError(self):
        with self.assertRaises(TypeError):
            BassinAquatique("Grand Bassin", "Zone Est", CODE3, 4, 2015, True)

    def test_volume_nulle_leve_ValueError(self):
        with self.assertRaises(ValueError):
            BassinAquatique("Grand Bassin", "Zone Est", CODE3, 4, 2015, 0)

    def test_validation_heritee_appliquee(self):
        with self.assertRaises(ValueError):
            BassinAquatique("Grand Bassin", "Zone Est", CODE3, 4, 1799, 20.0)

    def test_fiche_resume_remplace(self):
        e = BassinAquatique("Grand Bassin", "Zone Est", CODE3, 4, 2015, 20.0)
        self.assertEqual(e.fiche_resume(), "20.0 m³ de bassin")

    def test_fiche_resume_ne_mentionne_pas_animaux(self):
        e = BassinAquatique("Grand Bassin", "Zone Est", CODE3, 4, 2015, 20.0)
        self.assertNotIn("animaux", e.fiche_resume())

    def test_repr_reconstructible(self):
        e = BassinAquatique("Grand Bassin", "Zone Est", CODE3, 4, 2015, 20.0)
        reconstruit = eval(
            repr(e),
            {"Enclos": Enclos, "EnclosChauffe": EnclosChauffe,
             "BassinAquatique": BassinAquatique},
        )
        self.assertEqual(reconstruit, e)
        self.assertEqual(reconstruit.volume_m3, 20.0)

    def test_depuis_csv_donne_un_bassin(self):
        e = BassinAquatique.depuis_csv(
            f"Grand Bassin;Zone Est;{CODE3};4;2015;20.0")
        self.assertIsInstance(e, BassinAquatique)
        self.assertEqual(e.volume_m3, 20.0)

    def test_str_renvoie_une_chaine_mentionnant_etat(self):
        e = BassinAquatique("Grand Bassin", "Zone Est", CODE3, 4, 2015, 20.0)
        self.assertIsInstance(str(e), str)
        self.assertIn("libre", str(e))


if __name__ == "__main__":
    unittest.main()
