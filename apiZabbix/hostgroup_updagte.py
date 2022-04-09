from funcoes import conecta_zabbix

zapi = conecta_zabbix()

options = {
    "groupid": "11761", #para realizar a alteração é necessario inserir o groupid
    "name": "CURSO_API/ALUNOS/ALEXANDRE_GASPAR"
}

try:
    zapi.hostgroup.update(options)
    print('codigo atualizado com sucesso')
except Exception as erro:
    print(f"Erro ao atualizar grupo. Erro: {erro}")