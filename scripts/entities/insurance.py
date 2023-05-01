from scripts.constants import Const
from brownie import Contract
from time import time


class Insurance:
    def __init__(self, account):
        self.account = account
        self.crypto_atts = ["INSURANCE", "INSPECTING", "INTERNATIONAL", "PUBLIC",]

    def read(self, car, item_address):
        cipher_text = Const.db.retrieve(self, car, item_address)
        r2 = Const.ttp.att_dec(cipher_text, self.crypto_atts)
        print("INSURANCE", f"The data received from db is {r2}")

    def read_ipfs(self, car, item_id):
        contract = Contract(car.contract.address)
        t1 = time()
        item_address = contract.get_data_adr.call(item_id)
        t2 = time()
        Const.logger.add_item("get_adr_att", t2 - t1)
        Const.logger.add_item("insurance_gas", self.account.gas_used)
        print(type(item_address), len(item_address))
        print("Item Address", item_address)
        t1 = time()
        cipher_text = Const.ipfs.retrieve(item_address)
        t2 = time()
        Const.logger.add_item("ipfs_read_att", t2 - t1)
        t1 = time()
        r2 = Const.ttp.att_dec(cipher_text, self.crypto_atts)
        t2 = time()
        Const.logger.add_item("att_dec", t2 - t1)
        print("INSURANCE", f"The data received from db is {r2}")

    def deposit(self, car):
        contract = Contract(car.contract.address)
        fee = contract.getFee.call()
        print("INSURANCE", f"Fee of accessing data is: {fee}")
        tx_receipt = contract.deposit({    
            "from": self.account,
            "value": fee
        })
        tx_receipt.wait(1)
        print("INSURANCE", f"{self.account.address} used {self.account.gas_used}")   
