class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self, path):
        file = open(path, "r", encoding="utf-8")
        for riga in file.readlines():
                self._dict.append(Word(riga.strip()))
        file.close()

    def printAll(self):
        for w in self._dict:
            print(w)

    @property
    def dict(self):
        return self._dict

    def searchWord(self, word):
        if self._dict.__contains__(word):
            return True
        else:
            return False
    def searchWordLineare(self,word):
        for w in self._dict:
            if w.parola == word:
                return True
        return False

    def searchWordDicotomica(self,wordi):
        l=len(self._dict)//2
        if self._dict[l].parola==wordi:
            return True
        elif self._dict[l].parola>wordi:
            for w in self._dict:
                if w.parola == wordi:
                    return True
            return False
        else:
            for w in reversed(self._dict):
                if w.parola == wordi:
                    return True
            return False




class Word:
    def __init__(self, parola):
        self.parola = parola

    def __str__(self):
        return self.parola
