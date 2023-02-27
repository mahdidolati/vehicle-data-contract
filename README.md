
Environment:
```
Operating System: Ubuntu 22.04.1 LTS
Python: 3.10.6
```

Prepare the environment
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
