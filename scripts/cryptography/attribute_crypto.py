import subprocess
import pickle
from time import time, sleep
import os


class AttributeCrypto:
    def __init__(self):
        self.prefix_root = "./scripts/cryptography/att/"
        self.prefix_crypto = "./att/"
        rm_cmd = "rm" + " " + self.prefix_root + "ttp_*"
        subprocess.run([rm_cmd,], shell=True)
        cpabe_cmd = "cpabe-setup"
        self.ttp_public = "ttp_public"
        self.ttp_master = "ttp_master"
        subprocess.run([cpabe_cmd, "-p", self.prefix_root + self.ttp_public, "-m", self.prefix_root + self.ttp_master])
        self.users = dict()

    def enc(self, msg, policy):
        enc_cmd = "cpabe-enc"
        in_file = "ttp_msg_" + str(time())
        out_file = in_file + ".cpabe"
        f = open(self.prefix_root + in_file, "+w")
        f.write(msg)
        f.flush()
        f.close()
        while(os.path.isfile(self.prefix_root + in_file) == False):
            sleep(0.001)
        enc_cmd_c = enc_cmd + " " + self.prefix_root + self.ttp_public + " " \
                        + self.prefix_root + in_file + \
                        " -k -o " + self.prefix_root + out_file + \
                        " '" + policy + "'"
        # print(enc_cmd_c)
        proc = subprocess.Popen([enc_cmd_c,], shell=True)
        # print("the commandline is {}".format(proc.args))
        # print(str(proc.communicate()))
        while(os.path.isfile(self.prefix_root + out_file) == False):
            sleep(0.001)
        # print(self.prefix_root + out_file)
        f = open(self.prefix_root + out_file, "rb")
        cipher_text = f.read()
        f.close()
        subprocess.run(["rm " + self.prefix_root + in_file + " " \
                                + self.prefix_root + out_file,], shell=True)
        return cipher_text

    def dec(self, cipher_text, attributes):
        pk_file = "ttp_pk_" + str(time())
        pk_cmd = "cpabe-keygen -o " + self.prefix_root + pk_file + " " \
                    + self.prefix_root + self.ttp_public + " " \
                    + self.prefix_root + self.ttp_master + " " \
                    + attributes
        print("==>", pk_cmd)
        subprocess.run([pk_cmd,], shell=True)
        
        while(os.path.isfile(self.prefix_root + pk_file) == False):
            sleep(0.001)
        cipher_file = "ttp_cipher_" + str(time())
        dec_file = cipher_file + "_dec"
        f = open(self.prefix_root + cipher_file, "wb")
        f.write(cipher_text)
        f.flush()
        f.close()

        dec_cmd = "cpabe-dec -k " + self.prefix_root + self.ttp_public + " " \
                    + self.prefix_root + pk_file + " " \
                    + self.prefix_root + cipher_file + " " \
                    + "-o " + self.prefix_root + dec_file
        print(dec_cmd)
        out_msg = subprocess.Popen([dec_cmd,], shell=True, stdout=subprocess.PIPE)
        
        while True:
            out_msg2 = str(out_msg.communicate())
            if not out_msg2.startswith("b"):
                print(out_msg2)
            if os.path.isfile(self.prefix_root + dec_file) or out_msg2.startswith("cannot"):
                sleep(1)
                break

        decrypted_msg = None
        print(out_msg2)
        if not out_msg2.startswith("cannot"):
            f = open(self.prefix_root + dec_file, "r")
            decrypted_msg = f.read()
            f.close()

        subprocess.run(["rm " + self.prefix_root + pk_file + " " \
                                + self.prefix_root + cipher_file + " " \
                                + self.prefix_root + dec_file,], shell=True)
        return decrypted_msg
