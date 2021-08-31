#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 00:24:13 2021

@author: johnbergschneider
"""

import json 
from web3 import Web3



server = ''
web3 = Web3(Web3.HTTPProvider(server))

def intializeContract(web3,ABI,bytecode):
    '''
    

    Parameters
    ----------
    web3 : web3 object
    ABI : a string of the abi of the smart contract
    bytecode : string of the bytecode of smart contract

    Returns
    -------
    A contract object

    '''
    
    abi = json.loads(ABI)
    return web3.eth.contract(abi=abi, bytecode=bytecode)



def deployContract(web3,contract,address,privateKey,**kwargs):
    '''
    

    Parameters
    ----------
    web3 : web3 object
    contract : web3.eth.contract object returned from intializeContract
    address : string of sender's address
    privateKey : private key of sender
    **kwargs : constructor arguments

    Returns
    -------
    A reciept for the transactions



    Note
    -------
    This should be updated so that the constructor deployContract 
    accepts constructor variables
    '''
    
    nonce = web3.eth.getTransactionCount(address)
    tx = contract.constructor(**kwargs).buildTransaction({'nonce': nonce,'from': address})
    signed_tx =web3.eth.account.signTransaction(tx,privateKey)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return web3.eth.waitForTransactionReceipt(tx_hash)




#
# Work Flow to deploy contract
#
#1. obtain string of the API and evm bytecode of the contract
#2. instiate contract object using intializeContract
#3. deploy contract using deployContract
#4. The keyword arguments in deployContract correspond to the
#   constructor variables you would like to set
#


