
from zabbix_api import ZabbixAPI

    URL = ''
    USERNAME = '02812141743'
    PASSWORD = '@adriano74'

try:
    conexao = ZabbixAPI(URL, timeout=60)
    conexao.login(USERNAME, PASSWORD)
    print(f'conexao foi realizado com sucesso {conexao.api_version()}')
except Exception as erro:
    print(f'falha ao conectar ao Zabbix')
    print(f'Erro : {erro}')
return conexao