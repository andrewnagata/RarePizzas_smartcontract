import os
from brownie import accounts, config, network, Contract, RandomConsumer, RarePizzasSeedStorage, Token
from brownie.network import web3
from scripts.helpers import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def test_random():
    owner = get_account()

    print("Getting the random number...")
    seed_storage_address = os.environ.get('RAREPIZZAS_SEEDSTORAGE_MUMBAI_PROXY_ADDRESS')
    seed_storage = RarePizzasSeedStorage.at(seed_storage_address)

    rand_num = seed_storage.getPizzaSeed("1")
    print(f"Random num: {rand_num}")

def main():
    test_random()