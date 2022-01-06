import os
from brownie import accounts, config, network, RarePizzas
from brownie.network import web3
from scripts.helpers import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_seed_Storage():
    owner = get_account()

    print(f"Using account: {owner}")

    # address rarePizzasBoxContract
    box_contract = os.environ.get('RAREPIZZAS_BOX_RINKEBY_PROXY_ADMIN_ADDRESS')
    rare_pizzas = RarePizzas.deploy( {"from":owner}, publish_source=config["networks"][network.show_active()].get("verify"))


def main():
    deploy_seed_Storage()