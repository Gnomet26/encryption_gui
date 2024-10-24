import hashlib

class SHA256:
    def __init__(self,matn:str):

        self.natija_ = hashlib.sha256(b"" + matn.encode("utf-8"))

    def natija(self):

        return self.natija_.hexdigest()