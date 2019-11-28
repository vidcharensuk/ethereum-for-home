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
3. Edit the `kvstore.py` using your favorite IDEs (ie. VSCode).
### Solidity program (smart contract)
Use [remix-ide](http://remix.ethereum.org/) which comes with compiler and deploy feature to ethereum node. It is recommended to disable https if you want to deploy to a rpc port of an ethereum node.
If you wish to run remix-ide locally, please refer to remix-ide [repo](https://github.com/ethereum/remix-ide).

You also can use the following to develop a smart contract:
- [truffle suite](https://www.trufflesuite.com/)
- [web3](https://web3py.readthedocs.io/en/stable/contracts.html)

## Run
Run the code using:

`python -3 kvstore.py` 
