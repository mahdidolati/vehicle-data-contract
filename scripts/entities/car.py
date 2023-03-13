from scripts.constants import Const
from brownie import VehicleContract
from time import time


class Car:
    def __init__(self, account):
        self.account = account
        self.contract = None
        self.location = []
        self.location_address = []
        self.location_map = {}

    def deploy(self, price_feed_address):
        self.contract = VehicleContract.deploy(price_feed_address, { "from" : self.account })
        # print(f"Contract deployed at {self.contract}")
        # print(f"{self.account.address} used {self.account.gas_used}")    

    def review(self):
        addrs, strs = self.contract.getRequests.call()
        for i in range(len(addrs)):
            print("CAR", "New Request", addrs[i], "for", strs[i])
            tx_receipt = self.contract.grantAccess(i, {
                "from" : self.account
            })
            tx_receipt.wait(1)
            print("CAR", f"{self.account.address} used {self.account.gas_used}")
            data_val = bytes(self.location_map[strs[i]], "utf-8")
            data_val = Const.ttp.id_enc(data_val, addrs[i])
            Const.db.save(strs[i] + "_i", data_val)

    def use(self):
        if len(self.location) == 0:
            self.location.append(1)
        else:
            self.location.append((self.location[-1] + 1) % 20)
        self.location_address.append("location" + str(time()))

        data_adr = self.location_address[-1]
        data_val = Const.ttp.att_enc(str(self.location[-1]), "police or insurance")
        self.location_map[data_adr] = str(self.location[-1])
        Const.db.save(data_adr, data_val)        
        
    def read(self):
        print("CAR", f"ETH price is: {self.contract.getEthPrice.call()}")
        print("CAR", f"{self.account.address} used {self.account.gas_used} has {self.account.balance()}")
