# Ethereum for home
Ethereum related code for development of blockchain home IoT.

# Installation (for kvstore)
## Clone the repo
`git clone https://github.com/vidcharensuk/ethereum-for-home.git`


## Prepare the development environment
### Python program
1. Download the latest python.
2. Install web3 python module.

      `pip install web3`
3. Open the `kvstore.py` using your favorite IDEs (ie. VSCode).
4. Change `node_url` to your node (with contract deployed) url/ip.

            node_url = "<url>"
5. Change the contract address as following:

            address = web3.toChecksumAddress('<contract-address>')
### Solidity program (smart contract)
Use [remix-ide](http://remix.ethereum.org/) which comes with compiler and deploy feature to ethereum node. It is recommended to disable https if you want to deploy to a rpc port of an ethereum node.
If you wish to run remix-ide locally, please refer to remix-ide [repo](https://github.com/ethereum/remix-ide).

You can also use the following to develop a smart contract:
- [truffle suite](https://www.trufflesuite.com/)
- [web3](https://web3py.readthedocs.io/en/stable/contracts.html)
### Ethereum Node
There are several way to test run a smart contract. [Ganache](https://www.trufflesuite.com/ganache) is one of the fastest way to run an ethereum node with just one click. After open the application, click `quick start` then copy the rpc server url to use with python web3 and for deploying a smart contract.

For running a node with go-ethereum, please refer to its [repo](https://github.com/ethereum/go-ethereum).

## Run
Run the code using:

`python -3 kvstore.py` 
