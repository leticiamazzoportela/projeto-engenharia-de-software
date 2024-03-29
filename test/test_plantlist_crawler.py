import unittest
import sys
import os

DIRNAME = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(DIRNAME, "../src"))
import plantlist_crawler as plantlist_crawler

test_caseImput = [
    {
        "nome": 'Dicliptera ciliaris Juss.'
    },
    {
        "nome": 'Hygrophila angusta'
    },
    {
        "nome": 'Echinodorus argentinensis Rataj.'
    },
    {
        "nome": 'Justia pectoralis Jacq.'
    }
]


test_caseOutput = [
    {
        'nome': 'Dicliptera ciliaris Juss.', 'status_plantlist': '', 'plantlist': None
    },
    {
        'nome': 'Hygrophila angusta', 'status_plantlist': 'Não resolvido', 'plantlist': 'Hygrophila angusta Huber'
    },
    {
        'nome': 'Echinodorus argentinensis Rataj.', 'status_plantlist': 'sinonimo', 'plantlist': 'Echinodorus grandiflorus (Cham. & Schltdl.) Micheli'
    },
    {
        'nome': 'Justia pectoralis Jacq.', 'status_plantlist': 'nao_encontrado', 'plantlist': ''
    }
]

class test_getNames(unittest.TestCase):
    def test(self):
        self.assertEqual(plantlist_crawler.getNames(test_caseImput), test_caseOutput)

if __name__ == '__main__':
    unittest.main()

    #print(test_caseImput[1])
