import config
from pyzabbix import ZabbixAPI
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def connect_rfb_prod():

    url = http://10.31.3.88
    USERNAME = '02812141743'
    PASSWORD = 'serpro123'

    zapi = ZabbixAPI(url)

    # Enable HTTP auth
    zapi.session.auth = (USERNAME, PASSWORD)

    # Disable SSL certificate verification
    zapi.session.verify = False

    # Specify a timeout (in seconds)
    zapi.timeout = 20

    # Login (in case of HTTP Auth, only the username is needed, the password, if passed, will be ignored)
    try:
        zapi.login(USERNAME, PASSWORD)
        print('Conectado na API do Zabbix, versÃ£o: {}'.format(zapi.api_version()))
    except Exception as err:
        print('Falha ao conectar na API do Zabbix')
        print('Erro: {}'.format(err))

    # You can also authenticate using an API token instead of user/pass with Zabbix >= 5.4
    # zapi.login(api_token='xxxxx')

    return zapi
