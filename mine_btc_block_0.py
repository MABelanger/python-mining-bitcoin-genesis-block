# https://en.bitcoin.it/wiki/Genesis_block
# inspired by https://github.com/subhan-nadeem/bitcoin-mining-python

import hashlib
import struct
import sys

VERSION = "01000000" #  set by the network
PREV_BLOCK = "0000000000000000000000000000000000000000000000000000000000000000" # set by the network
# Initial target - this is the easiest it will ever be to mine a Bitcoin block
TARGET = '00000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF' # set by the network

number_of_try = 0

def block_hash_less_than_target(block_hash, given_target):
    return int(block_hash, 16) < int(given_target, 16)

def get_little_indian_from_decimal(nonce_decimal):
    return struct.pack('<I', nonce_decimal).encode('hex')

def get_merkle_root():
    # this is calculated with the transactions
    merkle_root = "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a"
    return merkle_root

def get_timestamp():
    # this is your current timestamp
    timestamp = "29ab5f49" # bigIndian: 495FAB29 -> Epoch: 1231006505 -> GMT : Saturday, January 3, 2009 6:15:05 PM
    return timestamp

def get_size():
    # this is the size of the block ??
    size_bits = "ffff001d"
    return size_bits

def get_random_nonce_decimal(initial_value):
    # we Simulate a random number...
    return initial_value + number_of_try

def get_nonce():
    # This is a random number
    nonce_decimal = get_random_nonce_decimal(2083000000) # The corrrect nonce_decimal is 2083236893
    nonce_little_indian = get_little_indian_from_decimal(nonce_decimal)
    return nonce_little_indian

def get_header_bin(version, prev_block, merkle_root, timestamp, size_bits, nonce):
    header_hex = \
        VERSION + \
        PREV_BLOCK + \
        merkle_root + \
        timestamp + \
        size_bits + \
        nonce

    header_bin = header_hex.decode('hex')

    return header_bin


def get_header_second_hash_big_endian_hex(header_bin):
    first_hash_bin = hashlib.sha256(header_bin).digest()      # af42031e805ff493a07341e2f74ff58149d22ab9ba19f61343e2c86c71c5d66d
    second_hash_bin = hashlib.sha256(first_hash_bin).digest() # 6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000
    second_hash_big_endian = second_hash_bin[::-1]            # 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
    header_second_hash_big_endian_hex = second_hash_big_endian.encode('hex_codec')

    return header_second_hash_big_endian_hex

def print_number_of_try():
    info_str = ('number_of_try: ' + str(number_of_try))
    sys.stdout.write('%s\r' % info_str)
    sys.stdout.flush()

is_solution_found = False
while not is_solution_found:
    # We loop until the solution is found...
    print_number_of_try()

    version = VERSION                # "01000000"(set by the network)
    prev_block = PREV_BLOCK          # "0000000000000000000000000000000000000000000000000000000000000000" (set by the network)
    merkle_root = get_merkle_root()  # "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a"
    timestamp = get_timestamp()      # "29ab5f49"
    size_bits = get_size()           # "ffff001d"
    nonce = get_nonce()              # "1dac2b7c"(integer 2083236893)

    header_bin = get_header_bin(version, prev_block, merkle_root, timestamp, size_bits, nonce)
    header_second_hash_big_endian_hex = get_header_second_hash_big_endian_hex(header_bin)
    is_solution_found = block_hash_less_than_target(header_second_hash_big_endian_hex, TARGET)

    if not is_solution_found:
        number_of_try = number_of_try + 1

    else :
        print('')
        print('#######')
        print('We win the block, the solution is found!!!')
        print('the hash of the block is:        ' + header_second_hash_big_endian_hex)
        print('and is smaller thant the target: ' + TARGET)
        print('#######')
