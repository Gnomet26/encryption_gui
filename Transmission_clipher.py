class transmission_clipher:

    def __init__(self,matn,kalit,flag:bool):

        self.natija_ = ""

        if flag:
            index2 = 0
            index = 0

            natija = ""

            data = []
            ustunlar = []

            for i in "" + kalit:
                ustunlar.append(int(i))

            massiv_x = int(len(kalit))
            helper = int(len(matn))

            if helper > 0:
                massiv_y = int(len(matn.replace(" ", "")) / massiv_x) + 1
            else:
                massiv_y = int(len(matn.replace(" ", "")) / massiv_x)

            for i in range(massiv_y):
                mms = []
                for j in range(massiv_x):
                    try:
                        mms.append(matn[index])
                        pass
                    except:
                        mms.append("x")
                    index += 1
                data.append(mms)

            for i in range(massiv_x):
                for j in range(massiv_y):
                    natija += data[j][ustunlar[index2] - 1]
                index2 += 1

            self.natija_ = natija
        else:
            pass

    def natija(self):

        return self.natija_