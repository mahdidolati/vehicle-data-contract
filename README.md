# Identity-Based & Attribute-Based Cryptography for Data Sharing in Vehicular Networks via Blockchain

## About
This repository hosts the open-source implementation of our research paper “Blockchain-Based User-Centric Privacy-Preserving Framework for Vehicular Data Sharing and Monetization,” published in Elsevier’s Computers & Electrical Engineering journal. [Link to article.](https://www.sciencedirect.com/science/article/abs/pii/S0045790626000017?via%3Dihub)

```
@article{HOSSEIN2026110933,
  title = {Blockchain-based user-centric privacy-preserving framework for vehicular data sharing and monetization},
  journal = {Computers and Electrical Engineering},
  volume = {132},
  pages = {110933},
  year = {2026},
  issn = {0045-7906},
  doi = {https://doi.org/10.1016/j.compeleceng.2026.110933},
  url = {https://www.sciencedirect.com/science/article/pii/S0045790626000017},
  author = {Koosha Mohammad Hossein and Negar Rezaei and Ahmad Khonsari and Mahdi Dolati and Tooska Dargahi and Meisam Babaie}
}
```

## Environment:
```
Operating System: Ubuntu 22.04.1 LTS
Python: 3.7.16
eth_utils: '1.9.5'
web3: '5.31.3'
solcx: '1.1.1'
dotenv: '0.21.1'

```

### Prepare the environment
```
sudo apt update
sudo apt install python3.7
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2
sudo update-alternatives --config python3
sudo apt install python3.7-dev
sudo apt install python3.7-distutils
sudo apt install python3-apt
sudo apt install python3-pip
sudo apt install virtualenv
virtualenv --python=python3.7 contract37
pip install web3
pip install py-solc-x
pip install eth-utils
pip install python-dotenv
pip install eth-brownie  
sudo apt install nodejs
sudo apt install npm
npm install -g ganache-cli 
ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie
brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=5777 
brownie networks add Development ganache-local host=http://127.0.0.1:8545 chainid=5777 accounts=10 default_balance="100 ether"
brownie run scripts/deploy_interact.py
##
brownie networks add Ethereum glocal host=http://127.0.0.1:7545 chainid=5777
sudo ganache-cli --port 7545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie --networkId glocal
brownie run scripts/deploy_interact.py --network glocal
rm -rf build
```

Download Ganache from `https://trufflesuite.com/ganache/` and install it with following commands:
```
chmod a+x ganache-2.7.0-linux-x86_64.AppImage
sudo add-apt-repository universe
sudo apt install libfuse2
./ganache-2.7.0-linux-x86_64.AppImage
```

### Upgrade to use conda

conda install 3.8.5
conda create --name environment_name python=3.8.5
conda activate environment_name    # to activate it 
conda deactivate                   # to deactivate it 
conda remove -n environment_name   # to remove it
conda install -n environment_name [package] # install package in it



## Run
```
source contract37/bin/activate
```

Run the blockchain with the following command:
```
./ganache-2.7.0-linux-x86_64.AppImage 
```

Run the program with the following command:
```
python3 main.py
```

## References:
[1] https://sesamedisk.com/smart-contracts-in-python-complete-guide/
[2] https://chainstack.com/the-brownie-tutorial-series-part-1/
