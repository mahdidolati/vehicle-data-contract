from scripts.constants import Const
from brownie import Contract
from time import time


class Researcher:
    def __init__(self, account):
        self.account = account
    
    def read_ipfs(self, car, item_id):
        contract = Contract(car.contract.address)
        g1 = self.account.gas_used
        t1 = time()
        item_address = contract.get_data_adr.call(item_id)
        t2 = time()
        g2 = self.account.gas_used
        Const.logger.add_item("Case2", "GetAddrTime", t2 - t1)
        Const.logger.add_item("Case2", "GetAddrGas", g2 - g1)
        print(type(item_address), len(item_address))
        print("Item Address", item_address)
        t1 = time()
        cipher_text = Const.ipfs.retrieve(item_address)
        t2 = time()
        Const.logger.add_item("Case2", "IpfsReadTime", t2 - t1)
        t1 = time()
        r2 = Const.ttp.id_dec(cipher_text, self.account.address)
        t2 = time()
        Const.logger.add_item("Case2", "DecTime", t2 - t1)
        print("RESEARCHER", f"The data received from db is {r2}")

    def request_and_pay(self, car, item_id):
        contract = Contract(car.contract.address)
        g1 = self.account.gas_used
        t1 = time()
        fee = contract.getFee.call()
        t2 = time()
        g2 = self.account.gas_used
        Const.logger.add_item("Case2", "GetFeeTime", t2 - t1)
        Const.logger.add_item("Case2", "GetFeeGas", g2 - g1)
        print("RESEARCHER", f"Fee of accessing data is: {fee}")
        g1 = self.account.gas_used
        t1 = time()
        tx_receipt = contract.requestAccessPay(item_id, {
            "from": self.account,
            "value": fee
        })
        tx_receipt.wait(1)
        t2 = time()
        g2 = self.account.gas_used
        Const.logger.add_item("Case2", "RequestTime", t2 - t1)
        Const.logger.add_item("Case2", "RequestGas", g2 - g1)
        print("RESEARCHER", f"{self.account.address} used {self.account.gas_used}")
