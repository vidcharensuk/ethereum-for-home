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

node_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(node_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant":false,"inputs":[{"internalType":"bool","name":"value","type":"bool"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"get","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"}]')

#contract address
address = web3.toChecksumAddress("0xde4936DD510115B8B583C039858ABce8f76Dc531")

contract = web3.eth.contract(address=address, abi=abi)  

print("Current Switch Status is: ", contract.functions.getSwitch().call)

while True:
    print("1: Turn On, 2: Turn Off")
    on = input()
    contract.functions.setSwitch(on).transact
    web3.eth.waitForTransactionReceipt(tx_hash)
    print("Done")
    print("Currently: ", on)
