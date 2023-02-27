
# Environment:
```
Operating System: Ubuntu 22.04.1 LTS
Python: 3.10.6
eth_utils: '1.9.5'
web3: '5.31.3'
solcx: '1.1.1'
dotenv: '1.0.0'

```

## Prepare the environment
```
sudo apt update
sudo apt install python3-pip
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
Run the blockchain with the following command:
```
./ganache-2.7.0-linux-x86_64.AppImage 
```

Run the program with the following command:
```
python3 main.py
```
