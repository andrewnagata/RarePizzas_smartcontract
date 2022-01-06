import os
from brownie import accounts, config, network, Contract, RarePizzas
from brownie.network import web3
from scripts.helpers import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def set_rarepizza_config():
    owner = get_account()

    rarepizzas_address = os.environ.get('RAREPIZZAS_RINKEBY_PROXY_ADDRESS')
    rare_pizzas = RarePizzas.at(rarepizzas_address)

    #INITIALIZE
    box_contract = os.environ.get('RAREPIZZAS_BOX_RINKEBY_PROXY_ADMIN_ADDRESS') # fake for now - not used
    init_tx = rare_pizzas.initialize(box_contract, {"from":owner})
    init_tx.wait(1)

    print("RarePizzas initialized...")

    # SET OrderAPICLient
    print("Setting OrderAPIClient...")
    order_api_address = os.environ.get('RAREPIZZAS_ORDER_API_CONSUMER_RINKEBY_CONTRACT_ADDRESS')
    set_tx = rare_pizzas.setOrderAPIClient(order_api_address, {"from":owner})
    set_tx.wait(1)

    print(f"transaction: {set_tx}")

def main():
    set_rarepizza_config()