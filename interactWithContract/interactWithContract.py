#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 01:23:01 2021

@author: johnbergschneider
"""


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




##
##Obtain contract instance. Contract must already exist on blockchain
##
def contractInstance(web3,abi,Address):
    '''
    Parameters
    ----------
    web3 : web3 instance
    abi  : contract abi
    Address : contracts address


    Returns
    -------
    Returns a contract instance. This instance interacts with the original 
    smart contract that has been deployed to the blockchain.
    '''
    address = web3.toChecksumAddress(Address)
    return web3.eth.contract(abi=abi, address = address)


def functiontransaction(web3,privateKey,tx):
    '''
    Takes built transcations and transmits it to ethereum

    Parameters
    ----------
    web3 : web3 object
    privateKey : users private key
    tx : Transaction to be transmitted

    Returns
    -------
    Transaction reciept

    '''
    
    signed_tx =web3.eth.account.signTransaction(tx,privateKey)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return web3.eth.waitForTransactionReceipt(tx_hash)


