# encoding: utf-8

import unittest
import sys
import os

DIRNAME = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(DIRNAME, "../src"))
from plantlist_other_infos import getNames
import util

test_caseImput = [
    {
        "status_florabrasil": "nao_encontrado",
        "nome": "Colocasia esculenta (L.) Schott.",
        "status_plantlist": "",
        "plantlist": "Colocasia esculenta (L.) Schott"
    }
]

test_caseOutput = [
    {
        'name': 'Colocasia esculenta (L.) Schott', 'family': 'Araceae', 'hierarchy': 'Angiosperms', 
            'synonyms': [
                'Alocasia dussii Dammer', 'Alocasia illustris W.Bull', 'Aron colocasium (L.) St.-Lag.', 'Arum chinense L.', 
                'Arum colocasia L.', 'Arum colocasioides Desf.', 'Arum esculentum L.', 'Arum lividum Salisb.', 
                'Arum nymphaeifolium (Vent.) Roxb.', 'Arum peltatum Lam.', 'Caladium acre R.Br.', 'Caladium colocasia (L.) W.Wight [Illegitimate]', 
                'Caladium colocasioides (Desf.) Brongn.', 'Caladium esculentum (L.) Vent.', 'Caladium glycyrrhizum Fraser', 'Caladium nymphaeifolium Vent.', 
                'Caladium violaceum Desf.', 'Caladium violaceum Engl.', 'Calla gaby Blanco', 'Calla virosa Roxb.', 'Colocasia acris (R.Br.) Schott', 
                'Colocasia aegyptiaca Samp.', 'Colocasia antiquorum var. acris (R.Br.) Schott', 'Colocasia antiquorum f. acuatica Makino', 
                'Colocasia antiquorum var. aquatilis (Hassk.) Engl. & K. Krause', 'Colocasia antiquorum f. eguimo Makino', 
                'Colocasia antiquorum var. esculenta (L.) Schott', 'Colocasia antiquorum var. euchlora (K.Koch & Linden) Schott', 
                'Colocasia antiquorum var. globulifera Engl. & K.Krause', 'Colocasia antiquorum var. illustris (W.Bull) Engl.', 
                'Colocasia antiquorum var. multifolia Makino', 'Colocasia antiquorum var. nymphaeifolia (Vent.) Engl.', 'Colocasia antiquorum f. oyasetage Makino', 
                'Colocasia antiquorum var. patens Makino', 'Colocasia antiquorum f. purpurea Makino', 'Colocasia antiquorum var. rosea Makino', 
                'Colocasia antiquorum var. rupicola Haines', 'Colocasia antiquorum var. stolonifera Haines', 'Colocasia antiquorum f. yamamotoi Makino', 
                'Colocasia colocasia (L.) Huth [Invalid]', 'Colocasia esculenta var. acris (R.Br.) A.F.Hill', 'Colocasia esculenta var. aquatilis Hassk.', 
                'Colocasia esculenta f. ebiimo Makino', 'Colocasia esculenta var. euchlora (K.Koch & Linden) A.F.Hill', 
                'Colocasia esculenta var. globulifera (Engl. & K.Krause) R.A.Young', 'Colocasia esculenta var. illustris (W.Bull) A.F.Hill', 
                'Colocasia esculenta var. nymphaeifolia (Kunth) A.F.Hill', 'Colocasia esculenta f. rotundifolia Makino', 
                'Colocasia esculenta var. rupicola (Haines) H.B.Naithani', 'Colocasia esculenta var. stolonifera (Haines) H.B.Naithani', 
                'Colocasia euchlora K.Koch & Linden', 'Colocasia formosana Hayata', 'Colocasia gracilis Engl.', 'Colocasia himalensis Royle', 
                'Colocasia konishii Hayata', 'Colocasia neocaledonica Van Houtte', 'Colocasia nymphaeifolia (Vent.) Kunth', 'Colocasia peltata (Lam.) Samp.', 
                'Colocasia vera Hassk.', 'Colocasia violacea (Desf.) auct.', 'Colocasia virosa (Roxb.) Kunth', 'Colocasia vulgaris Raf.', 'Leucocasia esculenta (L.) Nakai', 
                'Steudnera virosa (Roxb.) Prain', 'Zantedeschia virosa (Roxb.) K.Koch'
            ]
    }
]

class test_getNames(unittest.TestCase):
    def test(self):
        self.assertEqual(getNames(util.get_list_plantlist_name(test_caseImput)), test_caseOutput)

if __name__ == '__main__':
    unittest.main()