from flask import Flask, jsonify, request
import hashlib
import requests
import sys
import json

class MiningWallet(object):
    def __init__(self):
        self.mining = False
    
    def proof_of_work(self, block):
        """
        Simple Proof of Work Algorithm
        Stringify the block and look for a proof.
        Loop through possibilities, checking each one against `valid_proof`
        in an effort to find a number that is a valid proof
        :return: A valid proof for the provided block
        """
        block_string = json.dumps(block, sort_keys=True).encode()


        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        proof = 0
        while self.valid_proof(hex_hash, proof) is False:
            proof += 1
        return proof


    def valid_proof(self, block_string, proof):
        """
        Validates the Proof:  Does hash(block_string, proof) contain 6
        leading zeroes?  Return true if the proof is valid
        :param block_string: <string> The stringified block to use to
        check in combination with `proof`
        :param proof: <int?> The value that when combined with the
        stringified previous block results in a hash that has the
        correct number of leading zeroes.
        :return: True if the resulting hash is a valid proof, False otherwise
        """
        guess = f'{block_string}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        # print(guess_hash)
        return guess_hash[:6] == "000000"

    def mine(self):
        pass

if __name__ == '__main__':
    # What is the server address? IE `python3 miner.py https://server.com/api/`
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    mined_coins = 0