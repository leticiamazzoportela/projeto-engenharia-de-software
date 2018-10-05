import unittest
import sys
import os

DIRNAME = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(DIRNAME, "../src"))
import florabrasil_api

test_caseImput = [
    "Echinodorus bolivianus (Rusby) Hom-Niels",
    "Echinodorus cordifolius (L.) Griseb. ",
    "Echinodorus floribundus (Seub.) Seub.",
    "Echinodorus glandulosus Rataj",
    "Echinodorus grandiflorus (Cham. & Schltdl.) Micheli",
    "Echinodorus grisebachii Small",
    "Echinodorus lanceolatus Rataj",
]

test_caseOutput = [
    {
        "status_florabrasil": "sinonimo",
        "nome": "Echinodorus bolivianus (Rusby) Hom-Niels",
        "florabrasil": "Helanthium bolivianum (Rusby) Lehtonen & Myllys"
    },
    {
        "status_florabrasil": "nao_encontrado",
        "nome": "Echinodorus cordifolius (L.) Griseb. "
    },
    {
        "status_florabrasil": "",
        "nome": "Echinodorus floribundus (Seub.) Seub.",
        "florabrasil": "Echinodorus floribundus (Seub.) Seub."
    },
    {
        "status_florabrasil": "",
        "nome": "Echinodorus glandulosus Rataj",
        "florabrasil": "Echinodorus glandulosus Rataj"
    },
    {
        "status_florabrasil": "",
        "nome": "Echinodorus grandiflorus (Cham. & Schltdl.) Micheli",
        "florabrasil": "Echinodorus grandiflorus (Cham. & Schltr.) Micheli"
    },
    {
        "status_florabrasil": "",
        "nome": "Echinodorus grisebachii Small",
        "florabrasil": "Echinodorus grisebachii Small"
    },
    {
        "status_florabrasil": "",
        "nome": "Echinodorus lanceolatus Rataj",
        "florabrasil": "Echinodorus lanceolatus Rataj"
    }
]

class test_getNames(unittest.TestCase):
    def test(self):
        self.assertEqual(florabrasil_api.getNames(test_caseImput), test_caseOutput)

if __name__ == '__main__':
    unittest.main()