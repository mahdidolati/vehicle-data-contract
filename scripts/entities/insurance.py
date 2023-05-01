from scripts.constants import Const
from brownie import Contract
from time import time


class Insurance:
    def __init__(self, account):
        self.account = account
        self.crypto_atts = Const.attributes["insurance"]

    def read_ipfs(self, car, item_id):
        contract = Contract(car.contract.address)
        t1 = time()
        item_address = contract.get_data_adr.call(item_id)
        t2 = time()
        Const.logger.add_item("Case1", "GetAddrTime", t2 - t1)
        Const.logger.add_item("Case1", "GetAddrGas", self.account.gas_used)
        print(type(item_address), len(item_address))
        print("Item Address", item_address)
        t1 = time()
        cipher_text = Const.ipfs.retrieve(item_address)
        t2 = time()
        Const.logger.add_item("Case1", "IpfsReadTime", t2 - t1)
        t1 = time()
        r2 = Const.ttp.att_dec(cipher_text, self.crypto_atts)
        t2 = time()
        Const.logger.add_item("Case1", "DecTime", t2 - t1)
        print("INSURANCE", f"The data received from db is {r2}")
