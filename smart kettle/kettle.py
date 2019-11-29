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

#shows status of hardware led. Will be replaced by gpio on actual device
ledOn = False

node_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(node_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant":false,"inputs":[{"internalType":"uint256","name":"k","type":"uint256"}],"name":"setLimit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getPower","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"t","type":"uint256"}],"name":"storeTemp","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"p","type":"uint256"}],"name":"setPower","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"temp","type":"uint256"}],"name":"overlimit","type":"event"}]')

#contract address
address = web3.toChecksumAddress("0xde4936DD510115B8B583C039858ABce8f76Dc531")

contract = web3.eth.contract(address=address, abi=abi)  


