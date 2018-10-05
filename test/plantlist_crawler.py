import unittest
import plantlist_crawler

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
        'nome': 'Dicliptera ciliaris Juss.', 'status_plantlist': '', 'plantlist': 'Dicliptera ciliaris Juss.'
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
