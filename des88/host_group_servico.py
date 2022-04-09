from apizabbix import *
from pprint import pprint

zapi= conecta_zabbix(site("88"))

grupo_name = "WAN/"
options1 = {
    "output": ["name"],
    "search": {"name": grupo_name},
    #"monitored_hosts": 4
    }
# hostgroups1 = zapi.hostgroup.get(options1)[0]['name']
# print(hostgroups1)
# cliente = hostgroups1.split('/')[1]
# print(cliente)

# options = {
#         "name": cliente,
#         "algorithm": 0,
#         "parentid": "24113",
#         "showsla": 0,
#         "sortorder": 1
#     }
#
# service = zapi.service.create(options)
# serviceid = (service['serviceids'][0])
# pprint(serviceid)

hostgroups = zapi.hostgroup.get(options1)
lista_felipe = []
lista_uf = ['AC', 'AL', 'AM', 'AP', 'PB', 'RS', 'SE', 'TO', 'BA', 'CE', 'DF', 'ES',
            'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO',
            'RR', 'SC','SP']
for grupo in hostgroups:
    group = grupo['name'].split('/')[1]

    if group not in lista_felipe and group not in lista_uf:
        lista_felipe.append(group)
print(lista_felipe)
    # lista_name = grupo['name'].split('/')[2]
    # print(lista_name)

    # options = {
    #     "name": lista_name,
    #     "algorithm": 0,
    #     "parentid": serviceid,
    #     "showsla": 0,
    #     "sortorder": 1
    # }
    # service = zapi.service.create(options)