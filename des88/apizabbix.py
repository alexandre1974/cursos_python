import sys
import locale
import datetime
from time import sleep
from zabbix_api import ZabbixAPI

URL = 'http://192.168.100.40/zabbix'
#USERNAME = 'Admin'
#PASSWORD = 'zabbix'
USERNAME = 'apizabbix'
PASSWORD = 'nprsitw'


def site(cod):
    sites = [('zu', 'http://192.168.100.40/zabbix'),
             ('hom', 'http://hom.monitoracao.serpro'),
             ('200', 'http://192.168.100.40/zabbix'),
             ('prod', 'https://monitoracao.serpro'),
             ('34', 'https://10.31.19.34'),
             ('88', 'http://10.31.3.88')

             ]

    sitess = dict(sites)
    return sitess[cod]


def conecta_zabbix(siteapi):
    try:
        #zapi = ZabbixAPI(URL, timeout=180)
        zapi = ZabbixAPI(siteapi, timeout=10, validate_certs=False)
        # Disable SSL certificate verification
        zapi.login(USERNAME, PASSWORD)
        print('Conectado na API do Zabbix, versão: {}'.format(zapi.api_version()))
    except Exception as err:
        print('Falha ao conectar na API do Zabbix')
        print('Erro: {}'.format(err))
    return zapi


def checa_data(date_text):
    try:
        data = datetime.datetime.strptime(date_text, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Data Inválida, formato aceito DD/MM/AAAA")
    return data
