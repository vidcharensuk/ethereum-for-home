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

#shows status of hardware sensor and LED. Will be replaced by gpio on actual device.
#Servo Motor position. 0 = unlock, 1 = lock; Button. 1 = pressed; LED. 1 = on, 0 = off;
motor = 0
button = 0
LED = 0

#Init Variable
buttonSW = 0

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

def runMotor():
    if (motor == 0):
        motor = 1
    else:
        motor = 0

def getDoorStat():
    if (motor == 1):
        print ("Door Locked!")
    else:
        print ("Door Unlocked!")

def setDoorStat():
    if (motor ==1):
        contract.functions.setDoorstat(1).transact()
    else :
        contract.functions.setDoorStat(0).transact()

while True:
    time.sleep(1)
    getDoorStat()
    if (button == 1 or buttonSW == 1):
        buttonSW = 0
        runMotor()
    setDoorStat()
    if (contract.functions.getUidSwitch().call()):
        buttonSW = 1
        contract.functions.setUidSwitch(False).transact()