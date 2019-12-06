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
node_url = "http://192.168.100.115:8545"
web3 = Web3(Web3.HTTPProvider(node_url))
web3.eth.defaultAccount = web3.eth.accounts[0]
#ABI for solidity contract code - change when sol is editted
abi = json.loads('[{"constant":false,"inputs":[{"internalType":"uint256","name":"k","type":"uint256"}],"name":"setLimit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getPower","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"t","type":"uint256"}],"name":"storeTemp","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getTemp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"p","type":"uint256"}],"name":"setPower","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getLimit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"temp","type":"uint256"}],"name":"overlimit","type":"event"}]')
#contract address
address = web3.toChecksumAddress("0x068fe0F8eDCB15100574b9E9fd8d8a6452BDEA49")
contract = web3.eth.contract(address=address, abi=abi)
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

print("Current Power Status is: ", contract.functions.getPower().call())

while True:
    try:
        time.sleep(1)
        print ("Power: ", contract.functions.getPower().call())
        print ("Current Temperature: ", contract.functions.getTemp().call())
        print ("Temperature Limit Set: ", contract.functions.getLimit().call())
    except KeyboardInterrupt:
        time.sleep(1)
        print ()
        print ("Power{ p1: on, p0: off} Limit{ l }")
        key = input()
        if key == 'p1':
            tx_hash = contract.functions.setPower(1).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)
        elif key == 'p0':
            tx_hash = contract.functions.setPower(0).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)
        else:
            print ("set limit: ")
            lim = int(input())
            tx_hash = contract.functions.setLimit(lim).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)