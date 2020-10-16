class Etudiant:
    def __init__(self, prenom, nom, age, note_moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.note_moyenne = note_moyenne

    def __str__(self):
        return '\n({} {} {} {})'.format(self.prenom, self.nom, self.age, self.note_moyenne)

    def __repr__(self):
        return self.__str__()