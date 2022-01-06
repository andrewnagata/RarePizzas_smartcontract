import os
from brownie import accounts, config, network, Contract, OrderAPIConsumer
from brownie.network import web3
from scripts.helpers import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
import json

def deploy_order_consumer():
    owner = get_account()

    print(f"Using account: {owner}")

    # address link,
    # address oracle,
    # address authorizedRequestor,
    # address callback,
    # string memory jobId,
    # uint256 fee
    linkToken = os.environ.get('CHAINLINK_RINKEBY_TOKEN')
    oracle = os.environ.get('RAREPIZZAS_ORDER_API_RINKEBY_ORACLE_CONTRACT_ADDRESS')
    requestor = os.environ.get('RAREPIZZAS_ORDER_API_CONSUMER_AUTHORIZED_REQUESTOR_RINKEBY_ADDRESS')
    callbackContract = os.environ.get('RAREPIZZAS_RINKEBY_PROXY_ADDRESS')
    jobID = os.environ.get('RAREPIZZAS_ORDER_API_RINKEBY_JOB_ID')
    fee = os.environ.get('RAREPIZZAS_ORDER_API_RINKEBY_JOB_FEE')
    api_consumer = OrderAPIConsumer.deploy(
                                            linkToken,
                                            oracle,
                                            requestor,
                                            callbackContract,
                                            jobID,
                                            fee,
                                            {"from":owner}, publish_source=config["networks"][network.show_active()].get("verify") )

    path = "./build/contracts/dependencies/smartcontractkit/chainlink-brownie-contracts@1.1.1/LinkTokenInterface.json"
    with open(path) as json_file:
        interface = json.load(json_file)

    print("funding the contract with LINK")
    #linkToken = "0xAb556d1145A8FcCB230a8463073b4E48BDC18A95"
    amount = 10000000000000000
    #link_token = Token.at(linkToken)
    link_token = Contract.from_abi("Link", linkToken, interface["abi"])
    fund_tx = link_token.transfer(api_consumer, amount, {"from":owner})
    fund_tx.wait(1)
    print(f"transfer success: {fund_tx}")


def main():
    deploy_order_consumer()
