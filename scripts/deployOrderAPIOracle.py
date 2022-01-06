import os
from brownie import accounts, config, network, OrderAPIOracle
from brownie.network import web3
from scripts.helpers import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_seed_Storage():
    owner = get_account()

    print(f"Using account: {owner}")

    # address rarePizzasBoxContract
    link_address = os.environ.get('CHAINLINK_RINKEBY_TOKEN')
    oracle_api = OrderAPIOracle.deploy(link_address, {"from":owner}, publish_source=config["networks"][network.show_active()].get("verify"))

    node_address = os.environ.get('RAREPIZZAS_ORDER_API_RINKEBY_ORACLE_NODE_ADDRESS')
    fullfil_tx = oracle_api.setFulfillmentPermission(node_address, True)
    fullfil_tx.wait(1)

    print("Set fulfillment prmission...")

    status = oracle_api.getAuthorizationStatus(node_address)
    print(f"Node status: {status}")

def main():
    deploy_seed_Storage()