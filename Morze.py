class morze:
    def __init__(self,matn,flag:bool):

        self.natija_ = ""
        self.harflar = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                        "t", "u", "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9","0",".",',']
        self.cod = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--..","--.-",".-.","...",
                    "-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....","-....","--...",
                    "---..","----.","-----",".-.-.-","--..-"]
        self.index = 0

        if flag:
            for j in range(len(matn)):
                for i in self.harflar:
                    if matn[j] == i:
                        self.natija_ += self.cod[self.index] +"/"
                    self.index += 1
                self.index = 0
        else:
            self.masiv = []

            self.harf = ""

            for i in range(len(matn)):

                if(matn[i] != "/"):
                    self.harf += matn[i]

                else:
                    self.masiv.append(self.harf)
                    self.harf = ""


            for i in self.masiv:
                for j in range(len(self.cod)):

                    if i == self.cod[j]:
                        self.natija_ += self.harflar[j]


    def natija(self):

        return self.natija_
        pass