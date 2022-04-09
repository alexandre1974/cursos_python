from funcoes import *
import csv
from pprint import pprint
from statistics import mean

zapi = conecta_zabbix()

#Lendo dados de serviços

# options = {
#     "filter": {'name': 'INTERNET'},
#     "output": ['name','goodsla'],
#     "selectDependencies": 'extend'
# }
#intervalo de tempo de medição

date_from = '11/06/2020 00:00'
date_from = convert_datestr_to_timestamp(date_from)
date_fill = '10/07/2020 23:59'
date_fill = convert_datestr_to_timestamp(date_fill)

options = {
    "search": {'name': '_PGFN_'},
    "output": ['name', 'goodsla']
}
servicos =zapi.service.get(options)
for servico in servicos:

    options = {
        "serviceids": servico['serviceid'],
        "intervals":[
            {
                "from": date_from,
                "to": date_fill,
            }
        ]
    }


    sla_data = zapi.service.getsla(options)
    sla = round(sla_data[servico['serviceid']]['sla'][0]['sla'], 2)
    nome = servico['name'].split('(')[0]
    print(f' Nome : {nome} , SLA : {sla}%')


zapi.logout()