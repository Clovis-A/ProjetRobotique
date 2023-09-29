
import paho.mqtt.client as mqtt
import time

# Permet de lire les messages reçus et de les stockées dans le fichier log.txt
def on_mes(client, userdata, mes):
    date_actuelle = time.strftime("%Y-%m-%d")
    heure_actuelle = time.strftime("%H:%M:%S")
    msg = mes.payload.decode("utf-8") # decode message
    #save message in file
    with open('log.txt', 'a') as file:
        file.write(date_actuelle+ " "+heure_actuelle +" -> " + mes.topic + " -> " + msg + "\n")

    print("Received message: ", msg," on topic ", mes.topic)
    """client.loop_stop()
    client.disconnect()"""

# Permet de se connecter au broker et de s'abonner au topic Junia/Robot/#
client = mqtt.Client()
client.on_message = on_mes
client.connect("test.mosquitto.org", 1883)
client.subscribe("JuniaLaboRobot/#")
client.loop_forever()
