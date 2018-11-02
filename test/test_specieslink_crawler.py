import unittest
import sys
import os

DIRNAME = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(DIRNAME, "../src"))
import specieslink_crawler

test_caseImput = ["Coleataenia prionitis (Nees) Soreng", "Trichanthecium nervosum (Lam.) Zuloaga & Morrone"]

test_caseOutput = {'Coleataenia prionitis (Nees) Soreng': 
[{'lat': '-23.366667', 'long': '-53.75', 'collector': 'Leite, P.F.; Klein, R.M.', 'country': 'Brasil', 'state': 'Paraná', 'local': 'Perto do ribeirão Veado, Porto Camargo.', 'date': '19/01/1986'},
{'lat': '-22.683333', 'long': '-53.216667', 'collector': 'K.Kawakita; Ma.C.Souza; Vianna, L.F.; Rosa, G.S.', 'country': 'Brasil', 'state': 'Mato Grosso do Sul', 'local': 'rio Baía, várzea da margem esquerda', 'date': '04/10/2008'},
{'lat': '-30.113899230957', 'long': '-51.3250007629395', 'collector': 'Nélson Ivo Matzenbacher', 'country': 'Brasil', 'state': 'RS', 'local': None, 'date': None},
{'lat': '-22.4878005981445', 'long': '-53.3513984680176', 'collector': 'Ma.C.Souza', 'country': 'Brasil', 'state': 'Mato Grosso do Sul', 'local': 'rio Baía', 'date': '29/04/1994'},
{'lat': '-22.4818992614746', 'long': '-54.3025016784668', 'collector': 'K.Kawakita; Rosa, G.S.; Ma.C.Souza; Rodrigues, S.; Almeida, C.G.', 'country': 'Brasil', 'state': 'Mato Grosso do Sul', 'local': 'Rio Curupaí, Parque Estadual do Rio Ivinhema.', 'date': '10/12/2009'},
{'lat': '-29.7546997070312', 'long': '-57.0882987976074', 'collector': 'José Francisco Montenegro Valls', 'country': 'Brasil', 'state': 'RS', 'local': 'Uruguaiana - Barra do Quaraí.', 'date': '14/10/1971'},
{'lat': '-22.2952995300293', 'long': '-53.2710990905762', 'collector': 'Zanon, C.M.V.', 'country': 'Brasil', 'state': 'Mato Grosso do Sul', 'local': 'rio Baía, ilha do Aurélio', 'date': '18/11/2007'},
{'lat': '-22.859328', 'long': '-53.614122', 'collector': 'K.Kawakita; Garcia, J.M.; Harthman, V.C.; Santos, L.S.; Soares, A.', 'country': 'Brasil', 'state': 'Mato Grosso do Sul', 'local': 'rio Ivinhema, margem direita (campinho), Parque Estadual do Rio Ivinhema', 'date': '03/12/2008'},
{'lat': '-29.1252994537354', 'long': '-56.5531005859375', 'collector': 'Klein, R.M.; Pastore, U.', 'country': 'Brasil', 'state': 'Rio Grande do Sul', 'local': 'Margens do Rio Ibiquí.', 'date': '25/11/1980'},
{'lat': '-29.9591999053955', 'long': '-51.7221984863281', 'collector': 'Teresia Strehl', 'country': 'Brasil', 'state': 'RS', 'local': 'Pólo Carboquímico, mata do Rio Jacuí.', 'date': '18/10/1982'},
{'lat': '-22.2952995300293', 'long': '-53.2710990905762', 'collector': 'Ma.C.Souza; Slusarski, S.R.; Asinelli, M.E.C.; Rodrigues, S.', 'country': 'Brasil', 'state': 'Mato Grosso do Sul', 'local': 'rio Baía, ilha do Aurélio', 'date': '07/12/2006'},
{'lat': '-22.908333', 'long': '-53.64', 'collector': 'K.Kawakita; J.M.Garcia; J.G.Servilheri; Rosa, G.S.; A.S.Silva', 'country': 'Brasil', 'state': 'Mato Grosso do Sul', 'local': 'rio Ivinhema, lagoa Peroba, 10m da margem direita', 'date': '23/11/2010'},
{'lat': '-30.5439', 'long': '-52.5219', 'collector': 'H. Lorenzi', 'country': 'Brasil', 'state': 'RS', 'local': 'Coletado na fazenda Xafri (Frida), Serra das Encantadas. Material anterior e erroneamente tombado como HPL-6622.', 'date': '10/12/2005'},
{'lat': '-22.692611', 'long': '-53.232778', 'collector': 'K.Kawakita; J.M.Garcia; J.G.Servilheri; Rosa, G.S.; Silva, A.S.', 'country': 'Brasil', 'state': 'Mato Grosso do Sul', 'local': 'Rio Baía, margem esquerda', 'date': '25/11/2010'},
{'lat': '-22.918619', 'long': '-53.650894', 'collector': 'A.L.S. Fachardo', 'country': 'Brasil', 'state': 'Mato Grosso do Sul', 'local': 'Parque Estadual das Varzéas do Rio Ivinhema. Rio Ivinhema.', 'date': '11/06/2015'},
{'lat': '-22.4818992614746', 'long': '-54.3025016784668', 'collector': 'Fontana, A.C.; e col.', 'country': 'Brasil', 'state': 'Mato Grosso do Sul', 'local': 'rio Ivinhema, mata da lagoa Finado Raimundo', 'date': '12/12/2004'},
{'lat': '-22.4878005981445', 'long': '-53.3513984680176', 'collector': 'Ma.C.Souza', 'country': 'Brasil', 'state': 'Mato Grosso do Sul', 'local': 'rio Ivinhema, além da lagoa do Ventura', 'date': '17/05/1992'},
{'lat': '-22.2952995300293', 'long': '-53.2710990905762', 'collector': 'Ma.C.Souza', 'country': 'Brasil', 'state': 'Mato Grosso do Sul', 'local': 'rio Baía, Planície de inundação do rio Paraná',
'date': '27/11/2009'}, {'lat': '-22.4818992614746', 'long': '-54.3025016784668', 'collector': 'K.Kawakita; Rosa, G.S.; Ma.C.Souza; Rodrigues, S.; Almeida, C.G.', 'country': 'Brasil', 'state': 'Mato Grosso do Sul', 'local': 'rio Ivinhema, Parque Estadual do Rio Ivinhema; Campinho.', 'date': '09/12/2009'},
{'lat': '-30.8131008148193', 'long': '-53.8950004577637', 'collector': 'Jan Christiaan Lindeman', 'country': 'Brasil', 'state': 'RS', 'local': 'Baixada com capim alto recentemente secado, no campo 19 km NE de Lavras do Sul em touças grandes ate 2 m altas', 'date': '17/10/1971'}],
'Trichanthecium nervosum (Lam.) Zuloaga & Morrone':
[{'lat': '-9.597222', 'long': '-65.339167', 'collector': 'Pereira-Silva, G', 'country': 'Brasil', 'state': 'Rondônia', 'local': 'Módulo Abunâ, transecto 10, parcela 4, margem dire, Campinarana arbórea aberta. Relevo Plano. Solo Latossolo amarelo pouco estruturado.', 'date': '07/12/2012'},
{'lat': '0.816667', 'long': '-63.333333', 'collector': 'Hubber, O; et al.', 'country': 'Brasil', 'state': 'Amazonas', 'local': 'Campina en la región alta del Río Jauará (afluente del Río Aracá, llamado Río Cuieiras en los mapas RADAM), aprox. 15 km al NW de la punta SW de la Serra Aracá.', 'date': '07/1985'},
{'lat': '-13.117778', 'long': '-61.213889', 'collector': 'Bigio, NC', 'country': 'Brasil', 'state': 'Rondônia', 'local': 'Ramal de acesso ao Parque Estadual de Corumbiara, Beira da estrada antropizada.', 'date': '20/04/2013'},
{'lat': '0.8166667', 'long': '-63.3333333', 'collector': 'Otto Huber|Ghillean T. Prance|João Murça Pires|I. Cordeiro|José Guedes|C.D.A. da Mota|E.L.S. da Silva|J.A.C. da Silva', 'country': 'Brazil', 'state': 'Amazonas', 'local': 'Campina en la región alta del Río Jauarí (afluente del Río Aracá, llamado Rio Cuieriras en los mapas RADAM), aprox. 15 km al NW de la punta SW de la Serra Aracá.', 'date': '07/1985'},
{'lat': None, 'long': None, 'collector': 'Nelson A. Rosa|Nazaré do Carmo|Eliana Penha', 'country': 'Brazil', 'state': 'Pará', 'local': 'Marajó, Joanes, campo próximo ao igapó.', 'date': '18/09/1976'},
{'lat': None, 'long': None, 'collector': 'J.S. de la Cruz', 'country': 'Brazil', 'state': None, 'local': "Kamakusa, upper Mazaruni River. Longitude about 59°50' W.", 'date': '11/07/1923'},
{'lat': '-0.4', 'long': '-51.03333', 'collector': 'José Francisco Montenegro Valls', 'country': 'Brasil', 'state': 'AP', 'local': 'Campo Experimental do Cerrado, km 45 da rodovia BR - 156 (trecho Macapá - Ferreira Gomes).', 'date': '05/05/1988'},
{'lat': '-13.117778', 'long': '-61.213889', 'collector': 'Bigio, NC', 'country': 'Brasil', 'state': 'Rondônia', 'local': 'Ramal de acesso ao Parque Estadual de Corumbiara, Beira da estrada antropizada.', 'date': '20/04/2013'},
{'lat': '-15.0525', 'long': '-38.9986111', 'collector': "W. Wayt Thomas|D. Bock|Sérgio C. de Sant'Ana", 'country': 'Brazil', 'state': 'Bahia', 'local': 'Ca. 10 km S of Olivença along BA 001.', 'date': '21/03/2002'},
{'lat': '-20.6580009460449', 'long': '-40.5110015869141', 'collector': 'Behar, L.', 'country': 'Brasil', 'state': 'Espírito Santo', 'local': None, 'date': '08/02/1985'},
{'lat': '4.43139', 'long': '-61.1464', 'collector': 'Rocha, A.E.S.; Araújo, M.A.M.', 'country': 'Brasil', 'state': 'Roraima', 'local': 'Quartel do Exército de fronteira', 'date': '26/09/2013'},
{'lat': '-2.44306', 'long': '-54.7083', 'collector': 'Richard Spruce', 'country': 'Brazil', 'state': 'Pará', 'local': 'Santarem.',
'date': None}, {'lat': '-7.50611019134521', 'long': '-63.0208015441895', 'collector': 'Ribeiro, A.', 'country': 'Brasil', 'state': 'Amazonas', 'local': None, 'date': None},
{'lat': '0.816667', 'long': '-63.333333', 'collector': 'Huber, O', 'country': 'Brasil', 'state': 'Amazonas', 'local': 'Serra do Aracá, Campina en la región alta del río Jauarí (afluente del río Aracé, llamado río Cuieiras en los mapas RADAM), aprox. 15 km al NW de la punta SW de la Serra Aracá.', 'date': '07/1985'},
{'lat': '2.2', 'long': '-50.9166667', 'collector': 'Benedito V. Rabelo|N. Solamon|R. Souza', 'country': 'Brazil', 'state': 'Amapá', 'local': 'BR156, between Calçoene and Rio Amapá Grande, ca. 35 km S of Calçoene.', 'date': '12/12/1984'},
{'lat': None, 'long': None, 'collector': 'N.A.Rosa; N.Carmo; E.Penha', 'country': 'Brasil', 'state': 'Pará', 'local': 'Joanes, campo próximo ao igapó.', 'date': '18/09/1976'},
{'lat': '-12.8166667', 'long': '-51.7666667', 'collector': 'D. Philcox|A. Fereira', 'country': 'Brazil', 'state': 'Mato Grosso', 'local': 'Ca. 1-3 km W of km 261 Xavantina-Cachimbo road.', 'date': '19/01/1968'},
{'lat': '2.25', 'long': '-50.9166667', 'collector': 'Scott A. Mori|R.M. Cardoso', 'country': 'Brazil', 'state': 'Amapá', 'local': 'BR156, between Calçoene and Rio Amapá Grande, 30 km S of Calçoene.', 'date': '12/12/1984'},
{'lat': '-9.5972222', 'long': '-65.339166', 'collector': 'Glocimar Pereira-Silva', 'country': 'Brasil', 'state': 'RO', 'local': 'Modulo Abunã, Transecto 10, parcela 4, margem direita do rio Madeira.', 'date': '07/12/2012'},
{'lat': '2.3333333', 'long': '-55.75', 'collector': 'Paulo B. Cavalcante', 'country': 'Brazil', 'state': 'Pará', 'local': 'Parque Indigena do Tumucumaque, Rio Parú de Oeste, Missão Tiriyo.', 'date': '28/02/1970'},
{'lat': '0.816667', 'long': '-63.333333', 'collector': 'Prance, GT; et al.', 'country': 'Brasil', 'state': 'Amazonas', 'local': 'Serra do Aracá, Foothills of central massif of Serra do Acará.', 'date': '12/07/1985'},
{'lat': '-2.33333', 'long': '-49.53333', 'collector': 'Renato Ferraz de Arruda Veiga', 'country': 'Brasil', 'state': 'AM', 'local': 'Rodovia Transcameta, km 196,4.', 'date': '20/10/1987'},
{'lat': '-2.449614', 'long': '-54.740486', 'collector': 'R. Spruce', 'country': 'Brasil', 'state': 'ParÃ¡', 'local': 'In vicinibus Santarem', 'date': None},
{'lat': '-15.053889', 'long': '-38.998611', 'collector': "Thomas, WW; Bock, D; Sant'Ana, S", 'country': 'Brasil', 'state': 'Bahia', 'local': 'Ca. 10 km S of Olivença along BA-001.', 'date': '21/03/2002'},
{'lat': '-9.597222', 'long': '-65.339167', 'collector': 'Pereira-Silva, G da', 'country': 'Brasil', 'state': 'Rondônia', 'local': 'UHE Jirau, Modulo Abunã, Transecto 10, parcela 4, margem direita do rio Madeira.', 'date': '07/12/2012'},
{'lat': '-15.054167', 'long': '-38.9987', 'collector': "W. W. Thomas; D. Bock & S.C. Sant'Ana", 'country': 'Brasil', 'state': 'Bahia', 'local': 'Ca 10km S of Olivença along BA 001. 5m. Restinga', 'date': '21/03/2002'},
{'lat': '2.45', 'long': '-50.883333', 'collector': 'Bridgewater, S', 'country': 'Brasil', 'state': 'Amapá', 'local': 'White sand campo sujo, 5 Km south of Calçoene.', 'date': '07/08/1993'},
{'lat': '-13.4869', 'long': '-39.0439', 'collector': 'Talmon S. dos Santos|L.A. Mattos Silva|Edgar B. dos Santos', 'country': 'Brazil', 'state': 'Bahia', 'local': 'Rod. Nilo Pecanha-Cairú, km 14-18. Região da Mata Higrófila.', 'date': '29/04/1980'},
{'lat': '0.8166667', 'long': '-63.3333333', 'collector': 'Ghillean T. Prance|I. Cordeiro|J.A.C. da Silva|C.D.A. da Mota|João Murça Pires|E.L.S. da Silva', 'country': 'Brazil', 'state': 'Amazonas', 'local': 'Foothills of central massif of Serra Aracá.', 'date': '12/07/1985'},
{'lat': '-5.388553', 'long': '-61.009625', 'collector': 'Costa, FM', 'country': 'Brasil', 'state': 'Amazonas', 'local': 'Parque Estadual do Matupiri', 'date': '28/11/2012'},
{'lat': '-8.581528', 'long': '-61.407278', 'collector': 'Giacomin, LL; Almeida, TE; Lombardi, JA', 'country': 'Brasil', 'state': 'Amazonas', 'local': 'Parque Nacional dos Campos Amazônicos, Campo sujo às margens da estrada, ca. de 0,6 km saindo da estrada do Estanho a direita no trevo do Bodocó.', 'date': '29/07/2013'}]}

class test_getNames(unittest.TestCase):
    def test(self):
        self.assertEqual(specieslink_crawler.get_data(test_caseImput), test_caseOutput)

if __name__ == '__main__':
    unittest.main()