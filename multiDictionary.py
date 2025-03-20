import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        #gli do i tre oggetti dizionari
        self._english = d.Dictionary([], "english")
        self._italian = d.Dictionary([], "italian")
        self._spanish = d.Dictionary([], "spanish")

        #loadDictionary per tutte le lingue
        self._english.loadDictionary("resources/English.txt")
        self._italian.loadDictionary("resources/Italian.txt")
        self._spanish.loadDictionary("resources/Spanish.txt")


    def printDic(self, language):
        if language == "english":
            self._english.printAll()
        elif language == "italian":
            self._italian.printAll()
        elif language == "spanish":
            self._spanish.printAll()
        else:
            print("Language not supported")

    def searchWord(self, words, language): #con contains

        # words is a list of strings
        parole = []

        for word in words:
            word = word.lower()
            found = False
            richW = rw.RichWord(word)
            if language == "english":
                if self._english.dict.__contains__(word):
                    found = True
            elif language == "italian":
                if self._italian.dict.__contains__(word):
                    found = True
            elif language == "spanish":
                if self._spanish.dict.__contains__(word):
                    found = True
            if found:
                richW.corretta = True
            else:
                richW.corretta = False

            parole.append(richW)

        return parole

    def searchWordLinear(self, words, language):  # con ricerca lineare
        """
        Iterare su tutti gli elementi del vocabolario a partire dal primo. La ricerca termina quando
        viene trovato l' elemento cercato o si raggiunge l’ultimo, nel caso in cui l’elemento cercato
        non sia presente nella lista.

        :param words: lista di parole
        :param language: lingua
        :return: parole
        """
        found = False
        parole = []

        for w in words:
            richW = rw.RichWord(w)
            if language == "italian":
                for wd in self._italian.dict:
                    if w == wd:
                        found = True

            if language == "english":
                for wd in self._english.dict:
                    if w == wd:
                        found = True

            if language == "spanish":
                for wd in self._spanish.dict:
                    if w == wd:
                        found = True

            if found:
                richW.corretta =True
            else:
                richW.corretta= (False)

            parole.append(richW)

        return parole

    def searchWordDichotomic(self, words, language): #con ricerca dicotomica
        """
        Sapendo che il vocabolario è ordinato alfabeticamente, l'idea è quella di non iniziare la ricerca dal primo
        elemento, ma da quello centrale, cioè a metà del dizionario. Si confronta questo elemento con quello cercato:
        - Se corrisponde, la ricerca termina indicando che l'elemento è stato trovato
        - se è superiore, la ricerca viene ripetuta sugli elementi precedenti (ovvero sulla prima metà del
        dizionario), scartando quelli successivi
        - se è inferiore, la ricerca viene ripetuta sugli elementi successivi (ovvero sulla seconda metà del
        dizionario), scartando quelli precedenti.

        Il procedimento viene ripetuto iterativamente fino a quando o si trova l’elemento cercato, o tutti gli elementi
        vengono scartati. In quest’ultimo caso la ricerca termina indicando che il valore non è stato trovato.
        :param words: lista di parole
        :param language: lingua
        :return: parole
        """

        parole = []

        for word in words:

            word = word.lower()
            found = False
            richW = rw.RichWord(word)
            if language == "english":
                currentDic = self._english.dict
                found = dichotomicSearch(word, currentDic)
            elif language == "italian":
                currentDic = self._italian.dict
                found = dichotomicSearch(word, currentDic)
            elif language == "spanish":
                currentDic = self._spanish.dict
                found = dichotomicSearch(word, currentDic)
            if found:
                richW.corretta= True
            else:
                richW.corretta = False

            parole.append(richW)

            return parole

def dichotomicSearch(word, currentDic):
    start = 0
    end = len(currentDic)

    while (start != end):
        mean = start + int((end - start) / 2)
        currentW = currentDic[mean]
        if word == currentW:
            return True
        elif word > currentW:  # in python < applied to strings gives True if the first string is before in lexicographic order
            start = mean + 1
        else:
            end = mean

    return False





