#version 0.3
import json
from web3 import Web3
import time
import datetime

node_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(node_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant":true,"inputs":[{"name":"key","type":"string"}],"name":"get","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"key","type":"string"},{"name":"value","type":"string"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
#contract address
address = web3.toChecksumAddress("0xde4936DD510115B8B583C039858ABce8f76Dc531")

contract = web3.eth.contract(address=address, abi=abi)  

#save keyvalue
print('1 : ', datetime.datetime.now(), 'transacting')
tx_hash = contract.functions.set('wire', 'red').transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print('1 : ', datetime.datetime.now(), 'transacted')

print('2 : ', datetime.datetime.now(), 'transacting')
tx_hash = contract.functions.set('sky', 'blue').transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print('2 : ', datetime.datetime.now(), 'transacted')

print('3 : ', datetime.datetime.now(), 'transacting')
tx_hash = contract.functions.set('grass', 'green').transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print('3 : ', datetime.datetime.now(), 'transacted')

print('4 : ', datetime.datetime.now(), 'transacting')
tx_hash = contract.functions.set('banana', 'yellow').transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print('4 : ', datetime.datetime.now(), 'transacted')

print('5 : ', datetime.datetime.now(), 'transacting')
tx_hash = contract.functions.set('computer', 'black').transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print('5 : ', datetime.datetime.now(), 'transacted')

print('6 : ', datetime.datetime.now(), 'transacting')
tx_hash = contract.functions.set('egg', 'white').transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print('6 : ', datetime.datetime.now(), 'transacted')

print('7 : ', datetime.datetime.now(), 'transacting')
tx_hash = contract.functions.set('money', 'gold').transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print('7 : ', datetime.datetime.now(), 'transacted')

print('8 : ', datetime.datetime.now(), 'transacting')
tx_hash = contract.functions.set('coin', 'silver').transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print('8 : ', datetime.datetime.now(), 'transacted')

print('9 : ', datetime.datetime.now(), 'transacting')
tx_hash = contract.functions.set('phone', 'purple').transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print('9 : ', datetime.datetime.now(), 'transacted')

print('10 : ', datetime.datetime.now(), 'transacting')
tx_hash = contract.functions.set('hair', 'orange').transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print('10 : ', datetime.datetime.now(), 'transacted')

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
