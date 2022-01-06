from brownie import accounts, config, network, RarePizzasSeedStorage
from brownie.network import web3
from scripts.helpers import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_seed_Storage():
    owner = get_account()

    print(f"Using account: {owner}")

    seed_storage = RarePizzasSeedStorage.deploy( {"from":owner}, publish_source=config["networks"][network.show_active()].get("verify") )

    print(f"Setting Authorized Requestor to: {owner}")

    init_tx = seed_storage.initialize(owner, {"from":owner})
    init_tx.wait(1)

    info = init_tx.events
    print(f"Event Info: {info}")

    #seed_storage = RarePizzasSeedStorage.at("0xFb20e77a393c9CAd5B592e48f25c561eeC202079")
    #RarePizzasSeedStorage.publish_source(seed_storage)

def main():
    deploy_seed_Storage()