class Dictionary:
    def __init__(self, dict, language):
        self._dict = dict
        self.language = language

    def loadDictionary(self,path):
        file_path = path

        with open(file_path, 'r', encoding="utf-8") as file:
            lines = [line.strip().lower() for line in file]
            self._dict = lines #lista di parole nel dizionario

    def printAll(self):
        for value in self._dict:
            print(f"{value}")


    @property
    def dict(self):
        return self._dict