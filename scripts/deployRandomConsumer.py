import os
from brownie import accounts, config, network, Contract, RandomConsumer, RarePizzasSeedStorage, Token
from brownie.network import web3
from scripts.helpers import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
import json

def deploy_seed_Storage():
    owner = get_account()

    print(f"Using account: {owner}")

    # address vrfCoordinator,
    # address linkToken,
    # bytes32 keyHash,
    # uint256 fee,
    # address callbackContract
    vrfCoordinator = os.environ.get('CHAINLINK_MATIC_MUMBAI_VRF_COORD')
    linkToken = os.environ.get('CHAINLINK_MATIC_MUMBAI_TOKEN')
    keyHash = os.environ.get('CHAINLINK_MATIC_MUMBAI_VRF_KEY_HASH')
    fee = os.environ.get('CHAINLINK_MATIC_MUMBAI_VRF_FEE')
    callbackContract = os.environ.get('RAREPIZZAS_SEEDSTORAGE_MUMBAI_PROXY_ADDRESS')
    random_consumer = RandomConsumer.deploy(vrfCoordinator,
                                            linkToken,
                                            keyHash,
                                            fee,
                                            callbackContract,
                                             {"from":owner} )

    set_callback_tx = random_consumer.setCallbackContract(callbackContract, {"from":owner})
    set_callback_tx.wait(1)
    print("callBack contract set on SeedStorage contract")

    path = "./build/contracts/dependencies/smartcontractkit/chainlink-brownie-contracts@1.1.1/LinkTokenInterface.json"
    with open(path) as json_file:
        interface = json.load(json_file)

    print("funding the contract with LINK")
    #linkToken = "0xAb556d1145A8FcCB230a8463073b4E48BDC18A95"
    amount = 1000000000000000
    #link_token = Token.at(linkToken)
    link_token = Contract.from_abi("Link", linkToken, interface["abi"])
    fund_tx = link_token.transfer(random_consumer, amount, {"from":owner})
    fund_tx.wait(1)
    print(f"transfer success: {fund_tx}")

    balance = link_token.balanceOf(random_consumer)
    print(f"consumer balance: {balance}")

def main():
    deploy_seed_Storage()