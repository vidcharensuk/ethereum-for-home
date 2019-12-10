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
node_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(node_url))
web3.eth.defaultAccount = web3.eth.accounts[0]
#ABI for solidity contract code - change when sol is editted
abi = json.loads('[{"constant":false,"inputs":[{"internalType":"uint256","name":"k","type":"uint256"}],"name":"setDoorStat","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getDoorStat","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"k","type":"uint256"}],"name":"setUidSwitch","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getUidSwitch","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
#contract address
address = web3.toChecksumAddress("0xde4936DD510115B8B583C039858ABce8f76Dc531")
contract = web3.eth.contract(address=address, abi=abi)
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

while True:
    time.sleep(1)
    contract.functions.getUidSwitch().call()
    print("1: Lock/Unlock")
    on = input()
    if (on == 1):
            tx_hash = contract.functions.setUidSwitch(1).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)
            print("Done")
