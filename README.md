# Environment:
```
Operating System: Ubuntu 22.04.1 LTS
Python: 3.7.16
eth_utils: '1.9.5'
web3: '5.31.3'
solcx: '1.1.1'
dotenv: '0.21.1'

```

## Prepare the environment
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
```

Download Ganache from `https://trufflesuite.com/ganache/` and install it with following commands:
```
chmod a+x ganache-2.7.0-linux-x86_64.AppImage
sudo add-apt-repository universe
sudo apt install libfuse2
./ganache-2.7.0-linux-x86_64.AppImage
```

# Run
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

# References:
[1] https://sesamedisk.com/smart-contracts-in-python-complete-guide/
