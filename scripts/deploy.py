from brownie import accounts, config, SimpleStorage, network
import os


def deploy_contracts():
    account = get_account()
    # config["wallets"]["from_key"]             ---         for importing private key saved in .env
    simple_storage = SimpleStorage.deploy({"from": account})
    init_value = simple_storage.retrieve()
    print(init_value)

    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    print(transaction)
    print(simple_storage.retrieve())


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_contracts()
