from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    print("Deploying FundMe...")
    # Pass the price feed address as a parameter
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account, "gas_fee": 20000000000},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Fund me deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
