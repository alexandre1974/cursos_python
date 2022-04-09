from funcoes import *
import csv
from pprint import pprint

zapi = conecta_zabbix()
options = {
    "filter": {"name": 'CURSO_API_ZABBIX'},
    "output": ['serviceid']
}
serviceid = zapi.service.get(options)[0]['serviceid']
print(serviceid)
options = {
    "serviceid": serviceid,
    "name": "CURSO_API"
}

zapi.service.update(options)

zapi.logout()