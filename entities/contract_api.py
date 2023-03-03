from eth_utils import address
from web3 import Web3
import os
from solcx import compile_standard
from dotenv import load_dotenv
import json
from constants import Const


def get_compiled_contract(contract_path, contract_name):
    file = open("{}{}".format(contract_path, contract_name), "r")
    simple_storage_file = file.read()

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {
                contract_name: {
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

    file = open("compiled_code.json", "w")
    json.dump(compiled_sol, file)

    bytecode = compiled_sol["contracts"]["SimpleStorageContract.sol"]\
    ["SimpleStorage"]["evm"]["bytecode"]["object"]

    abi = json.loads(
        compiled_sol["contracts"]["SimpleStorageContract.sol"]\
        ["SimpleStorage"]["metadata"]
    )["output"]["abi"]

    return bytecode, abi