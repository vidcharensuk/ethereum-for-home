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

#Initialization connection to ethereum node
node_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(node_url))
web3.eth.defaultAccount = web3.eth.accounts[0]
#ABI for solidity contract code - change when sol is editted
abi = json.loads('[{"constant":true,"inputs":[],"name":"getSwitch","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bool","name":"value","type":"bool"}],"name":"setSwitch","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
#contract address
address = web3.toChecksumAddress("0x3C8Ec2A37CB4fFC7aC2E48a240Ca71A4220e93d9")
contract = web3.eth.contract(address=address, abi=abi)
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

print("Current Switch Status is: ", contract.functions.getSwitch().call())

while True:
    print("1: Turn On, 2: Turn Off")
    on = input()
    if on == '1':
        switch = True
    else:
        switch = False
    tx_hash = contract.functions.setSwitch(switch).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    print("Done")
    print("Currently: ", switch)
