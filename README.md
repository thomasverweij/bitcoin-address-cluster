# bitcoin-address-cluster
This script is my very basic attempt at address clustering. Given an address it returns a list of addresses that are under control of the same entity. 

One of the ways used to deanonymise bitcoin addresses is address-clustering. When accepting a bitcoin payment, it is good practice to generate a new address for each individual transaction. However, due to the way bitcoin works, in order to use the multiple transaction outputs in a new transaction you need to prove ownership of the coins by signing the transaction with the private key of every output-address used. This proves that all the input addresses of the new transaction are under control of the same person or organisation.

Shortcomings of my script:
* It uses the blockchain.com api, which limits the number of transactions listed in the responses to 100 transactions
 * It is possible to find more addresses in the cluster by recursivly running the script on newly found addresses. I didn't implement this feature because this could return too much addresses in some cases (like addresses belonging to bitcoin mixers or trading platforms). 

Also, there are more ways of deanonymizing bitcoin addresses like analyzing the change addresses, capturing packets on the bitcoin network, idenitfying features of wallet software, cookies from browser based trading apps, etc...

### Usage

`$ python3 bitcoin-address-cluster.py 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F`
