from brownie import network, config, accounts
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 454019000000

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)

    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        return accounts[0]
        
    return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print("Deploying Mocks...")