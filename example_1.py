from charm.core.math.integer import integer
from charm.schemes.chamhash_adm05 import ChamHash_Adm05


p = integer(141660875619984104245410764464185421040193281776686085728248762539241852738181649330509191671665849071206347515263344232662465937366909502530516774705282764748558934610432918614104329009095808618770549804432868118610669336907161081169097403439689930233383598055540343198389409225338204714777812724565461351567)
q = integer(70830437809992052122705382232092710520096640888343042864124381269620926369090824665254595835832924535603173757631672116331232968683454751265258387352641382374279467305216459307052164504547904309385274902216434059305334668453580540584548701719844965116691799027770171599194704612669102357388906362282730675783)
chamHash = ChamHash_Adm05(p, q)
(public_key, secret_key) = chamHash.paramgen()
msg = "hello world this is the message"
c = chamHash.hash(public_key, msg)
print(c == chamHash.hash(public_key, msg, c[1], c[2]))


# https://github.com/JHUISI/charm/blob/acb55513b244bfdebbfe715cec7b564c8e850779/charm/schemes/pre_mg07.py
from charm.schemes.pre_mg07 import PreGA
from charm.toolbox.pairinggroup import PairingGroup,pc_element  
ID = "nikos fotiou"
ID2 = "test user"
msg = "hello world!!!!!"
group = PairingGroup('SS512', secparam=1024)  
pre = PreGA(group)
(master_secret_key, params) = pre.setup()
id_secret_key = pre.keyGen(master_secret_key, ID)
id2_secret_key = pre.keyGen(master_secret_key, ID2)
ciphertext = pre.encrypt(params, ID, msg);
pre.decryptFirstLevel(params,id_secret_key, ciphertext, ID)
re_encryption_key = pre.rkGen(params,id_secret_key, ID, ID2)
ciphertext2 = pre.reEncrypt(params, ID, re_encryption_key, ciphertext)
pre.decryptSecondLevel(params,id2_secret_key,ID, ID2, ciphertext2)

# https://github.com/JHUISI/charm/blob/acb55513b244bfdebbfe715cec7b564c8e850779/charm/schemes/ibenc/ibenc_waters05.py
from charm.schemes.ibenc.ibenc_waters05 import IBE_N04
from charm.toolbox.pairinggroup import PairingGroup,GT
from charm.toolbox.hash_module import Waters
group = PairingGroup('SS512')
waters_hash = Waters(group)
ibe = IBE_N04(group)
(master_public_key, master_key) = ibe.setup()
ID = "bob@mail.com"
kID = waters_hash.hash(ID)
secret_key = ibe.extract(master_key, kID)
msg = group.random(GT)
cipher_text = ibe.encrypt(master_public_key, kID, msg)
decrypted_msg = ibe.decrypt(master_public_key, secret_key, cipher_text)
decrypted_msg == msg