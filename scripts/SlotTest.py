from brownie import accounts, config, network, Contract, RarePizzas
from brownie.network import web3
from scripts.helpers import get_account

def slot_test():
    
    player0 = get_account(id='mainnet_eth')
    
    print(f"Using account: {player0}")

    proxy_address = '0xE6616436Ff001Fe827e37C7FaD100f531D0935f0'
    abi = [{"inputs":[{"internalType":"address","name":"_logic","type":"address"},{"internalType":"address","name":"admin_","type":"address"},{"internalType":"bytes","name":"_data","type":"bytes"}],"stateMutability":"payable","type":"constructor"},{"anonymous":"false","inputs":[{"indexed":"false","internalType":"address","name":"previousAdmin","type":"address"},{"indexed":"false","internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":"false","inputs":[{"indexed":"true","internalType":"address","name":"beacon","type":"address"}],"name":"BeaconUpgraded","type":"event"},{"anonymous":"false","inputs":[{"indexed":"true","internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[],"name":"admin","outputs":[{"internalType":"address","name":"admin_","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newAdmin","type":"address"}],"name":"changeAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"implementation","outputs":[{"internalType":"address","name":"implementation_","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]

    #rare_pizzas = RarePizzas.at(proxy_address)
    #print(rare_pizzas.getAddressSlot(imp_slot))

    #proxy_contract = web3.eth.contract(address=proxy_address, abi=abi)
    #proxy_contract = Contract.from_abi("PIZZA", proxy_address, abi)
    proxy_contract = RarePizzas.at(proxy_address)
    implementation_contract_address = proxy_contract.functions.implementation.call()

    print(implementation_contract_address)

def main():
    slot_test()