import time
import multiDictionary as md


class SpellChecker:

    def __init__(self):
        self.multi = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        testo=replaceChars(txtIn)
        start=time.time()
        paroleErrate = self.multi.searchWord(testo, language)
        if len(paroleErrate)==0:
            print("Nessuna Parola Errata")
        else:
            print("Parole errate: ")
            for cos in paroleErrate:
                print(cos)
        end=time.time()
        print(f"tempo di esecuzione: {end-start} ")
        print("---------------------------------")
        start = time.time()
        paroleErrate = self.multi.searchWordL(testo, language)
        if len(paroleErrate) == 0:
            print("Nessuna Parola Errata")
        else:
            print("Parole errate: ")
            for cos in paroleErrate:
                print(cos)
        end = time.time()
        print(f"tempo di esecuzione Lineare: {end - start} ")

        print("---------------------------------")
        start = time.time()
        paroleErrate = self.multi.searchWordD(testo, language)
        if len(paroleErrate) == 0:
            print("Nessuna Parola Errata")
        else:
            print("Parole errate: ")
            for cos in paroleErrate:
                print(cos)
        end = time.time()
        print(f"tempo di esecuzione Dicotomica: {end - start} ")



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n" +
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