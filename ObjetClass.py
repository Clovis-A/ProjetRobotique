import MQTT.MQTTPub as MQTTPub

class Objet:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description
        self.position = None
        self.dernier_message = None
        self.MQTTTopic = None  # Concernant les messages mqtt

    # Getters
    def get_nom(self):
        return self.nom

    def get_position(self):
        return self.position

    def get_dernier_message(self):
        return self.dernier_message

    def get_MQTTTopic(self):
        return self.MQTTTopic

    # Setters
    def set_nom(self, nom):
        self.nom = nom

    def set_position(self, position):
        self.position = position

    def set_dernier_message(self, dernier_message):
        self.dernier_message = dernier_message

    def set_MQTTTopic(self, MQTTTopic):
        self.MQTTTopic = MQTTTopic

    # Methods
    def MQTTEnvoieMessage(self, message):
        """
        :description: Permet d'envoyer un message sur le topic de l'objet
        :param message: message à envoyer sur le topic
        """
        MQTTPub.MQTTPublish(self.MQTTTopic, message)


