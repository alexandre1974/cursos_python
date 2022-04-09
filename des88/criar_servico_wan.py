from apizabbix import *

zapi = conecta_zabbix(site("88"))

options = {

        "name": "WAN",
        "algorithm": 0,
        "parentid": "24107",
        "showsla": 0,
        "sortorder": 1

}

service = zapi.service.create(options)
print(service)
