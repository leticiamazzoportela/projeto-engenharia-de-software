import csv_util
import florabrasil_api
import plantlist_crawler
import specieslink_crawler
import util
import json

print("\n\n----------------------------")
print("processando lista de entrada.....")
csv_data = csv_util.readInput()

# try:
# 	print("Verificando nomes.....")
# 	print("\nanalisando flora do brasil....\n")
# 	florabrasil_data = florabrasil_api.getNames(csv_data)

# 	print("\nanalisando plantlist....\n")
# 	plantlist_data = plantlist_crawler.getNames(florabrasil_data)
# except ConnectionError:
# 	print("Falha na rede...")
# 	exit(1)

# with open('plant_flora.json', 'w') as outfile:
#     json.dump(plantlist_data, outfile)

plantlist_data = json.loads(open("data/plant_flora.json").read())

# print("Salvando CSV")
# csv_util.saveSheet(plantlist_data)

valid_names = util.get_list_of_valid_names(plantlist_data)

with open('data/validname.json', 'w') as outfile:
    json.dump(valid_names, outfile)


specieslink =specieslink_crawler.get_data(valid_names)

with open('data/specieslink.json', 'w') as outfile:
    json.dump(specieslink, outfile)