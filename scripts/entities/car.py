from scripts.constants import Const
from brownie import VehicleContract
from time import time


class Car:
    def __init__(self, account):
        self.account = account
        self.contract = None
        self.location = []
        self.location_address = []
        self.location_id = []
        self.location_map = {}
        self.location_id_map = {}

    def deploy(self, price_feed_address):
        t1 = time()
        self.contract = VehicleContract.deploy(price_feed_address, { "from" : self.account })
        t2 = time()
        Const.logger.add_item("deploy", t2 - t1)
        Const.logger.add_item("car_gas", self.account.gas_used)
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

    def review_ipfs(self):
        addrs, strs = self.contract.getRequests.call()
        Const.logger.add_item("car_gas", self.account.gas_used)
        for i in range(len(addrs)):
            data_id = strs[i]
            print("CAR", "New Request", addrs[i], "for", data_id)
            data_val = bytes(self.location_id_map[data_id], "utf-8")
            t1 = time()
            data_val = Const.ttp.id_enc(data_val, addrs[i])
            t2 = time()
            Const.logger.add_item("id_enc", t2 - t1)
            t1 = time()
            data_adr = Const.ipfs.save(data_val)
            t2 = time()
            Const.logger.add_item("ipfs_save_id", t2 - t1)
            t1 = time()
            tx_receipt = self.contract.add_data_adr(data_id + "_i", data_adr, {
                "from" : self.account
            })
            tx_receipt.wait(1)
            t2 = time()
            Const.logger.add_item("add_adr_id", t2 - t1)
            Const.logger.add_item("car_gas", self.account.gas_used)

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

    def use_ipfs(self):
        if len(self.location) == 0:
            self.location.append(1)
        else:
            self.location.append((self.location[-1] + 1) % 20)
        data_id = "location" + str(time())        
        t1 = time()
        data_val = Const.ttp.att_enc(str(self.location[-1]), "police or insurance")
        t2 = time()
        Const.logger.add_item("att_enc", t2 - t1)
        t1 = time()
        data_adr = Const.ipfs.save(data_val)
        t2 = time()
        Const.logger.add_item("ipfs_save_att", t2 - t1)
        print("Saved into IPFS. Hash is: {}".format(data_adr))
        self.location_map[data_adr] = str(self.location[-1])
        self.location_id_map[data_id] = str(self.location[-1])
        self.location_address.append(data_adr)
        t1 = time()
        tx_receipt = self.contract.add_data_adr(data_id, data_adr, {
            "from" : self.account
        })
        tx_receipt.wait(1)
        t2 = time()
        Const.logger.add_item("add_adr_att", t2 - t1)
        Const.logger.add_item("car_gas", self.account.gas_used)
        self.location_id.append(data_id)
        
    def read(self):
        print("CAR", f"ETH price is: {self.contract.getEthPrice.call()}")
        print("CAR", f"{self.account.address} used {self.account.gas_used} has {self.account.balance()}")
