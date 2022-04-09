from funcoes import conecta_zabbix, criar_grupo
import csv

zapi = conecta_zabbix()
'''
options = {
    "name": "CURSO_API/ALUNOS/GASPAR/SERVIDORES"
}

try:
    zapi.hostgroup.create(options) #COMENTO PARA CRIA HOSTGROUP
    print('codigo criado com sucesso')
except Exception as erro:
    print(f"Erro ao criar grupo. Erro: {erro}")
'''

with open('exercicio1.cvs') as file:
    linhas = csv.reader(file, delimiter = ';')
    for [grupo] in linhas:
        criar_grupo(zapi, grupo)
        #print(grupo)
