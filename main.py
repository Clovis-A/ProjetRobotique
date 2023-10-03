

if __name__ == '__main__':
    # deéclaration des variables
    dernier_message = ["topic", "message"]
    dernier_message_traite = "None"
    while True:
        i=1
        # Lire dans les logs
        with open('MQTT/log.txt', 'r') as file:
            dernier_message_NON_traite = file.readlines()[-i]
            # Trouve le dernier message non traité
            while dernier_message_traite!=dernier_message_NON_traite:
                i-=1
                dernier_message_NON_traite = file.readline()[-i]
            dernier_message_traite = dernier_message_NON_traite

            # sépare le message du topic et enlève l'heure
            dernier_message[0] = dernier_message_traite.split("->")[1].split("/")
            dernier_message[1] = dernier_message_traite.split("->")[2]
            """
            Notes de fonctionnement:
            dernier_message[0] = topic
            dernier_message[1] = message
            mais dernier_message[0] est une liste de 4 éléments
            dernier_message[0][0] = JuniaLaboRobot
            dernier_message[0][1] = Mobile ou Fixe
            dernier_message[0][2] = Aerien ou Terrestre
            dernier_message[0][3] = Nom du robot ou du système associé
            """

            # gestion des différents messages reçus
            if dernier_message[0][1] == "Mobile":
                print( "cela est important car cela concerne le mobile")
                if (dernier_message[0][2]=="Aerien"):
                    print("cela concerne un drone")
                elif (dernier_message[0][2]=="Terrestre"):
                    print("cela concerne un robot terrestre")
            elif dernier_message[0][1] == "Fixe":
                print("cela concerne une mission ou une information")


