
import paho.mqtt.client as mqtt

# Permet d'écrire des messages sur un topic
def MQTTPublish(topic, message):
    def on_pub(client, userdata, result):
        print("data published \n")
        client.loop_stop()
        client.disconnect()

    client = mqtt.Client()
    client.on_publish = on_pub
    client.connect("test.mosquitto.org", 1883)
    client.publish(topic, message)


import time
for i in range(10):
    time.sleep(1)
    if i % 2 == 0:
        MQTTPublish("JuniaLaboRobot/Mobile/Terrestre/Tino1", "robot 1 available")
    else:
        MQTTPublish("JuniaLaboRobot/Mobile/Terrestre/Tino2", "robot 2 available")
