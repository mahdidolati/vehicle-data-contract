from eth_utils import address
from web3 import Web3
import os
from solcx import compile_standard, install_solc
from dotenv import load_dotenv
import json


install_solc('0.6.0')

with open("./SimpleStorageContract.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {
                "SimpleStorageContract.sol": {
                    "content": simple_storage_file
                }
            },
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": [
                            "abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"
                        ]
                    }
                }
            },
        },
        solc_version="0.6.0",
    )

    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)
        print("Done!")

        bytecode = compiled_sol["contracts"]["SimpleStorageContract.sol"]\
        ["SimpleStorage"]["evm"]["bytecode"]["object"]
        print("---\n", type(bytecode), bytecode)

        abi = json.loads(
            compiled_sol["contracts"]["SimpleStorageContract.sol"]\
            ["SimpleStorage"]["metadata"]
        )["output"]["abi"]
        print("---\n", type(abi), abi)

        w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
        chain_id = 1337
        my_address = "0x7B33E899ec188307D642C25b9943e653F041671d"
        private_key = "0x9a21149c3c4fba20f2c7d860ff76f6718aacb2d1682a18c170d73ddbd5d87d1f"

        SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
        nonce = w3.eth.getTransactionCount(my_address)
        transaction = SimpleStorage.constructor().buildTransaction({
            "chainId": chain_id,
            "from": my_address,
            "nonce": nonce
        })
        signed_tx = w3.eth.account.sign_transaction(transaction, private_key=private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(type(tx_receipt), tx_receipt)
        print("Done!")