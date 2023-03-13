from charm.core.math.integer import integer
from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, GT
from charm.toolbox.policytree import PolicyParser
from charm.schemes.abenc.abenc_waters09 import CPabe09
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from charm.toolbox.ABEnc import *
from charm.core.engine.util import objectToBytes, bytesToObject
import base64
import pickle


# https://github.com/JHUISI/charm/blob/dev/charm/adapters/abenc_adapt_hybrid.py
class AttributeCrypto:
    def __init__(self):
        self.group = PairingGroup('SS512')
        self.cpabe = CPabe_BSW07(self.group)
        self.hyb_abe = HybridABEnc(self.cpabe, self.group)
        self.pk, self.msk = self.hyb_abe.setup()
    
    def enc(self, msg, policy_string):
        cipher_text = self.hyb_abe.encrypt(self.pk, msg, policy_string)
        return objectToBytes(cipher_text, self.group)

    def dec(self, cipher_text, attributes):
        cipher_object = bytesToObject(cipher_text, self.group)
        sk = self.hyb_abe.keygen(self.pk, self.msk, attributes)
        decrypted_message = self.hyb_abe.decrypt(self.pk, sk, cipher_object)
        return decrypted_message


if __name__ == "__main__":
    att = AttributeCrypto()
    msg = b"hello world this is an important message."
    policy_string = '((police or insurance) and (emergency or investigating))'
    cipher_text = att.enc(msg, policy_string)
    attrs = ['INSURANCE', 'EMERGENCY']
    decrypted_message = att.dec(cipher_text, attrs)
