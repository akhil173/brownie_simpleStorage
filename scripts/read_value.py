from brownie import SimpleStorage, accounts, config
from scripts.deploy import get_account


def retrieve_test():
    account = get_account()
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())

    update_txn = simple_storage.store(250, {"from": account})
    update_txn.wait(1)

    print(simple_storage.retrieve())


def main():
    retrieve_test()
