class viginner:

    def __init__(self,matn,kalit,flag:bool):

        self.natija_ = ""

        if flag:
            key_length = len(kalit)
            for i in range(len(matn)):
                shift = ord(kalit[i % key_length]) - ord('a')
                if matn[i].isalpha():
                    if matn[i].islower():
                        self.natija_ += chr((ord(matn[i]) - ord('a') + shift) % 26 + ord('a'))
                    else:
                        self.natija_ += chr((ord(matn[i]) - ord('A') + shift) % 26 + ord('A'))
                else:
                    self.natija_ += matn[i]
        else:
            key_length = len(kalit)
            for i in range(len(matn)):
                shift = ord(kalit[i % key_length]) - ord('a')
                if matn[i].isalpha():
                    if matn[i].islower():
                        self.natija_ += chr((ord(matn[i]) - ord('a') - shift) % 26 + ord('a'))
                    else:
                        self.natija_ += chr((ord(matn[i]) - ord('A') - shift) % 26 + ord('A'))
                else:
                    self.natija_ += matn[i]

    def natija(self):

        return self.natija_