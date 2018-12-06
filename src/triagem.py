# encoding: utf-8

import json
import os
import io


countrys = ['argentina', 'bolívia', 'brasil','chile', 'colômbia', 'equador',  'guiana', 'paraguai', 'peru', 'suriname', 'uruguai', 'venezuela', 'bolivia', 'brazil', 'colombia', 'ecuador', 'paraguay', 'uruguay']

lat = [12.0, -59.0]
longt = [-26.0, -109.0]

def read_gbif(data):
    new_data = {}
    for plant in data:
        oc = []
        for ocurrence in data[plant]:
            if(ocurrence['country'].lower() in countrys):
                oc.append(ocurrence)
            elif(ocurrence['decimalLatitude'] != "" and ocurrence['decimalLongitude'] != ""):
                if((float(ocurrence['decimalLatitude'])<= lat[0] and float(ocurrence['decimalLatitude']) >= lat[1]) and (float(ocurrence['decimalLongitude']) <= longt[0] and float(ocurrence['decimalLongitude']) >= longt[1])):
                    oc.append(ocurrence)
            else:
                print('não esta na ame. do sul')
        new_data[plant] = oc
    return new_data
    

def read_spicieslink(data):
    new_data = {}
    for plant in data:
        oc = []
        for ocurrence in data[plant]:
            if(ocurrence['pais'].lower() in countrys):
                oc.append(ocurrence)
            elif(ocurrence['lat'] != "" and ocurrence['long'] != ""):
                if((float(ocurrence['lat'])<= lat[0] and float(ocurrence['lat']) >= lat[1]) and (float(ocurrence['long']) <= longt[0] and float(ocurrence['long']) >= longt[1])):
                    oc.append(ocurrence)
            else:
                print('não esta na ame. do sul')
        new_data[plant] = oc
    return new_data

# gbif_data = read_gbif()
# with open('./data/saida_gbif_validado.json', 'w') as data_file:
#     data = json.dump(gbif_data, data_file)

# specieslink_data = read_gbif()
# with open('./data/gbif_validade.json', 'w') as data_file:
#     data = json.dump(specieslink_data, data_file)