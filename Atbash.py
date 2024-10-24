class atbash:
    def __init__(self,matn,flag:bool):

        self.natija_ = ""
        self.harflar = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                        "t", "u", "v", "w", "x", "y", "z"]
        self.index = 0

        if flag:
            for j in range(len(matn)):
                for i in self.harflar:
                    if matn[j] == i:
                        self.natija_ += self.harflar[25-self.index]
                    self.index += 1
                self.index = 0
        else:
            for j in range(len(matn)):
                for i in self.harflar:
                    if matn[j] == i:
                        self.natija_ += self.harflar[25-self.index]
                    self.index += 1
                self.index = 0


    def natija(self):

        return self.natija_
        pass