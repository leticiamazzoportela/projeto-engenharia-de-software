# encoding: utf-8

import requests
import json
import os
import io
import util

countrys = ['argentina', 'bolívia', 'brasil','chile', 'colômbia', 'equador',  'guiana', 'paraguai', 'peru', 'suriname', 'uruguai', 'venezuela', 'bolivia', 'brazil', 'colombia', 'ecuador', 'paraguay', 'uruguay']

lat = [12.0, -59.0]
longt = [-26.0, -109.0]

def read_gbif():

    with open('./data/saida_gbif.json') as json_gbif:
        plants = 0
        notf = 0
        data = json.load(json_gbif)
        for plant in data:
            for ocurrence in data[plant]:
                plants += 1
                if(ocurrence['country'].lower() in countrys):
                    pass
                elif(ocurrence['decimalLatitude'] != "" and ocurrence['decimalLongitude'] != ""):
                    if((float(ocurrence['decimalLatitude'])<= lat[0] and float(ocurrence['decimalLatitude']) >= lat[1]) and (float(ocurrence['decimalLongitude']) <= longt[0] and float(ocurrence['decimalLongitude']) >= longt[1])):
                        pass
                else:
                    # print('não esta na ame. do sul')
                    del ocurrence
    
    with open('./data/saida_gbif.json', 'w') as data_file:
    data = json.dump(data, data_file)

read_gbif()