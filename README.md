# Environment:
```
Operating System: Ubuntu 22.04.1 LTS
Python: 3.7.16
```

## Prepare the environment
```
sudo apt update
sudo apt install python3.7
sudo apt install python3.7-dev python3.7-distutils python3-apt
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
sudo update-alternatives --config python3
sudo apt install python3-pip
sudo apt install virtualenv
virtualenv --python=python3.7 brw
git clone git@github.com:JHUISI/charm.git
cd charm
sudo ./configure.sh
make
sudo make test
sudo make install
source brw/bin/activate
pip install eth-brownie  
sudo apt install nodejs npm
npm install -g ganache-cli 
brownie networks add Ethereum glocal host=http://127.0.0.1:7545 chainid=5777
sudo ganache-cli --port 7545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie --networkId glocal
```

```
sudo apt install sqlite3 
sudo apt install ./dbeaver-ce_23.0.0_amd64.deb
sqlite3 database.db
sqlite> CREATE TABLE vehicleData(DATA_ADR text NOT NULL, DATA_VAL text NOT NULL);
sqlite> CREATE TABLE vehicle_data(DATA_ADR text NOT NULL, DATA_VAL BLOB NOT NULL);
```

# Run
```
source brw/bin/activate
rm -rf build; brownie run scripts/main.py --network glocal
```

# References:
[1] https://sesamedisk.com/smart-contracts-in-python-complete-guide/

[2] https://chainstack.com/the-brownie-tutorial-series-part-1/

[3] https://ethereum.stackexchange.com/questions/110979/deploying-smartcontract-to-ganache-desktop-instead-of-ganache-cli-with-brownie

[4] https://ethereum.stackexchange.com/questions/122096/how-to-clean-or-reset-brownie-build-folder

[5] https://eth-brownie.readthedocs.io/en/stable/network-management.html

[6] https://github.com/smartcontractkit/full-blockchain-solidity-course-py/blob/main/README.md

[7] https://stackoverflow.com/questions/43251642/how-to-serialize-store-the-ciphertext-encrypted-by-hybrid-cpabe-bsw07-in-charm

