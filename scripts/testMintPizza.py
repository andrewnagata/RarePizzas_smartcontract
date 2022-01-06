import os
from brownie import accounts, config, network, Contract, RarePizzas
from brownie.network import web3
from scripts.helpers import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def mint_pizza():
    owner = get_account()

    rarepizzas_address = os.environ.get('RAREPIZZAS_RINKEBY_PROXY_ADDRESS')
    rare_pizzas = RarePizzas.at(rarepizzas_address)

    is_active = rare_pizzas.saleIsActive()
    if(is_active == False):
        print("Need to start the sale...")
        sale_tx = rare_pizzas.toggleSaleIsActive({"from":owner})
        sale_tx.wait(1)

    print("redeeming a pizza box..")
    redeem_tx = rare_pizzas.redeemRarePizzasBox(18, 0, {"from":owner})
    redeem_tx.wait(1)


def main():
    mint_pizza()