from charm.core.math.integer import integer
from charm.schemes.chamhash_adm05 import ChamHash_Adm05
from charm.schemes.pre_mg07 import PreGA
from charm.toolbox.pairinggroup import PairingGroup, pc_element  
from charm.schemes.ibenc.ibenc_waters05 import IBE_N04
from charm.schemes.ibenc.ibenc_bf01 import IBE_BonehFranklin
from charm.toolbox.pairinggroup import PairingGroup, GT, ZR
from charm.toolbox.hash_module import Waters
from charm.core.engine.util import objectToBytes, bytesToObject
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
import pickle
from charm.core.math.integer import integer


# https://github.com/JHUISI/charm/blob/acb55513b244bfdebbfe715cec7b564c8e850779/charm/schemes/ibenc/ibenc_bf01.py
class ThirdParty:
    def __init__(self):
        self.group = PairingGroup('MNT224', secparam=1024)  
        self.ibe = IBE_BonehFranklin(self.group)
        (master_public_key, master_secret_key) = self.ibe.setup()
        self.master_public_key = master_public_key
        self.master_secret_key = master_secret_key

    def id_enc(self, ID, msg):
        cipher_text = self.ibe.encrypt(self.master_public_key, ID, msg)
        # print(cipher_text, type(cipher_text))
        for k in cipher_text:
            if str(type(cipher_text[k])) == "<class 'integer.Element'>":
                cipher_text[k] = int(cipher_text[k])
            else:
                cipher_text[k] = self.group.serialize(cipher_text[k])
        # print(cipher_text)
        pickled = pickle.dumps(cipher_text)
        return pickled

    def id_dec(self, ID, cipher_text):
        cipher_object = pickle.loads(cipher_text)
        for k in cipher_object:
            if type(cipher_object[k]) is int:
                cipher_object[k] = integer(cipher_object[k])
            else:
                cipher_object[k] = self.group.deserialize(cipher_object[k])
        private_key = self.ibe.extract(self.master_secret_key, ID)
        decrypted_msg = self.ibe.decrypt(self.master_public_key, private_key, cipher_object)
        return decrypted_msg
