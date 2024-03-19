import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.it = d.Dictionary()
        self.it.loadDictionary("resources/Italian.txt")
        self.sp = d.Dictionary()
        self.sp.loadDictionary("resources/Spanish.txt")
        self.en = d.Dictionary()
        self.en.loadDictionary("resources/English.txt")

    def printDic(self, language):
        if language == "italian":
            self.it.printAll()
        elif language == "english":
            self.en.printAll()
        elif language == "spanish":
            self.sp.printAll()

    def searchWord(self, words, language):
        parole = []
        for word in words.split():
            rich = rw.RichWord(word.lower())
            parole.append(rich)
            if language == "italian":
                if self.it.searchWord(word.lower()) == True:
                    rich._corretta=True
                else:
                    rich._corretta=False
            elif language == "english":
                if self.en.searchWord(word.lower()) == True:
                    rich._corretta=True
                else:
                    rich._corretta = False
            elif language == "spanish":
                if self.sp.searchWord(word.lower()) == True:
                    rich._corretta=True
                else:
                    rich._corretta=False
        return [cos for cos in parole if cos._corretta == False]

    def searchWordL(self, words, language):
        parole = []
        for word in words.split():
            rich = rw.RichWord(word.lower())
            parole.append(rich)
            if language == "italian":
                if self.it.searchWordLineare(word.lower()) == True:
                    rich._corretta=True
                else:
                    rich._corretta=False
            elif language == "english":
                if self.en.searchWordLineare(word.lower()) == True:
                    rich._corretta=True
                else:
                    rich._corretta = False
            elif language == "spanish":
                if self.sp.searchWordLineare(word.lower()) == True:
                    rich._corretta=True
                else:
                    rich._corretta=False
        return [cos for cos in parole if cos._corretta == False]

    def searchWordD(self, words, language):
        parole = []
        for word in words.split():
            rich = rw.RichWord(word.lower())
            parole.append(rich)
            if language == "italian":
                if self.it.searchWordDicotomica(word.lower()) == True:
                    rich._corretta=True
                else:
                    rich._corretta=False
            elif language == "english":
                if self.en.searchWordDicotomica(word.lower()) == True:
                    rich._corretta=True
                else:
                    rich._corretta = False
            elif language == "spanish":
                if self.sp.searchWordDicotomica(word.lower()) == True:
                    rich._corretta=True
                else:
                    rich._corretta=False
        return [cos for cos in parole if cos._corretta == False]