from funcoes import conecta_zabbix

zapi = conecta_zabbix()

options = [11764] #Deverá ser esse formato para delete aonde o número será o ID

try:
    zapi.hostgroup.delete(options)
    print('Deletado com sucesso')
except Exception as erro:
    print(f"Erro ao deletar grupo. Erro: {erro}")