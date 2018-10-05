import csv_util
import florabrasil_api
import plantlist_crawler

try:
	print("\n\n----------------------------")
	print("processando lista de entrada.....")
	csv_data = csv_util.readInput()
	print("Verificando nomes.....")
	print("\nanalisando flora do brasil....\n")
	florabrasil_data = florabrasil_api.getNames(csv_data)
except ConnectionError:
	print("Falha na rede...")
	exit(1)
print("\nanalisando plantlist....\n")
plantlist_data = plantlist_crawler.getNames(florabrasil_data)

print("Salvando CSV")
csv_util.saveCSV(plantlist_data)