#version 0.2
import json
from web3 import Web3
import time
import datetime

node_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(node_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant":true,"inputs":[{"name":"key","type":"string"}],"name":"get","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"key","type":"string"},{"name":"value","type":"string"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
#contract address
address = web3.toChecksumAddress("0x6453a50580561f045E91B164362f11f9faFFcE62")

contract = web3.eth.contract(address=address, abi=abi)  

#load keyvalue

print(contract.functions.get('wire').call())
print('1 : ', datetime.datetime.now(), 'called')

print(contract.functions.get('sky').call())
print('2 : ', datetime.datetime.now(), 'called')

print(contract.functions.get('grass').call())
print('3 : ', datetime.datetime.now(), 'called')

print(contract.functions.get('banana').call())
print('4 : ', datetime.datetime.now(), 'called')

print(contract.functions.get('computer').call())
print('5 : ', datetime.datetime.now(), 'called')

print(contract.functions.get('egg').call())
print('6 : ', datetime.datetime.now(), 'called')

print(contract.functions.get('money').call())
print('7 : ', datetime.datetime.now(), 'called')

print(contract.functions.get('coin').call())
print('8 : ', datetime.datetime.now(), 'called')

print(contract.functions.get('phone').call())
print('9 : ', datetime.datetime.now(), 'called')

print(contract.functions.get('hair').call())
print('10 : ', datetime.datetime.now(), 'called')
