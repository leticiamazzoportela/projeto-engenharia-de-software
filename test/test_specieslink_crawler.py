import unittest
import sys
import os

DIRNAME = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(DIRNAME, "../src"))
import specieslink_crawler

test_caseImput = ["Coleataenia prionitis (Nees) Soreng"]
test_caseImput2 = ["Trichanthecium nervosum (Lam.) Zuloaga & Morrone"]

test_caseOutput = {
    'Coleataenia prionitis (Nees) Soreng': [
        {'filo': '', 'familia': 'Poaceae', 'ordem': 'Poales', 'genero': 'Coleataenia', 'especie': 'prionitis','classe': '', 
            'coletor': 'Leite, P.F.; Klein, R.M.', 'lat': '-23.366667', 'long': '-53.75', 'pais': 'Brasil', 'data': '19/01/1986'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'K.Kawakita; Ma.C.Souza; Vianna, L.F.; Rosa, G.S.', 'lat': '-22.683333', 'long': '-53.216667', 'pais': 'Brasil', 'data': '04/10/2008'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'Nélson Ivo Matzenbacher', 'lat': '-30.113899230957', 'long': '-51.3250007629395', 'pais': 'Brasil', 'data': ''}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'José Francisco Montenegro Valls', 'lat': '-29.7546997070312', 'long': '-57.0882987976074', 'pais': 'Brasil', 'data': '14/10/1971'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'Zanon, C.M.V.', 'lat': '-22.2952995300293', 'long': '-53.2710990905762', 'pais': 'Brasil', 'data': '18/11/2007'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'Ma.C.Souza', 'lat': '-22.4878005981445', 'long': '-53.3513984680176', 'pais': 'Brasil', 'data': '29/04/1994'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'K.Kawakita; J.M.Garcia; J.G.Servilheri; Rosa, G.S.; A.S.Silva', 'lat': '-22.908333', 'long': '-53.64', 'pais': 'Brasil', 'data': '23/11/2010'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'K.Kawakita; Rosa, G.S.; Ma.C.Souza; Rodrigues, S.; Almeida, C.G.', 'lat': '-22.4818992614746', 'long': '-54.3025016784668', 'pais': 'Brasil', 'data': '09/12/2009'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'Teresia Strehl', 'lat': '-29.9591999053955', 'long': '-51.7221984863281', 'pais': 'Brasil', 'data': '18/10/1982'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': 'Poales', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'Klein, R.M.; Pastore, U.', 'lat': '-29.1252994537354', 'long': '-56.5531005859375', 'pais': 'Brasil', 'data': '25/11/1980'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'Fontana, A.C.; e col.', 'lat': '-22.4818992614746', 'long': '-54.3025016784668', 'pais': 'Brasil', 'data': '12/12/2004'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'Ma.C.Souza', 'lat': '-22.4878005981445', 'long': '-53.3513984680176', 'pais': 'Brasil', 'data': '17/05/1992'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'K.Kawakita; J.M.Garcia; J.G.Servilheri; Rosa, G.S.; Silva, A.S.', 'lat': '-22.692611', 'long': '-53.232778', 'pais': 'Brasil', 'data': '25/11/2010'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'K.Kawakita; Garcia, J.M.; Harthman, V.C.; Santos, L.S.; Soares, A.', 'lat': '-22.859328', 'long': '-53.614122', 'pais': 'Brasil', 'data': '03/12/2008'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'H. Lorenzi', 'lat': '-30.5439', 'long': '-52.5219', 'pais': 'Brasil', 'data': '10/12/2005'}, 
        {'filo': 'Magnoliophyta', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'A.L.S. Fachardo', 'lat': '-22.918619', 'long': '-53.650894', 'pais': 'Brasil', 'data': '11/06/2015'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'K.Kawakita; Rosa, G.S.; Ma.C.Souza; Rodrigues, S.; Almeida, C.G.', 'lat': '-22.4818992614746', 'long': '-54.3025016784668', 'pais': 'Brasil', 'data': '10/12/2009'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'Ma.C.Souza', 'lat': '-22.2952995300293', 'long': '-53.2710990905762', 'pais': 'Brasil', 'data': '27/11/2009'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'Ma.C.Souza; Slusarski, S.R.; Asinelli, M.E.C.; Rodrigues, S.', 'lat': '-22.2952995300293', 'long': '-53.2710990905762', 'pais': 'Brasil', 'data': '07/12/2006'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Coleataenia', 'especie': 'prionitis', 'classe': '', 
            'coletor': 'Jan Christiaan Lindeman', 'lat': '-30.8131008148193', 'long': '-53.8950004577637', 'pais': 'Brasil', 'data': '17/10/1971'}
    ]
}

test_caseOutput2 = {
    'Trichanthecium nervosum (Lam.) Zuloaga & Morrone': [
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Otto Huber|Ghillean T. Prance|João Murça Pires|I. Cordeiro|José Guedes|C.D.A. da Mota|E.L.S. da Silva|J.A.C. da Silva', 'lat': '0.8166667', 'long': '-63.3333333', 'pais': 'Brazil', 'data': '07/1985'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Nelson A. Rosa|Nazaré do Carmo|Eliana Penha', 'lat': '', 'long': '', 'pais': 'Brazil', 'data': '18/09/1976'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'J.S. de la Cruz', 'lat': '', 'long': '', 'pais': 'Brazil', 'data': '11/07/1923'}, 
        {'filo': 'Angiosperma', 'familia': 'Poaceae', 'ordem': 'Poales', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Bigio, NC', 'lat': '-13.117778', 'long': '-61.213889', 'pais': 'Brasil', 'data': '20/04/2013'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Prance, GT; et al.', 'lat': '0.816667', 'long': '-63.333333', 'pais': 'Brasil', 'data': '12/07/1985'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'José Francisco Montenegro Valls', 'lat': '-0.4', 'long': '-51.03333', 'pais': 'Brasil', 'data': '05/05/1988'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': "W. Wayt Thomas|D. Bock|Sérgio C. de Sant'Ana", 'lat': '-15.0525', 'long': '-38.9986111', 'pais': 'Brazil', 'data': '21/03/2002'}, 
        {'filo': 'Monocotyledon', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Giacomin, LL; Almeida, TE; Lombardi, JA', 'lat': '-8.581528', 'long': '-61.407278', 'pais': 'Brasil', 'data': '29/07/2013'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Rocha, A.E.S.; Araújo, M.A.M.', 'lat': '4.43139', 'long': '-61.1464', 'pais': 'Brasil', 'data': '26/09/2013'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Richard Spruce', 'lat': '-2.44306', 'long': '-54.7083', 'pais': 'Brazil', 'data': ''}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Behar, L.', 'lat': '-20.6580009460449', 'long': '-40.5110015869141', 'pais': 'Brasil', 'data': '08/02/1985'}, 
        {'filo': 'Monocotyledon', 'familia': 'Poaceae', 'ordem': 'Poales', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Huber, O', 'lat': '0.816667', 'long': '-63.333333', 'pais': 'Brasil', 'data': '07/1985'}, 
        {'filo': 'Angiosperma', 'familia': 'Poaceae', 'ordem': 'Poales', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Bigio, NC', 'lat': '-13.117778', 'long': '-61.213889', 'pais': 'Brasil', 'data': '20/04/2013'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Benedito V. Rabelo|N. Solamon|R. Souza', 'lat': '2.2', 'long': '-50.9166667', 'pais': 'Brazil', 'data': '12/12/1984'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'D. Philcox|A. Fereira', 'lat': '-12.8166667', 'long': '-51.7666667', 'pais': 'Brazil', 'data': '19/01/1968'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Scott A. Mori|R.M. Cardoso', 'lat': '2.25', 'long': '-50.9166667', 'pais': 'Brazil', 'data': '12/12/1984'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Glocimar Pereira-Silva', 'lat': '-9.5972222', 'long': '-65.339166', 'pais': 'Brasil', 'data': '07/12/2012'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Paulo B. Cavalcante', 'lat': '2.3333333', 'long': '-55.75', 'pais': 'Brazil', 'data': '28/02/1970'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Renato Ferraz de Arruda Veiga', 'lat': '-2.33333', 'long': '-49.53333', 'pais': 'Brasil', 'data': '20/10/1987'}, 
        {'filo': 'Magnoliophyta', 'familia': 'Poaceae', 'ordem': 'Poales', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'R. Spruce', 'lat': '-2.449614', 'long': '-54.740486', 'pais': 'Brasil', 'data': ''}, 
        {'filo': 'Monocotyledon', 'familia': 'Poaceae', 'ordem': 'Poales', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Pereira-Silva, G da', 'lat': '-9.597222', 'long': '-65.339167', 'pais': 'Brasil', 'data': '07/12/2012'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Hubber, O; et al.', 'lat': '0.816667', 'long': '-63.333333', 'pais': 'Brasil', 'data': '07/1985'}, 
        {'filo': 'Angiospermae', 'familia': 'Poaceae', 'ordem': 'Poales', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': 'Lilianae', 
            'coletor': 'Ribeiro, A.', 'lat': '-7.50611019134521', 'long': '-63.0208015441895', 'pais': 'Brasil', 'data': ''}, 
        {'filo': 'Monocotyledon', 'familia': 'Poaceae', 'ordem': 'Poales', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Bridgewater, S', 'lat': '2.45', 'long': '-50.883333', 'pais': 'Brasil', 'data': '07/08/1993'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': "Thomas, WW; Bock, D; Sant'Ana, S", 'lat': '-15.053889', 'long': '-38.998611', 'pais': 'Brasil', 'data': '21/03/2002'}, 
        {'filo': '', 'familia': 'Panicoideae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'N.A.Rosa; N.Carmo; E.Penha', 'lat': '', 'long': '', 'pais': 'Brasil', 'data': '18/09/1976'}, 
        {'filo': 'Angiosperma', 'familia': 'Poaceae', 'ordem': 'Poales', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Pereira-Silva, G', 'lat': '-9.597222', 'long': '-65.339167', 'pais': 'Brasil', 'data': '07/12/2012'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '',
            'coletor': 'Talmon S. dos Santos|L.A. Mattos Silva|Edgar B. dos Santos', 'lat': '-13.4869', 'long': '-39.0439', 'pais': 'Brazil', 'data': '29/04/1980'}, 
        {'filo': '', 'familia': 'Poaceae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Ghillean T. Prance|I. Cordeiro|J.A.C. da Silva|C.D.A. da Mota|João Murça Pires|E.L.S. da Silva', 'lat': '0.8166667', 'long': '-63.3333333', 'pais': 'Brazil', 'data': '12/07/1985'}, 
        {'filo': 'Monocotyledon', 'familia': 'Poaceae', 'ordem': 'Poales', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': 'Costa, FM', 'lat': '-5.388553', 'long': '-61.009625', 'pais': 'Brasil', 'data': '28/11/2012'}, 
        {'filo': '', 'familia': 'Gramineae', 'ordem': '', 'genero': 'Trichanthecium', 'especie': 'nervosum', 'classe': '', 
            'coletor': "W. W. Thomas; D. Bock & S.C. Sant'Ana", 'lat': '-15.054167', 'long': '-38.9987', 'pais': 'Brasil', 'data': '21/03/2002'}
    ]
}


class test_getNames(unittest.TestCase):
    def test(self):
        self.assertEqual(specieslink_crawler.get_data(
            test_caseImput), test_caseOutput)

    def test2(self):
        self.assertEqual(specieslink_crawler.get_data(
            test_caseImput2), test_caseOutput2)


if __name__ == '__main__':
    unittest.main()
