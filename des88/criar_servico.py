from apizabbix import *
from pprint import pprint

zapi= conecta_zabbix(site("88"))

options = {
    #"output":['name','servicedownid'],
    "filter": {"name": "ANTAQ"},
    "selectDependencies": ['serviceupid'],
    #"serviceid": "1",

   # "name": "WAN",
   # "algorithm": 0,
    #"parentid": "24107",
    #"showsla": 0,
   #"sortorder": 1

}

lista_services = zapi.service.get(options)
pprint(lista_services)
dependencia = (lista_services[0]['dependencies'])
i = 0
for serviceid in dependencia:
    serviceid = (dependencia[i]['serviceid'])
    #print(serviceid)
    i += 1

    options = {
        "output": ['name'],
        "serviceids": serviceid
    }

    name = zapi.service.get(options)[0]['name']
    #print(name)

    # options = {
    #
    #     "name": name,
    #     "algorithm": 0,
    #     "parentid": "24125",
    #     "showsla": 0,
    #     "sortorder": 1
    #
    # }
    #
    # service = zapi.service.create(options)

zapi.logout()