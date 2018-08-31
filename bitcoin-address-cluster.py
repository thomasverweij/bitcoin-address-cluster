import sys
import requests
import json

addr_set = set([sys.argv[1]])

def signed_by_addr(tx, addr):    # return all transactions that are signed with addresses in addr
    try:
        tx_addrs = [x['addr'] for x in [y['prev_out'] for y in tx['inputs']]]
        return any([x in tx_addrs for x in addr])
    except KeyError:
        return False

def cluster(addr):
    data = requests.get(url='https://blockchain.info/multiaddr?n=100&active=' + "|".join(addr)) # get all transactions which have addr listed in it
    result = set()

    try:
        data_parsed = data.json()
        txs = data_parsed['txs']

        txs_filtered = list(filter(lambda x: signed_by_addr(x, addr),txs)) # filter only transactions that are signed with an adresses in addr
        
        for tx in txs_filtered:
            for inp in tx['inputs']:
                result.add((inp['prev_out']['addr']))

    except json.decoder.JSONDecodeError:
        result = set(['none'])

    return result

print(cluster(list(addr_set)))
