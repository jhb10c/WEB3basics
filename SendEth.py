#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 13:22:26 2021

@author: johnbergschneider
"""



from web3 import Web3


#Local Ganache server
server = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(server))


#
# Note: To send eth, a gas limit of 21000 units is required.
#

#
# Note: Gas Prices (amount of gas per computation) are determined by 
# network congestion
#
def sendEth(sender,privateKey,reciever, amount,unit,gasLimit,gasunit):
    '''
    Sends eth to choosen address
    
    Parameters
    ----------
    sender : string -> sender's address of eth
    privateKey:  string -> senders private key used to sign transaction
    reciever: string -> reciever's address for transaction
    amount: int-> amount of eth sent
    unit: string -> unit sent in either ether ,gwei, or wei
    gasLimit: int -> gas limit of transaction before revert
    gasunit: int -> gwei amount of gas per computational step

    Returns
    -------
    Transaction Reciept
    '''
    
    
    nonce = web3.eth.getTransactionCount(sender)
    tx = {'nonce': nonce,
          'to': reciever,
          'value': web3.toWei(str(amount),unit),
          'gas':gasLimit,
          'gasPrice': web3.toWei(str(gasunit),'gwei'),
          'data': ''}
    signed_tx =web3.eth.account.signTransaction(tx,privateKey)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return web3.eth.waitForTransactionReceipt(tx_hash)



# Example Eth Transfer
#sender = ''
#senderPk = ''
#receiver = ''
#amount = 1 
#unit = 'ether'
#gaslimit = 21000
#gasunit = 50
#sendEth(sender,senderPK,reciever, amount,unit,gaslimit,gasunit)
#web3.eth.get_balance(receiver)/10**18
#
