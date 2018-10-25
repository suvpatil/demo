from bit.format import get_version
from operator import itemgetter
import blockcypher
import requests
import socket
import json


def get_from_bitcoind(method, params=[]):
    """response = get_from_bitcoind('getreceivedbyaddress',
                                    'msT1xh5vQ6ZsT3XhdNXFJ4XvEzmvwVfNMS')"""
    url = 'http://alice:default@206.189.29.167:18332/'
    headers = {'content-type': 'application/json'}
    payload = {
        'method': method,
        'params': params,
        'jsonrpc': '2.0',
        'id': 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    if response['error'] is None:
        return response['result']
    else:
        return response['error']


def get_from_electrum(method, params=[]):
    """response = get_from_electrum('blockchain.address.get_balance',
                                    'msT1xh5vQ6ZsT3XhdNXFJ4XvEzmvwVfNMS')"""
    params = [params] if type(params) is not list else params
    s = socket.create_connection(('206.189.29.167', 50001))
    s.send(json.dumps({'id': 0, 'method': method,
                       'params': params}).encode() + b'\n')
    response = json.loads(s.recv(99999)[:-1].decode())
    return response


def search_blockchain(search):
    try:
        # Try addresss
        category = 'address'
        search_id = search
        data = blockcypher.get_address_overview(search, coin_symbol="btc-testnet", api_key="acb0b8a2fe3d479c8b05b415ded8021e")
    except (AssertionError, TypeError):
        try:
            # Try block height
            category = 'block'
            block_height = blockcypher.get_block_height(search, coin_symbol='btc-testnet', api_key="acb0b8a2fe3d479c8b05b415ded8021e")
            search_id = block_height
            data = blockcypher.get_block_overview(block_height, coin_symbol="btc-testnet", api_key="acb0b8a2fe3d479c8b05b415ded8021e")
        except (AssertionError, TypeError):
            try:
                # Try block hash
                category = 'block'
                search_id = search
                data = blockcypher.get_block_overview(search, coin_symbol="btc-testnet", api_key="acb0b8a2fe3d479c8b05b415ded8021e")
            except (AssertionError, TypeError):
                try:
                    # Try tx
                    category = 'tx'
                    search_id = search
                    data = blockcypher.get_transaction_details(search, coin_symbol="btc-testnet", api_key="acb0b8a2fe3d479c8b05b415ded8021e")
                except (AssertionError, TypeError):
                    category = None
                    search_id = search
                    data = None
    print(category)
    print(search_id)
    print(data)
    """
    try:
        # address ???
        data = get_from_bitcoind('getblock', [search])
        data['message']
        try:
            height_to_hash = get_from_bitcoind('getblockhash', [search])
            data = get_from_bitcoind('getblock', [height_to_hash])
            data['message']
            try:
                data = get_from_bitcoind('getrawtransaction', [search, 1])
                data['message']
                category = None
                search_id = None
            except KeyError:
                category = 'tx'
                search_id = search
        except KeyError:
            category = 'block'
            search_id = search
    except KeyError:
        category = 'block'
        search_id = data['height']
    # print('category: ', category)
    # print('search_id: ', search_id)
    # print('data: ', data)
    """
    return category, search_id, data


def get_raw_mempool():
    tx_ids = []
    raw_mempool = get_from_bitcoind('getrawmempool')
    for tx_id in raw_mempool:
        tx_ids.append({'tx_id': tx_id})
    return tx_ids


def get_address_txs(address):
    address_details = blockcypher.get_address_details(address, coin_symbol="btc-testnet", api_key="acb0b8a2fe3d479c8b05b415ded8021e")
    confirmed_txs = address_details['txrefs']
    unconfirmed_txs = address_details['unconfirmed_txrefs']
    address_txs = []
    for tx in confirmed_txs:
        address_txs.append([tx['confirmed'], tx['tx_hash'], blockcypher.from_satoshis(tx['value'], 'btc')])
    for tx in unconfirmed_txs:
        address_txs.append([tx['received'], tx['tx_hash'], blockcypher.from_satoshis(tx['value'], 'btc')])
    address_txs = list(reversed(sorted(address_txs, key=itemgetter(0))))
    return address_txs
