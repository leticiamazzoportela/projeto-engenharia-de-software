import csv_util
import florabrasil_api
import plantlist_crawler

print("\n\n----------------------------")
print("processando lista de entrada.....")
csv_data = csv_util.readInput()

try:
	print("Verificando nomes.....")
	print("\nanalisando flora do brasil....\n")
	florabrasil_data = florabrasil_api.getNames(csv_data)

	print("\nanalisando plantlist....\n")
	plantlist_data = plantlist_crawler.getNames(florabrasil_data)
except ConnectionError:
	print("Falha na rede...")
	exit(1)

print("Salvando CSV")
csv_util.saveSheet(plantlist_data)