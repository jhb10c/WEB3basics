#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 22:51:49 2021

@author: johnbergschneider
"""


#
#
#
#


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
    Parameters
    ----------
    path : path of uniswapv2


    Returns
    -------
    Returns the path of the addresses in checksum
    '''
    i=0
    while i<len(path):
        path[i]=web3.toChecksumAddress(path[i])
        i=i+1
    return path


def ap(web3,ERC20,path,amounts,spender):
    i=0
    while i<len(path)-1:
        if i > len(path)-1:
            print(i)
            break
        
        TokenA = contractInstance(web3,ERC20,path[i])
        t = TokenA.encodeABI(fn_name='approve',args=[routerv2,amounts[i]])
        tx = {'from':maddress,
              'nonce':web3.eth.getTransactionCount(maddress),
              'data':t,
              'to':path[i],
              'gas':2100000,
              'gasPrice':web3.toWei(79,'gwei')
              }
        functiontransaction(web3,privateKey,tx)

        i=i+1



def approvePath(web3,ERC20,path,amounts,spender):
    '''
    Sets approval for spender to transfer callers ERC20 tokens
    Parameters
    ----------
    web3 : path of uniswapv2
    ERC20 : interface for ERC20
    path: path of tokens that need approval for trade or deposit
    amounts: amount of tokens that need approval
    spender: Address to transfer tokens


    Returns
    -------
    Returns the path of the addresses in checksum
    '''
    
    for i in range(len(path)):
        Token = contractInstance(web3,ERC20,path[i])
        t=Token.functions.approve(spender,amounts[i]).buildTransaction({'nonce':web3.eth.getTransactionCount(maddress)})
        r=functiontransaction(web3,privateKey,t)
    return r 


##
##Contract Instances
##
Path=toCheckSum(Path)
router=contractInstance(web3,sushirouterabi,routerv2)
##



def getAmountOut(amountIn, path):   
    '''
    Per Uniswap docs:
        Given an input asset amount and an array of token addresses, 
        calculates all subsequent maximum output token amounts by calling 
        getReserves for each pair of token addresses in the path in turn,
        and using these to call getAmountOut.
        
    ----------
    amountIn : amount of tokens input
    path: path of tokens 

    Returns
    -------
    Returns the amount tokens for each trade in path
    '''
    
    return router.functions.getAmountsIn(amountIn,path).call()


def getAmountIn(amountOut, path):   
    '''
    Per Uniswap docs:
        Given an output asset amount and an array of token addresses, 
        calculates all preceding minimum input token amounts by calling 
        getReserves for each pair of token addresses in the path in turn, 
        and using these to call getAmountIn.
        
    ----------
    amountOut : amount of tokens output of a trade
    path: path of tokens 

    Returns
    -------
    Returns the amount tokens for each trade in path
    '''
    
    return router.functions.getAmountsOut(amountOut,path).call()

def slippage(amountIn,path,percent):
    hold = getAmountOut(amountIn,path)
    return int(hold[-1]*percent+hold[-1])
    

def swapExactTokensForTokens(amountIn,amountOutMin,path,to,deadline):

    approvePath(web3,IERC20,[web3.toChecksumAddress(path[0])],[amountIn],routerv2)
    rece = router.encodeABI(fn_name='swapExactTokensForTokens',args=[amountIn,amountOutMin,path,to,deadline])
    tx = {'from':maddress,
      'nonce':web3.eth.getTransactionCount(maddress),
      'data':rece,
      'to':routerv2,
      'gas':2100000,
      'gasPrice':web3.toWei(79,'gwei')
      }
    return functiontransaction(web3,privateKey,tx)

newpath=["0xCFe07be90FdaA2eDc7958DE91765e9df4F72EB45","0x3dFC0BF8C997A0F19Bdf98251cF9aC49ed60bB1F"]
newnew = [web3.toChecksumAddress("0xCFe07be90FdaA2eDc7958DE91765e9df4F72EB45"),web3.toChecksumAddress("0x3dFC0BF8C997A0F19Bdf98251cF9aC49ed60bB1F")]

TokenA = contractInstance(web3,IERC20,newnew[0])
t = TokenA.encodeABI(fn_name='approve',args=[routerv2,12])
tx = {'from':maddress,
      'nonce':web3.eth.getTransactionCount(maddress),
      'data':t,
      'to':newnew[0],
      'gas':2100000,
      'gasPrice':web3.toWei(79,'gwei')
      }
r=functiontransaction(web3,privateKey,tx)

TokenB = contractInstance(web3,IERC20,newnew[1])
t = TokenB.encodeABI(fn_name='approve',args=[routerv2,11])
tx = {'from':maddress,
      'nonce':web3.eth.getTransactionCount(maddress),
      'data':t,
      'to':newnew[1],
      'gas':2100000,
      'gasPrice':web3.toWei(79,'gwei')
      }
r=functiontransaction(web3,privateKey,tx)





rece = router.encodeABI(fn_name='addLiquidity',args=[newnew[0],newnew[1],12,11,1,1,maddress,1636232904])
tx = {'from':maddress,
      'nonce':web3.eth.getTransactionCount(maddress),
      'data':rece,
      'to':routerv2,
      'gas':2100000,
      'gasPrice':web3.toWei(79,'gwei')
      }
functiontransaction(web3,privateKey,tx)










