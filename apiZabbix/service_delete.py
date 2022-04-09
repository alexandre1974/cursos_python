from funcoes import *
import csv
from pprint import pprint

zapi = conecta_zabbix()

serviceids_to_delete = []

options = {
    "filter": {"name": "GASPAR"},
    "output": ['serviceid'],
    "selectDependencies": ['serviceid']
}
services = zapi.service.get(options)
serviceids_to_delete.append(services[0]['serviceid'])

while services[0]['dependencies']:
    child_serviceids = []
    for service in services:
        for dep in service['dependencies']:
            child_serviceids.append(dep['serviceid'])
            serviceids_to_delete.append(dep['serviceid'])
    options = {
        "serviceids": child_serviceids,
        "output":['serviceid'],
        "selectDependencies": ['serviceid']
        }
    services = zapi.service.get(options)

print(serviceids_to_delete)

try:
    zapi.service.deletedependencies(serviceids_to_delete)
    zapi.service.delete(serviceids_to_delete)
    print("servicos deletados")
except Exception as erro:
    print(f'Erro ao atualizar serviço: {erro}')

zapi.logout()