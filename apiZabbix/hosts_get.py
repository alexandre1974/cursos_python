from funcoes import conecta_zabbix
import csv
from pprint import pprint
zapi = conecta_zabbix()

options = {
    "output": ['host','name','status'],
    "search": {"host":"labgir"},
    "selectInterfaces":['ip'],
    "selectInventory":['type','os','hardware'],
    "selectGroups":['name'],
    "selectMacros":['macro','value']

}

hosts = zapi.host.get(options)

for host in hosts:
    host_host = host['host']
    host_name = host['name']
    ip = host['interfaces'][0]['ip']
    status = host['status']
    tipo = host['inventory']['type']
    """
    if int(status) == 0:
        status_host = "ATIVO"
    else:
        status_host = "INATIVO"
    """
    lista_status = ["Ativo","Inativo"]
    status_host = lista_status[int(status)]

    print(host_host,host_name,ip,status, status_host, tipo)

zapi.logout()


