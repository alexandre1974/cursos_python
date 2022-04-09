from funcoes import *
from pprint import pprint
import csv

#grupo de hosts
zapi = conecta_zabbix()

lista_grupos = ['TESTE_CURSO','CURSO_API/ALUNOS/GASPAR/SERVIDORES']
groups = []

for grupo in lista_grupos:
    groups.append(get_hostgroups(zapi, grupo))
#pprint(groups)
#interface
interface = {
    "dns": "",
    "ip": "192.168.11.1",
    "main": 1,
    "port": "10050",
    "type": 1,
    "useip": 1
}
# inserir tag

tags = [
    {
        "tag": "servico",
        "value": "LDAP"
     },
]

# macros
macro = [
            {
                "macro": "{$THRESHOLD_DISCO}",
                "value": "90"
            },
    ]

inventory = {
            "type": "servidor",
            "os": "linux",
            "type_full": "DC"
        }

lista_templates = ['101 - Linux Complementar','411 - LDAP']
templates = []

for template in lista_templates:
    templates.append(get_hosttemplates(zapi, template))
#pprint(templates)


#criação de host
options = {
    "host": "host_gaspar",
    "description": "Host criado para realizar o curso API",
    "name": "HOST DO GASPAR",
    "inventory_mode": 0,
    "groups": groups,
    "interfaces": interface,
    "tags": tags,
    "templates": templates,
    "macros": macro,
    "inventory": inventory

}

try:
    zapi.host.create(options)
    print("Host criado com sucesso!")
except Exception as erro:
    print(f"Erro ao criar o host. Error : {erro}")

