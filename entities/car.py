from eth_utils import address
from web3 import Web3
import os
from solcx import compile_standard
from dotenv import load_dotenv
import json
from entities.contract_api import get_compiled_contract
from constants import Const


class Car:
    def __init__(self, c_id):
        self.id = c_id
        self.address = "0xEBf52D1635488ebdec786350caC943FcD4aa8395"
        self.private_key = "0xfe5121b16d09c5d3ae2745cfbc57082c33efdbc3a2daaf0e8984810d2e7af6e0"
        self.contract = None
        self.contract_address = None
        self.nonce = 0
        self.location = [0]
        self.speed = [0]
        self.milage = 0

    def get_nonce(self):
        n = self.nonce
        self.nonce = self.nonce + 1
        return n

    def init(self, contract_path, contract_name):
        bytecode, abi = get_compiled_contract(contract_path, contract_name)
        SimpleStorage = Const.w3.eth.contract(abi=abi, bytecode=bytecode)
        self.nonce = Const.w3.eth.getTransactionCount(self.address)
        transaction = SimpleStorage.constructor().buildTransaction({
            "chainId": Const.chain_id,
            "from": self.address,
            "nonce": self.get_nonce()
        })
        signed_tx = Const.w3.eth.account.sign_transaction(transaction, private_key=self.private_key)
        tx_hash = Const.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = Const.w3.eth.wait_for_transaction_receipt(tx_hash)
        
        self.contract_address = tx_receipt.contractAddress
        self.contract = Const.w3.eth.contract(
            abi=abi,
            address=self.contract_address
        )

    def use(self):
        # collect data from sensors
        self.location.append((self.location[-1] + 1) % 20)
        self.speed.append((self.speed[-1] + 1) % 100)
        self.milage = self.milage + 1

        # send to the blockchain
        call_fun = self.contract.functions.store(self.milage).buildTransaction({
            "chainId": Const.chain_id,
            "from": self.address,
            "nonce": self.get_nonce()
        })
        sign_call_fun = Const.w3.eth.account.sign_transaction(call_fun, private_key=self.private_key)
        tx_call_fun_hash = Const.w3.eth.send_raw_transaction(sign_call_fun.rawTransaction)
        tx_call_fun_receipt = Const.w3.eth.wait_for_transaction_receipt(tx_call_fun_hash)

    def read(self):
        print(self.contract.functions.retrieve().call())
