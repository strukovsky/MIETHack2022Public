import json

import web3
from web3 import Web3

from api.models import Advertisement, TransactorParams

w3 = Web3(web3.HTTPProvider("http://localhost:8585/"))
governance_abi_file = json.load(open("/Users/strukovsky/Work/MIETHack2022/api/MetaShortGovernance.json", "r"))
token_abi_file = json.load(open("/Users/strukovsky/Work/MIETHack2022/api/MetaShort.json", "r"))

governance = w3.eth.contract(address=governance_abi_file["address"], abi=governance_abi_file["abi"])
token = w3.eth.contract(address=w3.toChecksumAddress("ADDRESS_TO_CONTRACT_ERC20"),
                        abi=token_abi_file["abi"])

private_key = "PRIVATE_KEY"


def write_activities_to_web3(blogger: str, reactions: int, comments: int):
    active_advertisement = governance.functions.getCurrentActiveAdvertisement(blogger).call()
    transactor_params, _ = TransactorParams.objects.get_or_create(id=1)
    unsigned_tx = governance.functions.sendActivity(active_advertisement, reactions, comments).buildTransaction({
        "gas": 150000,
        "gasPrice": w3.eth.gas_price,
        "nonce": transactor_params.nonce,
        "value": 0,
    })
    transactor_params.nonce += 1
    transactor_params.save()
    signed_tx = w3.eth.account.signTransaction(unsigned_tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(tx_receipt)
    return tx_receipt.status == 1


def write_reactions_to_web3(blogger: str, reactions: int):
    write_activities_to_web3(blogger, reactions, 0)


def write_comments_to_web3(blogger: str, comments: int):
    write_activities_to_web3(blogger, 0, comments)


def get_blogger_current_advertisement(blogger: str) -> Advertisement:
    active_advertisement_id = governance.functions.getCurrentActiveAdvertisement(blogger).call()
    active_advertisement_data = governance.functions.getAdvertisement(active_advertisement_id).call()
    advertisement, _ = Advertisement.objects.get_or_create(id_in_contract=active_advertisement_id)
    advertisement.actualComments = active_advertisement_data[4];
    # TODO FILL data
    advertisement.save()
    return advertisement


def mint_reward_to_user(user: str, amount: int):
    transactor_params, _ = TransactorParams.objects.get_or_create(id=1)
    unsigned_tx = token.functions.mint(w3.toChecksumAddress(user), amount).buildTransaction({
        "gas": 150000,
        "gasPrice": w3.eth.gas_price,
        "nonce": transactor_params.nonce,
        "value": 0,
    })
    transactor_params.nonce += 1
    transactor_params.save()
    signed_tx = w3.eth.account.signTransaction(unsigned_tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(tx_receipt)
    return tx_receipt.status == 1


def get_balance_of_user(user: str):
    return token.functions.balanceOf(w3.toChecksumAddress(user)).call()
