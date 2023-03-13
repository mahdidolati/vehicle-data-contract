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
        print("After encrypt:", cipher_text)
        for k in cipher_text:
            print(type(cipher_text[k]), cipher_text[k])
            if "pairing.Element" in str(type(cipher_text[k])):
                cipher_text[k] = self.group.serialize(cipher_text[k])
            elif type(cipher_text[k]) is integer:
                cipher_text[k] = int(cipher_text[k])
            elif type(cipher_text[k]) is dict:
                for kk in cipher_text[k]:      
                    print(type(cipher_text[k][kk]), cipher_text[k][kk])
                    if "pairing.Element" in str(type(cipher_text[k][kk])):
                        cipher_text[k][kk] = self.group.serialize(cipher_text[k][kk])
                    elif type(cipher_text[k][kk]) is integer:
                        cipher_text[k][kk] = int(cipher_text[k][kk])
                    elif type(cipher_text[k][kk]) is dict:
                        for kkk in cipher_text[k][kk]:
                            print(type(cipher_text[k][kk][kkk]), cipher_text[k][kk][kkk])
                            if "pairing.Element" in str(type(cipher_text[k][kk][kkk])):
                                cipher_text[k][kk][kkk] = self.group.serialize(cipher_text[k][kk][kkk])
                            elif type(cipher_text[k][kk][kkk]) is integer:
                                cipher_text[k][kk][kkk] = int(cipher_text[k][kk][kkk])    
        # return objectToBytes(cipher_text, self.group)
        print("After serialization: ", cipher_text)
        pickled = pickle.dumps(cipher_text)
        print("After pickled: ", pickled)
        return pickled


    def dec(self, cipher_text, attributes):
        cipher_object = pickle.loads(cipher_text)
        print("After Pickle load:", cipher_object)
        for k in cipher_object:
            print("1", type(cipher_object[k]), cipher_object[k])
            if type(cipher_object[k]) is bytes:
                cipher_object[k] = self.group.deserialize(cipher_object[k])
                print("1 done")
            # elif type(cipher_object[k]) is str:
            #    cipher_object[k] = pickle.loads(cipher_object[k])
            if type(cipher_object[k]) is dict:
                for kk in cipher_object[k]:      
                    print("2", type(cipher_object[k][kk]), cipher_object[k][kk])
                    if type(cipher_object[k][kk]) is bytes:
                        print("2 b start")
                        cipher_object[k][kk] = self.group.deserialize(cipher_object[k][kk])
                        print("2 b done")
                    # elif type(cipher_object[k][kk]) is int:
                    #     print("2 i start")
                    #     cipher_object[k][kk] = integer(cipher_object[k][kk])
                    #     print("2 i done")
                    # elif type(cipher_object[k][kk]) is str and cipher_object[k][kk][0] in ['{', '[']:
                    #     print("2 s start")
                    #     cipher_object[k][kk] = eval(cipher_object[k][kk])
                    #     print("2 s done")
                    if type(cipher_object[k][kk]) is dict:
                        for kkk in cipher_object[k][kk]:
                            print("3", type(cipher_object[k][kk][kkk]), cipher_object[k][kk][kkk])
                            if type(cipher_object[k][kk][kkk]) is bytes:
                                print("3 b start")
                                cipher_object[k][kk][kkk] = self.group.deserialize(cipher_object[k][kk][kkk]) 
                                print("3 b done")
                            # elif type(cipher_object[k][kk][kkk]) is int:
                            #     print("3 i start")
                            #     cipher_object[k][kk][kkk] = integer(cipher_object[k][kk][kkk]) 
                            #     print("3 i done")
                            # elif type(cipher_object[k][kk][kkk]) is str and cipher_object[k][kk][kkk][0] in ['{', '[']:
                            #     print("3 s start")
                            #     cipher_object[k][kk][kkk] = eval(cipher_object[k][kk][kkk])
                            #     print("3 s done")
        print("----", cipher_object)
        sk = self.hyb_abe.keygen(self.pk, self.msk, attributes)
        decrypted_message = self.hyb_abe.decrypt(self.pk, sk, cipher_object)
        print(decrypted_message)
        return decrypted_message


if __name__ == "__main__":
    att = AttributeCrypto()
    msg = b"hello world this is an important message."
    policy_string = '((police or insurance) and (emergency or investigating))'
    cipher_text = att.enc(msg, policy_string)
    attrs = ['INSURANCE', 'EMERGENCY']
    decrypted_message = att.dec(cipher_text, attrs)
