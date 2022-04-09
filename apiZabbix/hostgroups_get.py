
from funcoes import conecta_zabbix
from pprint import pprint
import csv
zapi = conecta_zabbix()

options = {
    "output": ["name"],
    "search": {"name": "LAN/DNIT"},
    #"filter": {"name": "LAN/ME"}, # o filtro mosta especificamente e não suas derivações
    #"sortfield": "name", # mostra em todos os nomes
    #"sortorder": "DESC", #mostra em ordem decrescente
    #"searchWildcardsEnabled": True, #habilita o uso * para inserir todos encontrados
    #"monitored_hosts": True, # mostra somente os hosts monitored
    #"real_hosts": True, # mostra a localidade final do host
    #"countOutput": True, # mostra a contagem de host porém terá que realizar o print(hostgroups)
    #"hostids": ["28938","20994"]
    #"groupids": ["1326"],
    "selectHosts": ['host','status']
}
hostgroups = zapi.hostgroup.get(options)

#pprint(hostgroups)

'''
for grupo in hostgroups:
    print(grupo["name"])
    for host in grupo['hosts']:
        hostname = host['host']
        status = host['status']
        print(f'{hostname} : {status}')
'''

# Gerando lista:

with open('relatorio_dnit.csv', 'w', newline = '', encoding='UTF-8') as file:
    relatorio = csv.writer(file, delimiter=';')
    cabecalho = ['Grupo','Hosts']
    relatorio.writerow(cabecalho)

    for hostgroup in hostgroups:
        nome_grupo = hostgroup['name']
        #pprint(nome_grupo)
        hosts=[]
        for host in hostgroup['hosts']:
            hosts.append(host['host'])
            #pprint(hosts)
        lista_host= ','.join(hosts)
        linha = [nome_grupo, lista_host]
        relatorio.writerow(linha)




