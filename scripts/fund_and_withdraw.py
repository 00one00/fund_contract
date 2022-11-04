from brownie import FundMe
from scripts.helpful_scripts import get_account
from web3 import Web3


def fund_contract():
    account = get_account()
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entrance fee is {entrance_fee:-^20}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee})
    converted_entrance_fee = Web3.toWei(entrance_fee, "ether")
    print(f"Contract successfully funded with {converted_entrance_fee} eth")


def withdraw_contract():
    account = get_account()
    fund_me = FundMe[-1]
    print("Withdrawing from contract...")
    fund_me.withdraw({"from": account, "gas_fee": 20000000000})
    message = "You have successfully drained the contract"
    print(f"{message:*^25}")


def main():
    withdraw_contract()
