from charm.core.math.integer import integer
from charm.schemes.chamhash_adm05 import ChamHash_Adm05
from charm.schemes.pre_mg07 import PreGA
from charm.toolbox.pairinggroup import PairingGroup, pc_element  
from charm.schemes.ibenc.ibenc_waters05 import IBE_N04
from charm.toolbox.pairinggroup import PairingGroup, GT, ZR
from charm.toolbox.hash_module import Waters
from charm.core.engine.util import objectToBytes, bytesToObject
from charm.adapters.abenc_adapt_hybrid import HybridABEnc


# https://github.com/JHUISI/charm/blob/acb55513b244bfdebbfe715cec7b564c8e850779/charm/schemes/ibenc/ibenc_waters05.py
class ThirdParty:
    def __init__(self):
        self.group = PairingGroup('SS512')
        self.waters_hash = Waters(self.group)
        self.ibe = IBE_N04(self.group)
        (master_public_key, master_key) = self.ibe.setup()
        self.master_public_key = master_public_key
        self.master_key = master_key

    def id_enc(self, ID, msg):
        # ID = "bob@mail.com"
        # msg = self.group.random(GT)
        kID = self.waters_hash.hash(ID)
        msg_init = self.group.init(ZR, msg)
        cipher_text = self.ibe.encrypt(self.master_public_key, kID, msg_init)
        print(type(cipher_text['c1']))
        return objectToBytes(cipher_text, self.group)

    def id_dec(self, ID, cipher_text):
        cipher_object = bytesToObject(cipher_text, self.group)
        kID = self.waters_hash.hash(ID)
        secret_key = self.ibe.extract(self.master_key, kID)
        decrypted_msg = self.ibe.decrypt(self.master_public_key, secret_key, cipher_object)
        # decrypted_msg == msg
        return decrypted_msg
