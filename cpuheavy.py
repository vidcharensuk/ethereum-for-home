#version 0.2
import json
from web3 import Web3
import time
import datetime

node_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(node_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant":false,"inputs":[{"internalType":"uint256[]","name":"arr","type":"uint256[]"},{"internalType":"uint256","name":"left","type":"uint256"},{"internalType":"uint256","name":"right","type":"uint256"}],"name":"quickSort","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"size","type":"uint256"},{"internalType":"uint256","name":"signature","type":"uint256"}],"name":"sort","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"size","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"signature","type":"uint256"}],"name":"finish","type":"event"}]')

#contract address
address = web3.toChecksumAddress("0xf072eDdB87D3a6Db66e8b739f38A70a2a8618C4b")

contract = web3.eth.contract(address=address, abi=abi)  

tx_hash = contract.functions.sort(100,2).transact()
print('start')
receipt = web3.eth.getTransactionReceipt(tx_hash)

print(contract.events.finish().processReceipt(receipt))

def handle_event(event):
    print(event)

#while True:
#   print("New entries: ", len(event_filter.get_new_entries()))
#   for event in event_filter.get_new_entries():
#       handle_event(event)
#   print("Get Hash:", contract.functions.getHash().call())
#   time.sleep(poll_interval)

def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)




#contract.events.myEvent().processReceipt(receipt)
