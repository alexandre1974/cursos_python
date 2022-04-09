from funcoes import *
import csv
from pprint import pprint
from statistics import mean

zapi = conecta_zabbix()

#coletando itens de template

#lista intens de um template

'''
options = {
    "filter": {"host": "101 - Linux Complementar"}
}

templateid = zapi.template.get(options)[0]['templateid']

#pprint(templateid)

options = {
    "templateids": templateid,
    "output": ['name', 'key_', 'delay', 'lastvalue'],
    "selectTriggers": ['descriptions']

}

items = zapi.item.get(options)
#pprint(items)
for item in items:
    print('ITEM =' + item['name'], item['key_'], item['delay'], item['lastvalue'])
    for trigger in item['triggers']:
        pprint(trigger)
        #print('  -' + trigger['description'])
        


options = {
    "filter": {"host": "spopvm019034"},
    "output": ["host"],
    "selectItems": ['itemid', 'name', 'lastvalue']
}
hosts = zapi.host.get(options)

hostid = hosts[0]['hostid']
host_host = hosts[0]['host']

arquivo = open('relatorio_host.txt', 'w', encoding='UTF-8')
msg = f'Relatorio de items do host {host_host} '
print(msg + '\n')
arquivo.write(msg + '\n')
print('')
for item in hosts[0]['items']:
    #print(item)
    item_name = item['name']
    item_value = item['lastvalue']
    itemid = item['itemid']
    print(f'  - ITEM: {item_name} = {item_value} '+'\n')
    arquivo.write(f'  - ITEM: {item_name} = {item_value} ' + '\n')
    #print(f'    Itemid = {itemid}')

    options = {
        "itemids": itemid,
        "selectTriggers": ['description'],
        "selectGraphs": ['name']
    }
    items = zapi.item.get(options)
    for item in items:
        for trigger in item['triggers']:
            print('   t = ' + trigger['description'])
            arquivo.write('   t = ' + trigger['description'] + '\n')
        for graph in item['graphs']:
            print('   g = ' + graph['name'])
            arquivo.write('   g = ' + graph['name'] + '\n')

arquivo.close()

'''

#Explorar histórico de items

options = {
    "filter": {"host": "spopvm019034"},
    "output": ["hostid"],
}
hostid = zapi.host.get(options)[0]['hostid']
print(hostid)
options = {
    "output": ["itemid"],
    "hostids": hostid,
    "filter": {"key_": "net.if.in[eth0]"}
}
itemid = zapi.item.get(options)[0]['itemid']
print(itemid)
date_from = '21/07/2021 00:00'
date_from = convert_datestr_to_timestamp(date_from)
date_fill = '21/07/2021 09:00'
date_fill = convert_datestr_to_timestamp(date_fill)

options = {
    "output": ['clock', 'value'],
    "itemids": itemid,
    "time_from": int(date_from),
    "time_till": int(date_fill),
    "sortfield": 'clock',
    "sortorder": 'DESC'
}
hist = zapi.history.get(options)
valores = []
for dado in hist:
    valores.append(int(dado['value']))
print(valores)

minimo = round(min(valores)/1000, 2)
print(minimo)
maximo = round(max(valores)/1000, 2)
media = round(mean(valores)/1000, 2)
media2 = round(sum(valores)/len(valores)/1000, 2)
ultimo = round(valores[-1]/1000, 2)
print(minimo, maximo, media)
print(f'O menor valor é: {minimo}')
print(f'O maior valor é: {maximo}')
print(f'O media dos valores é: {media}')
print(f'O último valor e: {ultimo}')

zapi.logout()