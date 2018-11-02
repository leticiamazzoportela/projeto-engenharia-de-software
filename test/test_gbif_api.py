import unittest
import sys
import os

DIRNAME = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(DIRNAME, "../src"))
import gbif_api

test_caseImput = [
    "Zizaniopsis bonariensis (Balansa & Poitr.) Speg."
]

test_caseOutput = {
    "Zizaniopsis bonariensis (Balansa & Poitr.) Speg.": [
        {
            "decimalLatitude": -29.99,
            "decimalLongitude": -51.083333,
            "eventDate": "2006-02-14T00:00:00.000+0000",
            "country": "Brazil",
            "stateProvince": "Rs",
            "locality": "."
        },
        {
            "decimalLatitude": 0.0,
            "decimalLongitude": 0.0,
            "eventDate": "1996-11-30T00:00:00.000+0000",
            "country": "Brazil",
            "stateProvince": "Rs",
            "locality": "Fazenda S\u00e3o Maximiano"
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1992-12-11T00:00:00.000+0000",
            "country": "Argentina",
            "stateProvince": "Corrientes",
            "locality": "Reserva Nat. Prov. Ibera. Paso Picada. Costa W de la laguna Ibera"
        },
        {
            "decimalLatitude": 0.0,
            "decimalLongitude": 0.0,
            "eventDate": "1981-02-02T00:00:00.000+0000",
            "country": "Brazil",
            "stateProvince": "Rs",
            "locality": "Lagoa Figueira, sul de palmares"
        },
        {
            "decimalLatitude": 0.0,
            "decimalLongitude": 0.0,
            "eventDate": "1981-03-01T00:00:00.000+0000",
            "country": "Brazil",
            "stateProvince": "Rs",
            "locality": "Taim"
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1980-11-02T00:00:00.000+0000",
            "country": "Argentina",
            "stateProvince": "",
            "locality": "Pdo. Gral. Lavalle, Ecia. Las Violetas."
        },
        {
            "decimalLatitude": 0.0,
            "decimalLongitude": 0.0,
            "eventDate": "1980-11-02T00:00:00.000+0000",
            "country": "Argentina",
            "stateProvince": "",
            "locality": "[...] Las Violetas"
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1978-03-08T00:00:00.000+0000",
            "country": "Argentina",
            "stateProvince": "Corrientes",
            "locality": "Estancia lavalle."
        },
        {
            "decimalLatitude": 0.0,
            "decimalLongitude": 0.0,
            "eventDate": "1978-12-04T00:00:00.000+0000",
            "country": "Brazil",
            "stateProvince": "Rs",
            "locality": "Esta\u00e7\u00e3o Ecol\u00f3gica do Taim"
        },
        {
            "decimalLatitude": 0.0,
            "decimalLongitude": 0.0,
            "eventDate": "1974-12-06T00:00:00.000+0000",
            "country": "Argentina",
            "stateProvince": "Corrientes",
            "locality": "Santo Tom\u00e9 Galarza"
        },
        {
            "decimalLatitude": 0.0,
            "decimalLongitude": 0.0,
            "eventDate": "1973-12-03T00:00:00.000+0000",
            "country": "Brazil",
            "stateProvince": "Rs",
            "locality": "estrada S\u00e3o Pedro do Sul-Jaguari 38 Km ap\u00f3s S\u00e3o Pedro"
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1970-03-23T00:00:00.000+0000",
            "country": "Brazil",
            "stateProvince": "Minas Gerais",
            "locality": "River bank. Cut-over slope forest, ca. 15 km N. of S\u00e3o Jo\u00e3o da Chapada."
        },
        {
            "decimalLatitude": 0.0,
            "decimalLongitude": 0.0,
            "eventDate": "1962-12-09T00:00:00.000+0000",
            "country": "Argentina",
            "stateProvince": "Buenos Aires",
            "locality": ""
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1961-02-17T00:00:00.000+0000",
            "country": "Argentina",
            "stateProvince": "Corrientes",
            "locality": "\"Estancia, Santa Teresa\"."
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1957-12-02T00:00:00.000+0000",
            "country": "Brazil",
            "stateProvince": "Rio Grande do Sul",
            "locality": "I.A.S. - Pelotas.  Canal I.A.S. - S. Gon\u00e7alo, bra\u00e7o de liga\u00e7ao com o arroio Pe. Doutor"
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1951-02-17T00:00:00.000+0000",
            "country": "Argentina",
            "stateProvince": "",
            "locality": "Estancia Santa Teresa. Dep. Mburucuya. Prov. Corrientes."
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1946-11-26T00:00:00.000+0000",
            "country": "Argentina",
            "stateProvince": "Buenos Aires",
            "locality": "Las Palmas."
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1946-11-26T00:00:00.000+0000",
            "country": "Argentina",
            "stateProvince": "Buenos Aires",
            "locality": "Las Palmas Zral. Uribure."
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1945-10-31T00:00:00.000+0000",
            "country": "Brazil",
            "stateProvince": "Rio Grande do Sul",
            "locality": "Sao Goncaies, instituto Agronomico do Sul, Pelotas. Wet ground along canal to arroyo."
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1912-06-23T00:00:00.000+0000",
            "country": "Argentina",
            "stateProvince": "Buenos Aires",
            "locality": "Quilmes"
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1875-11-14T00:00:00.000+0000",
            "country": "Paraguay",
            "stateProvince": "",
            "locality": "PL. du Paraguay., Bu\u00e9nos - aires, dans les marais."
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1875-11-14T00:00:00.000+0000",
            "country": "Paraguay",
            "stateProvince": "",
            "locality": "PL. du Paraguay., Bu\u00e9nos - aires, dans les marais."
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "1875-11-07T00:00:00.000+0000",
            "country": "Paraguay",
            "stateProvince": "",
            "locality": "Paseo de Julio, \u00e0 Buenos - Aires. *."
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "",
            "country": "Argentina",
            "stateProvince": "Buenos Aires",
            "locality": "Avellaneda ?"
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "",
            "country": "Argentina",
            "stateProvince": "Entre R\u00edos",
            "locality": "Pranacito"
        },
        {
            "decimalLatitude": -37.615321,
            "decimalLongitude": -57.423687,
            "eventDate": "",
            "country": "Argentina",
            "stateProvince": "Buenos Aires",
            "locality": "Estancia \"Nahuel Ruca\", m\u00e1rgen de Laguna Nahuel Ruca"
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "",
            "country": "Argentina",
            "stateProvince": "Buenos Aires",
            "locality": "Conchitas"
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "",
            "country": "Argentina",
            "stateProvince": "Buenos Aires",
            "locality": ""
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "",
            "country": "Argentina",
            "stateProvince": "Buenos Aires",
            "locality": "Delta del Paran\u00e1, R\u00edo Capit\u00e1n y Paran\u00e1 de las Palmas"
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "",
            "country": "Uruguay",
            "stateProvince": "",
            "locality": ""
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "",
            "country": "Brazil",
            "stateProvince": "",
            "locality": "General Vargas, Estr. S. Pedro do Sul-Jaguari, 38 km apos S. Pedro-Varzea do rio Toropi, jun to a ponte de concreto de + 80 de extens\u00e3o."
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "",
            "country": "Argentina",
            "stateProvince": "Buenos Aires",
            "locality": "Quilmes"
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "",
            "country": "Argentina",
            "stateProvince": "Buenos Aires",
            "locality": "\"El Toro\", Rosas F.C.S."
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "",
            "country": "Argentina",
            "stateProvince": "Buenos Aires",
            "locality": "Laguna San Vicente"
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "",
            "country": "Argentina",
            "stateProvince": "Entre R\u00edos",
            "locality": "M\u00e9danos"
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "",
            "country": "Argentina",
            "stateProvince": "La Pampa",
            "locality": ""
        },
        {
            "decimalLatitude": "",
            "decimalLongitude": "",
            "eventDate": "",
            "country": "Paraguay",
            "stateProvince": "",
            "locality": "Monoique., Buenos-ayres, dans les marais."
        }
    ]
}

class test_getNames(unittest.TestCase):
    def test(self):
        self.assertEqual(gbif_api.getOccurrences(test_caseImput), test_caseOutput)

if __name__ == '__main__':
    unittest.main()