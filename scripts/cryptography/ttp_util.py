from scripts.cryptography.identity_crypto import IdCrypto
from scripts.cryptography.attribute_crypto import AttributeCrypto


class ThirdParty:
    def __init__(self):
        self.id_crypt = IdCrypto()
        self.att_crypt = AttributeCrypto()

    def id_enc(self, msg, ID):
        return self.id_crypt.enc(msg, ID)

    def id_dec(self, cipher_text, ID):
        return self.id_crypt.dec(cipher_text, ID)

    def att_enc(self, msg, policy):
        return self.att_crypt.enc(msg, policy)

    def att_dec(self, cipher_text, attributes):
        return self.att_crypt.dec(cipher_text, attributes)

        

    

    
