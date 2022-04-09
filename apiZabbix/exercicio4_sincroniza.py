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
aluno_serviceid = criar_service(zapi, 'ALUNOS', curso_servicoid)
nome_serviceid = criar_service(zapi, 'GASPAR', aluno_serviceid )
print(aluno_serviceid)

#Checando grupo de hosts e host

options = {
    "search": {'name': "CURSO_API/ALUNOS/GASPAR"},
    "output": ['name'],
    "selectHosts": ['hostid', 'host']

}

grupos = zapi.hostgroup.get(options)

for grupo in grupos:
    print(grupo)
    nome = grupo['name'].split('/')[3]
    grupo_serviceid = criar_service(zapi, nome, nome_serviceid)
    for host in grupo['hosts']:
        host_serviceid = criar_service(zapi, host['host'], grupo_serviceid)
        options = {
            "hostids": host['hostid'],
            "filter": {"nome": "Dispositivo {HOST.HOST} Insdiponível há mais de 5 minutos"},
            "output": ['trigerid']
        }
        triggerid = zapi.trigger.get(options)[0]['triggerid']
        trigger_serviceid = criar_service(zapi, "Disponibilidade do Host", host_serviceid, triggerid)


zapi.logout()