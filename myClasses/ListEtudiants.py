class ListEtudiants(list):
    def __iter__(self):
        return IterListEtudiants(self)


class IterListEtudiants:
    def __init__(self, le: [ListEtudiants]):
        self.le = le
        self.index = len(le)

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.le[self.index]
