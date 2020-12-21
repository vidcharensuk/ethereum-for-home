#author = "Vid Charensuk"
#license = "GPLv3"
#version = "0.1"
#maintainer = "Vid Charensuk"
#email = "saravidsuchaad@gmail.com"
#status = "Development"

import json
from web3 import Web3
import time
import datetime
from web3.middleware import geth_poa_middleware

#shows status of hardware led. Will be replaced by gpio on actual device
ledOn = False

#Initialization connection to ethereum node
node_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(node_url))
web3.eth.defaultAccount = web3.eth.accounts[0]
#ABI for solidity contract code - change when sol is editted
abi = json.loads('[{"inputs":[],"name":"getSwitch","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"value","type":"bool"}],"name":"setSwitch","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
#contract address
address = web3.toChecksumAddress("0x6b8589Ceffd1c766bbB6D8182DA06ADcb1039546")
contract = web3.eth.contract(address=address, abi=abi)
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

while True:
    time.sleep(1)
    k = contract.functions.getSwitch().call()
    print ("getSwitch: ",datetime.datetime.now(), k)
    if (ledOn != k):
        ledOn = k
    print("LED:", ledOn)