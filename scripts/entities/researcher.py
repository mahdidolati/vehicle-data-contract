from scripts.constants import Const
from brownie import Contract
from time import time


class Researcher:
    def __init__(self, account):
        self.account = account

    def read(self, car, item_address):
        cipher_text = Const.db.retrieve(self, car, item_address)
        r2 = Const.ttp.id_dec(cipher_text, self.account.address)
        print("RESEARCHER", f"The data received from db is {r2}")
    
    def read_ipfs(self, car, item_id):
        contract = Contract(car.contract.address)
        t1 = time()
        item_address = contract.get_data_adr.call(item_id)
        t2 = time()
        Const.logger.add_item("get_adr_id", t2 - t1)
        Const.logger.add_item("researcher_gas", self.account.gas_used)
        print(type(item_address), len(item_address))
        print("Item Address", item_address)
        t1 = time()
        cipher_text = Const.ipfs.retrieve(item_address)
        t2 = time()
        Const.logger.add_item("ipfs_read_id", t2 - t1)
        t1 = time()
        r2 = Const.ttp.id_dec(cipher_text, self.account.address)
        t2 = time()
        Const.logger.add_item("id_dec", t2 - t1)
        print("RESEARCHER", f"The data received from db is {r2}")

    def request(self, car, item_id):
        contract = Contract(car.contract.address)
        t1 = time()
        tx_receipt = contract.requestAccess(item_id, {
            "from": self.account
        })
        tx_receipt.wait(1)
        t2 = time()
        Const.logger.add_item("request", t2 - t1)
        Const.logger.add_item("researcher_gas", self.account.gas_used)
        print("RESEARCHER", f"{self.account.address} used {self.account.gas_used}")

    def request_and_pay(self, car, item_id):
        contract = Contract(car.contract.address)
        fee = contract.getFee.call()
        Const.logger.add_item("researcher_gas", self.account.gas_used)
        print("RESEARCHER", f"Fee of accessing data is: {fee}")
        tx_receipt = contract.requestAccessPay(item_id, {
            "from": self.account,
            "value": fee
        })
        tx_receipt.wait(1)
        Const.logger.add_item("researcher_gas", self.account.gas_used)
        print("RESEARCHER", f"{self.account.address} used {self.account.gas_used}")

    def deposit(self, car):
        contract = Contract(car.contract.address)
        fee = contract.getFee.call()
        print("RESEARCHER", f"Fee of accessing data is: {fee}")
        tx_receipt = contract.deposit({    
            "from": self.account,
            "value": fee
        })
        tx_receipt.wait(1)
        print("RESEARCHER", f"{self.account.address} used {self.account.gas_used}")   
