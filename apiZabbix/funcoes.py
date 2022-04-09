
def conecta_zabbix():

    from zabbix_api import ZabbixAPI

    URL = 'http://treina.monitoracao.serpro'
    USERNAME = '02812141743'
    PASSWORD = '@adriano74'

    # USERNAME = 'curso_api'
    # PASSWORD = 'zabbix'

    try:
        conexao = ZabbixAPI(URL, timeout=600)
        conexao.login(USERNAME, PASSWORD)
        print(f'conexao foi realizado com sucesso {conexao.api_version()}')
    except Exception as erro:
        print(f'falha ao conectar ao Zabbix')
        print (f'Erro : {erro}')
    return conexao

# Função para criar grupo de host

def criar_grupo(zapi, name):
    try:
        zapi.hostgroup.create({
            "name": name
        })
        print(f'Grupo {name} criado com sucesso')
    except Exception as erro:
        print(f"Erro ao criar grupo {name}. Erro: {erro}")

def get_hostgroups(zapi, name):

    options = {
        "output": ['groupid'],
        "filter": {"name": name}
        }

    grupo = zapi.hostgroup.get(options)
    return {
        "groupid": grupo[0]['groupid']
    }

def get_hosttemplates(zapi, name):

    options = {
        "output": ['templateid'],
        "filter": {"host": name}
        }

    template = zapi.template.get(options)
    return {
        "templateid": template[0]['templateid']
    }

#Funçao cria host com os dados recebidos

def criar_host(zapi, options):
    #print(options)
    hostname = options['host']
    try:
         zapi.host.create(options)
         print(f'O host {hostname} foi criado com sucesso!')
    except Exception as erro:
         print(f"Erro ao criar o host {hostname}. Erro: {erro}")

#funçao que converte string de data para timestamp

def convert_datestr_to_timestamp(datestring):
    from datetime import datetime
    date_time_obj = datetime.strptime(datestring, '%d/%m/%Y %H:%M')
    return date_time_obj.timestamp()

#funcao que converte timestamp em data

def convert_timestamp_to_datestr(timestamp):
    from datetime import datetime
    date_time = datetime.fromtimestamp(timestamp)
    date_string = date_time.strftime('%d/%m/%Y %H:%M')
    return date_string

#funçao que retorna o serviceid do serviço, informado ou criado caso ele não exista e retorna o ID do serviço criado

def criar_service(zapi, name, parentid, triggerid=0):
    options = {
        "filter": {"name": name},
        "output": ["serviceid"],
        "parentids": parentid
    }
    servicos = zapi.service.get(options)
    if servicos:
        print(f"Servicos {name} já existe")
        return servicos[0]['serviceid']
    else:
        options = {
            "name": name,
            "algorithm": 1,
            "sortorder": 1,
            "showsla": 1,
            "parentid": parentid,
            "triggerid": triggerid,
            "goodsla": 99
        }
    try:
        services= zapi.service.create(options)
        print(f'Serviço {name} criado com sucesso')
        return services['serviceids'][0]
    except Exception as erro:
        print(f'Erro ao criar serviço {name} com o erro: {erro}')