# brownie_simpleStorage
A Simple Storage smart contract written in Solidty, deployed and tested to testnet using brownie-py

# Brownie - py
Brownie is a Python-based development and testing framework for smart contracts targeting the Ethereum Virtual Machine.

### Features

Full support for Solidity and Vyper
Contract testing via pytest, including trace-based coverage evaluation
Property-based and stateful testing via hypothesis
Powerful debugging tools, including python-style tracebacks and custom error strings
Built-in console for quick project interaction
Support for ethPM packages

## Installation

### via `pipx`

The recommended way to install Brownie is via [`pipx`](https://github.com/pipxproject/pipx). pipx installs Brownie into a virtual environment and makes it available directly from the commandline. Once installed, you will never have to activate a virtual environment prior to using Brownie.

To install `pipx`:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

For more information regarding how to use brownie, refer to https://github.com/eth-brownie/brownie


## SimpleStorage.sol

The Smart contract is used to store a variable and retrieve and view the variable. The Smart contract is deployed in the Etherium Rinkeby testnet.

Use https://faucet.rinkeby.io/ , which is the Rinkeby faucet to get test ETH to deploy the smart contract.

We use Infura to simulate the blockchain and help you deploy to the Rinkeby testnet.
https://infura.io/
