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

node_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(node_url))
web3.eth.defaultAccount = web3.eth.accounts[0]

#ABI for solidity contract code - change when sol is editted
abi = json.loads('[{"inputs":[],"name":"getSwitch","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"value","type":"bool"}],"name":"setSwitch","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
bytecode = "608060405234801561001057600080fd5b5060ea8061001f6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c80636fb7575c14603757806397cefc4c146055575b600080fd5b603d6082565b60405180821515815260200191505060405180910390f35b608060048036036020811015606957600080fd5b810190808035151590602001909291905050506098565b005b60008060009054906101000a900460ff16905090565b806000806101000a81548160ff0219169083151502179055505056fea26469706673582212209e7452078991d0d808bbdfcb042b2067a1a9c2fbd5b8caa5065a3675849201db64736f6c63430007060033"
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

Switch = web3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Switch.constructor().transact()

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
#save addr to a file"
file1 = open("contract_addr_hist.txt","a") 
print(tx_receipt.contractAddress)
file1.write("\n")
Current_time = str(datetime.datetime.now())
file1.write(Current_time)
file1.write("    ")
file1.write(tx_receipt.contractAddress)
file1.close()
