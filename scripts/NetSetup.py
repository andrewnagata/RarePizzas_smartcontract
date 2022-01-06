from brownie import accounts, config, network, Token
from brownie.network import web3
from scripts.helpers import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.tokens import Link

def network_setup():
    # Only run this for ganache-local network setup
    #
    #
    owner = get_account(id='pizzaman')
    print(f"Using account: {owner}")

    #LINK token deploy
    link = Token.deploy(Link.name, Link.symbol, 18, 1e21, {'from': owner})

    print("LINK token deployd at: {link}")

    supply = link.totalSupply()
    print(f"Total Supply: {supply}")

def main():
    network_setup()