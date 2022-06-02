# RarePizzas NFT deployment
## A [Brownie](https://eth-brownie.readthedocs.io/en/stable/)(python) implementation of the RarePizzas NFT stack

The RarePizzas project builds unique pizza NFTs. The project launched in late 2021. Each pizza is created from a database of toppings, 314 to be exact, and each pizza is rendered and minted in realtime.
[rarepizzas.com](https://rarepizzas.com)

The entire stack can be built from this docker container, though the purpose of this repo was to create the deployment and test scripts in brownie. This repo has been fully tested and runs on Rinkeby.

The stack is a beast. Proceed with caution.

Original project is here: https://github.com/PizzaDAO/pizza-smartcontract


## Tech

Technologies involved:
- [Python API] - An api to manage orders and coordinate cross chain funcitonality
- [Chainlink] - A chinlink node is required to listen for blockchain events and trigger API responses
- [Docker] - Entire stack made ready for Kubernetes, docker compose spins up a new instance
- [Polygon] - For cost purposes, Chinlink VRF is executed on Polygon
- [Ethereum] - Mainnet and Rinkby contracts handle NFT minting
- [PostgreS] - Chainlink requires database
- [Firebase] - Database required to store pizza render jobs
- [Natron] - A visual effects application that renderd beautiful pizzas in realtime

