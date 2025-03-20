import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self._multiDic = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        self.txtIn = txtIn
        self.language = language

        testo = replaceChars(txtIn)

        words = testo.split()

        print("-----------------------------------")

        print("Using contains")
        t1 = time.time()
        paroleTrovate = self._multiDic.searchWord(words, self.language) #funziona


        for rw in paroleTrovate:

            if rw.corretta == False:
               print(rw._parola)
        t2 = time.time()
        print("Time elapsed " + str(t2 - t1))

        print("-----------------------------------")
        print("Using Linear")
        t1 = time.time()
        paroleTrovate = self._multiDic.searchWordLinear(words, self.language)  # funziona

        for rw in paroleTrovate:
            #print(rw._parola)  le prende bene
            if rw.corretta == False:
                print(rw._parola)
        t2 = time.time()
        print("Time elapsed " + str(t2 - t1))

        print("-----------------------------------")
        print("Using Dichotomin")
        t1 = time.time()
        paroleTrovate = self._multiDic.searchWordDichotomic(words, self.language)  # funziona
        #print(words) è giusto

        for rw in paroleTrovate:
            #print(rw._parola) prende solo la prima
            if rw.corretta == False:
                print(rw._parola)
        t2 = time.time()
        print("Time elapsed " + str(t2 - t1))


    def printMenu(self):
            print("______________________________\n" +
                  "      SpellChecker 101\n"+
                  "______________________________\n " +
                  "Seleziona la lingua desiderata\n"
                  "1. Italiano\n" +
                  "2. Inglese\n" +
                  "3. Spagnolo\n" +
                  "4. Exit\n" +
                  "______________________________\n")


def replaceChars(text):
 chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
 for c in chars:
    text = text.replace(c, "")
 return text