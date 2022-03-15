import sys
import requests
import os


os.system('clear')

print('Bem vindo ao verificador de sites 1.0!')
print("")
print("Esta ferramenta possibilita a consulta de um ou mais domínios com apenas uma linha de comando, siga as instruções abaixo:")
print("")
print("Instruções:")
print('1. Digite a url que deseja verificar (ex: https://google.com)')
print('2. Separe múltiplos domínios por vírgula (ex: https://google.com, https://meu-site.com, https:outro.com)')
print('')
print('')
print('')



url_digitada = input('url: ')
#filtrar espaços e letras maíúsculas
lista_url = url_digitada.split(',')

lista_filtrada = [i.strip() for i in [i.lower() for i in lista_url]]

lista_url_apropriada = []






#adicionar "https://" caso não tenha
for url in lista_filtrada:

    if not '://' in url:
        if '.' in url:
            lista_url_apropriada.append('https://' + url)
        else:
            print("")
            print("")
            print("################################")
            print("")
            print("URL inválida: " + url)
        
    else:
        lista_url_apropriada.append(url)




#Fazer a requisição na web pra cada item na lista
def is_online():
    print(" ")
    print("################################")
    print(" ")
    print("Verificando...")
    print(" ")

    try:
        for url in lista_url_apropriada: 

            req = requests.get(url) #faz a requisição na url
            status = req.status_code #pega o código (ex:200)

            if status == 200:
                print("Online " + "[Código: " + str(status) + "] - " + str(url))

            else:
                print("Offline " + "[Código: " + str(status) + "] - " + str(url))
        return("Concluído")

    except:
        print("Falha " + "[sem resposta] - " + str(url))
        return("Concluído.")
 
print(is_online())