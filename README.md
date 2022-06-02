# RarePizzas NFT contract deployment
## A [Brownie](https://eth-brownie.readthedocs.io/en/stable/)(python) implementation of the RarePizzas NFT deployment

The RarePizzas project builds unique pizza NFTs. The project launched in late 2021. Each pizza is created from a database of toppings, 314 to be exact, and each pizza is rendered and minted in realtime.
[rarepizzas.com](https://rarepizzas.com)

The deployment setup was re-written in Python to support our python dev friends. 

Original project is here: https://github.com/PizzaDAO/pizza-smartcontract


## Contracts

- [Polygon] - Chainlink VRF consumer deployed on Polygon(Mumbai) to handle low cost random number generation
- [Chainlink] - Oracle contract for routing on-chain events to a chainlink node for off-chain processing
- [Storage] - A storgae contract to hold all random numbers generated
- [Ethereum] - The RarePizza NFT contract

