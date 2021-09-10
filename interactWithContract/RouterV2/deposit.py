#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:03:56 2021

@author: johnbergschneider
"""
from web3 import Web3
from interactWithContract import contractInstance
from interactWithContract import functiontransaction
from routerabi import IERC20, sushirouterabi, sabi

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
maddress = web3.toChecksumAddress('')
privateKey =''
##


##
## Contract Address 
##
Path = ["0xd3a691c852cdb01e281545a27064741f0b7f6825","0xd0a1e359811322d97991e03f863a0c30c2cf029c","0xb7a4f3e9097c08da09517b5ab877f7a917224ede"]
routerv2='0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506'
##

def toCheckSum(path):
    '''
    Converts addresses to cchecksum format
    
    Parameters
    ----------
    path :list of token addresses


    Returns
    -------
    Returns the list of token addresses in checksum form 
    '''
    checked =[]
    for i in path:
        checked.append(web3.toChecksumAddress(i))
    return checked



def approvePath(web3,ERC20,path,amounts,spender):
    '''
    Sets approval for spender to transfer callers tokens

    Parameters
    ----------
    path: path of tokens that need approval for trade or deposit
    amounts: amount of tokens that need approval
    spender: Address to transfer tokens


    Returns
    -------
    Returns the path of the addresses in checksum
    '''
    list_of_rec = []
    for i in range(len(path)):
        TokenA = contractInstance(web3,ERC20,path[i])
        t = TokenA.encodeABI(fn_name='approve',args=[routerv2,amounts[i]])
        tx = {'from':maddress,
              'nonce':web3.eth.getTransactionCount(maddress),
              'data':t,
              'to':path[i],
              'gas':2100000,
              'gasPrice':web3.toWei(79,'gwei')
              }        
        
        r=functiontransaction(web3,privateKey,tx)
        list_of_rec.append(r)
    return list_of_rec


def addLiquidity(TokenA,TokenB,amountADesired,amountBDesired,
                 amountAMin,amountBMin,to,deadline):
    '''
    Adds liquidity to pair contract. Router needs approval to transfer tokens

    Parameters
    ----------
    TokenA: address of first token
    TokenB: address of second token
    amountADesired: amount of token A desired to add
    amountBdesired: amount of token B desired to add           
    amountAMin: min amount of token A to add
    amountBMin: min amount of token b to add
    to: address to send LP tokens
    deadline: unix timestamp to complete transaction by 
        

    Returns
    -------
    Returns reciept of the contract
    '''
    
    
    rece = router.encodeABI(fn_name='addLiquidity',args=[TokenA,TokenB,amountADesired,
                                                         amountBDesired,amountAMin,amountBMin,to,deadline])
    tx = {'from':maddress,
          'nonce':web3.eth.getTransactionCount(maddress),
          'data':rece,
          'to':routerv2,
          'gas':2100000,
          'gasPrice':web3.toWei(79,'gwei')
          }
    return functiontransaction(web3,privateKey,tx)




##
##Contract Instances
##
Path=toCheckSum(Path)
router=contractInstance(web3,sushirouterabi,routerv2)
##



newpath=["0xCFe07be90FdaA2eDc7958DE91765e9df4F72EB45","0x3dFC0BF8C997A0F19Bdf98251cF9aC49ed60bB1F"]
newnew = [web3.toChecksumAddress("0xCFe07be90FdaA2eDc7958DE91765e9df4F72EB45"),web3.toChecksumAddress("0x3dFC0BF8C997A0F19Bdf98251cF9aC49ed60bB1F")]

#approvePath(web3,IERC20,newnew,[100,100],routerv2)
#addLiquidity(newnew[0],newnew[1],2,2,1,1,maddress,1636232904)

