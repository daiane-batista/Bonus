import paho.mqtt.client as mqtt
import random
import json
import time

print('Conectando ao MQTT Broker...')
mqtt_client = mqtt.Client()
mqtt_client.connect('localhost',1883)

#while True:

temperatura = random.uniform(34,40)
print(temperatura)

mensagem = {
    'cliente': 'Inatel',
    'temperatura': temperatura
}

mqtt_client.publish('in242',json.dumps(mensagem))

    #time.sleep(5)