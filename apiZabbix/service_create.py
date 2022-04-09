from funcoes import *
import csv
from pprint import pprint

zapi = conecta_zabbix()

options = {
    "filter": {'name': 'Serviços'},
    "output": ['serviceid']
}
servicos_serviceid = zapi.service.get(options)[0]['serviceid']

curso_servicoid = criar_service(zapi, 'CURSO_API', servicos_serviceid)
aluno_serviceid = criar_service(zapi, 'ALUNO', curso_servicoid)
print(aluno_serviceid)

zapi.logout()