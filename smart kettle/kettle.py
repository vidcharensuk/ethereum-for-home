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

#shows status of hardware sensor and LED. Will be replaced by gpio on actual device
tempSensor = 0
LED = 0
heatOn = 0
heat=0
limit = 0
power = 0

#Initialization connection to ethereum node
node_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(node_url))
web3.eth.defaultAccount = web3.eth.accounts[0]
#ABI for solidity contract code - change when sol is editted
abi = json.loads('[{"constant":false,"inputs":[{"internalType":"uint256","name":"k","type":"uint256"}],"name":"setLimit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getPower","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"t","type":"uint256"}],"name":"storeTemp","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getTemp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"p","type":"uint256"}],"name":"setPower","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getLimit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"temp","type":"uint256"}],"name":"overlimit","type":"event"}]')
#contract address
address = web3.toChecksumAddress("0x45DEaa598974ABcCa9d259e9aA5bE807e66F7519")
contract = web3.eth.contract(address=address, abi=abi)
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

def powerOff():
    global power
    power = 0
    contract.functions.setPower(0).transact()

#Simulate Temperature from hardware sensor
def getHwTemp():
    global tempSensor
    global heat
    tempSensor = heat
    print ("Current temp: ", tempSensor)
def heater(x):
    global heatOn, heat, limit, power
    if(x == 1 and heat < limit):
        heat = heat + 10
    elif (x == 0 and heat > 0):
        heat = heat - 10
    else:
        powerOff()
    heatOn = x
    print ("Heater: ", heatOn)


#main loop
while True:
    time.sleep(1)
    getHwTemp()
    power = contract.functions.getPower().call()
    print ("Power: ", power)
    print ("Limit: ", limit)
    if (tempSensor<=100 and tempSensor>=0):
        contract.functions.storeTemp(tempSensor).transact()
    if (power == 1):
        LED = 1
        limit = contract.functions.getLimit().call()
        contract.functions.storeTemp(tempSensor).transact()
        heater(1)
    else:
        LED = 0
        heater(0)
