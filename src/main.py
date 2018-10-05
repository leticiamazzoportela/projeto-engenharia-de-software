import csv_util
import florabrasil_api
import plantlist_crawler

print("\n\n----------------------------")
print("processando lista de entrada.....")
csv_util.readInput()
print("Verificando nomes.....")
print("\nanalisando flora do brasil....\n")
florabrasil_api.getNames()
print("\nanalisando plantlist....\n")
plantlist_crawler.getNames()

print("Salvando CSV")
csv_util.saveCSV()