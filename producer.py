import paho.mqtt.client as mqtt
import random
import json
import time

print('Conectando ao MQTT Broker...')
mqtt_client = mqtt.Client()
mqtt_client.connect('localhost',1883)

qtdade = 0

while True:

    sensor = random.randint(0,1)
    print(sensor)

    if sensor == 1:
        qtdade = qtdade + 1

        mensagem = {
            'Local': 'Porta-A',
            'Contagem': 'de pessoas',
            'Quantidade': qtdade
        }

        mqtt_client.publish('in242',json.dumps(mensagem))

    elif qtdade ==0:
        mensagem = {
            'Local': 'Roleta-A',
            'Contagem': 'de pessoas',
            'Quantidade': qtdade
        }

        mqtt_client.publish('in242', json.dumps(mensagem))

    #time.sleep(30)