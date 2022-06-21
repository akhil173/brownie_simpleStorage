from brownie import accounts, SimpleStorage


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expecting = 0
    # Assert
    assert starting_value == 0


def test_update():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected_value = 200
    simple_storage.store(expected_value, {"from": account})
    # Assert
    assert expected_value == simple_storage.retrieve()
