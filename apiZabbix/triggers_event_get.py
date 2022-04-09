from funcoes import *
import csv
from pprint import pprint

zapi = conecta_zabbix()

#identificando a trigger

options = {
    "output": ['description', 'priority', 'value'],
    "host": "dfcdsrvv4650"
}

triggers = zapi.trigger.get(options)
lista_value = ['OK', "PROBLEM"]
lista_severidade = ['NAO CLASSIFICADOS', 'INFORMACAO', 'ATENCAO', 'MEDIA', 'ALTA', 'DESASTRE']
date_from = convert_datestr_to_timestamp('06/08/2021 00:00')
for trigger in triggers:
    if int(trigger['value']):
        print('TRIGGER : ' + trigger['description'], lista_value[int(trigger['value'])])
        options = {
            "output": ['name', 'clock', 'severity', 'value', 'r_eventid'],
            "objectids": trigger['triggerid'],
            "sortfield": "clock",
            "sorterder":"DESC",
            "value": 1,
            "select_acknowledges": ['alias', 'message']
            #"time_from": date_from,
            #"acknowledged": True
        }

        events = zapi.event.get(options)

        for event in events:
            if not int(event['r_eventid']):
                print(' - EVENTOS : ' + event['name'], ' -- ' + lista_severidade[int(event['severity'])], ' -- ' + convert_timestamp_to_datestr(int(event['clock'])))
                for ack in event['acknowledges']:
                    print(' --- ACKNOWLEDGE : ' + ack['alias'], ack['message'])