
from funcoes import conecta_zabbix
from pprint import pprint
import csv
zapi = conecta_zabbix()

# gerar relatorio host da localidade de PGFN São Paulo

with open('exercicio2_relatorio_hosts.cvs', 'w', newline='', encoding='utf-8') as file:
    relatorio = csv.writer(file, delimiter = ';')
    cabecalho = ['Localidade','Host','Name','Status','Tipo','IP','Tipo']
    relatorio.writerow(cabecalho)

    #grupo de hosts
    options = {
        "output": ['name'],
        "search": {"name": "LAN/PGFN/SP/PGFN"},
        "sortfield": "name",
        "selectHosts": ['hostid']
    }
    grupos = zapi.hostgroup.get(options)

    for grupo in grupos:
        #pprint(grupo)
        localidade = grupo['name'].split('/')[3]
        #pprint(localidade)
        for host in grupo['hosts']:
            hostid = host['hostid']

            options = {
                "output":['host','name','status'],
                "hostid": hostid,
                "selectInterfaces": ['ip'],
                "selectInventory": ['type']
            }
            hosts = zapi.host.get(options)
            #pprint(hosts)
            for host in hosts:
                host_host = host['host']
                host_name = host['name']
                status = host['status']
                lista_status = ['Ativo','inativo']
                host_status = lista_status[int(status)]
                ip = host['interfaces'][0]['ip']
                #tipo = host['inventory']['type']
                tipo = ""
                if host['inventory']:
                    tipo = host['inventory']['type']

                print(localidade, host_host,host_name,host_status, ip,tipo)
                linha = [localidade, host_host, host_name, host_status, ip, tipo]
                relatorio.writerow(linha)
