import requests,json

nomes = {}
lista_nomes = []
nao_encontrados = []

with open('macrofitas.json') as f:
    data = json.load(f)


for i in range(0, len(data)):
    r = requests.get('http://servicos.jbrj.gov.br/flora/taxon/'+data[i])
    dado = json.loads(r.content)
    if(r.status_code == 200):
        if(dado.get('result') == None):
            nao_encontrados.append(data[i])
        else:
            nomes['nome_passado'] = data[i]
            if(dado.get('result')[0]['taxonomicstatus'] == 'NOME_ACEITO'):
                nomes['nome_correto'] = data[i]
            else:
                nomes['nome_correto'] = dado.get('result')[0]['acceptednameusage']
        lista_nomes.append(nomes.copy())
        print("list \n",lista_nomes)
    else:
        print(r.status_code)


macrofitas = 'nome_validado.json'

with open(macrofitas, 'w') as arq:
    json.dump(lista_nomes, arq, indent=2)


nao_encontrato = 'nao_encontrado_floraBrasil.json'

with open(nao_encontrato, 'w') as arq:
    json.dump(nao_encontrados, arq, indent=2)

