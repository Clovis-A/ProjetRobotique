import ObjetClass as Objet


class Mobile(Objet.Objet):
    def __init__(self, nom, description, type_mobile):
        super().__init__(nom, description)
        self.type_mobile = type_mobile  # Aerien ou Terrestre
        self.destination = None  # Destination du mobile
        self.vitesse = None
        self.batterie = None  # Niveau de batterie
        self.etat = None  # En marche, en cours de recharge ,ou en panne
        self.isCharge = None  # Pour savoir si le mobile porte un objet ou non

    # Getters
    def get_type_mobile(self):
        return self.type_mobile

    def get_destination(self):
        return self.destination

    def get_vitesse(self):
        return self.vitesse

    def get_batterie(self):
        return self.batterie

    def get_etat(self):
        return self.etat

    def get_isCharge(self):
        return self.isCharge

    # Setters
    def set_type_mobile(self, type_mobile):
        self.type_mobile = type_mobile

    def set_destination(self, destination):
        self.destination = destination

    def set_vitesse(self, vitesse):
        self.vitesse = vitesse

    def set_batterie(self, batterie):
        self.batterie = batterie

    def set_etat(self, etat):
        self.etat = etat

    def set_isCharge(self, isCharge):
        self.isCharge = isCharge
