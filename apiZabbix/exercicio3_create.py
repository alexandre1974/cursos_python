from funcoes import *
import csv
from pprint import pprint

zapi = conecta_zabbix()

#criando host API a apartir do csv

with open("exercicio3.cvs", encoding='UTF-8') as file:
    linhas = csv.reader(file, delimiter=';')
    for [host, ip, proxy, grupos, templates, inventario, tags] in linhas:

        options = {
            "output": ['´proxyid'],
            "filter": {
                "host": proxy
            }
        }
        proxyid = zapi.proxy.get(options)[0]['proxyid']
        #pprint(proxyid)

        #exit()

        #inventario
        campo_inventario = inventario.split(',')
        #print(campo_inventario[0])
        inventario_tipo = campo_inventario[0]
        inventario_info = campo_inventario[1]

        inventory = {
            "type": inventario_tipo,
        }

        if inventario_tipo == "Servidor":
            inventory['os'] = inventario_info
            inventory['type_full'] = "DC"
            # inventory = {
            #     "type": inventario_tipo,
            #     "os": inventario_info
            # }
        else:
            inventory["hardware"] = inventario_tipo
            inventory['type_full'] = "REDE"
            # inventory = {
            #     "type": inventario_tipo,
            #     "hardware": inventario_info
            # }
        #pprint(inventory)

        #interface
        if inventario_tipo == 'Servidor':
            tipo_int = 1
            port = "10050"
        else:
            tipo_int = 2
            port = "161"

        interfaces = {
            "dns": "",
            "ip": ip,
            "main": 1,
            "port": port,
            "type": tipo_int,
            "useip": 1 # para habilitar a conexão por ip (vide manual)
        }
        #pprint(interface)

        #grupos
        #pprint(grupos)
        lista_grupos = grupos.split(',')
        groups = []
        for grupo in lista_grupos:
            groups.append(get_hostgroups(zapi, grupo))
        #print(groups)
        #exit()
        #Template
        lista_templates = templates.split(',')
        templates = []
        for template in lista_templates:
            templates.append(get_hosttemplates(zapi, template))
        # pprint(templates)
        # exit()
        #tags

        tag = tags.split(':')
        tags = [{
            "tag": tag[0],
            "value": tag[1]
        }]


        #criar host
        options = {
            "host": host,
            "name": f'HOST_DO_GASPAR - {host}',
            "descriptions": "Host criado via API - Exercicio 3 - Arquivo CSV",
            "inventory_mode": 0,# para ativar o inventario do host tem que inserir o zero
            "proxy_hostid": proxyid,
            "inventory": inventory,
            "interfaces": interfaces,
            "groups": groups,
            "templates": templates,
            "tags": tags
        }
        #print (options)
        criar_host(zapi, options)

zapi.logout()