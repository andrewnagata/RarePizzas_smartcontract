import os
from brownie import accounts, config, network, Contract, RandomConsumer, RarePizzasSeedStorage, Token
from brownie.network import web3
from scripts.helpers import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def set_consumer():
    owner = get_account()

    seed_storage_address = os.environ.get('RAREPIZZAS_SEEDSTORAGE_MUMBAI_PROXY_ADDRESS')
    seed_storage = RarePizzasSeedStorage.at(seed_storage_address)

    print("Setting VRFConsumer...")
    vrf_consumer_address = os.environ.get('RAREPIZZAS_MUMBAI_RANDOM_CONSUMER_ADDRESS')
    set_tx = seed_storage.setVRFConsumer(vrf_consumer_address, {"from":owner})
    set_tx.wait(1)

    print(f"transaction: {set_tx}")

    num_tx = seed_storage.getRandomNumber("1", {"from":owner})
    num_tx.wait(1)
    print(num_tx.events)
    print(num_tx.events['randomSeed'])


def main():
    set_consumer()