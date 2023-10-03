import ObjetClass as Objet


class Fixe(Objet.Objet):
    def __init__(self, nom, description, type_fixe):
        super().__init__(nom, description)
        self.type_fixe = type_fixe

