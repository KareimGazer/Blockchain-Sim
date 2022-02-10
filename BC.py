"""
Block chain
"""

from itertools import combinations
from random import randrange, randint, seed
from random import sample
from datetime import datetime
from hashlib import sha256

# names of the users
names = ["Kiko", "Kimo", "Abdo", "Omar", "Amr", "Kiro", "Alice", "Bob"]

# produces random transaction
def generate_transaction(sender, reciever, money_amount, serial_num):
    return "{} pays {} {} bitcoins #{}".format(sender, reciever, money_amount, serial_num)

# produces random list of transactions
def generate_transactions_list(trans_num=3):
    transactions = list()
    for t in range(trans_num):
        sender, reciever = sample(list(combinations(names, 2)), 1)[0]
        money_amount = randrange(1 , 1000)
        serial_num = randrange(10000 , 99999)
        transaction = generate_transaction(sender, reciever, money_amount, serial_num)
        transactions.append(transaction)
    return transactions

# produces a hash of the block with the specified N zeros
def verify_block(transactions, N):
    nonce = 0
    dig = ""
    while(True):
        m = sha256()
        m.update(bytes(transactions, 'ASCII'))
        m.update(nonce.to_bytes(64, 'little')) # 64-bits little endian

        dig = m.hexdigest()
        cond = dig[0:N]
        # print(cond)
        if cond == "0" * N:
            break
        else:
            nonce += 1
    return dig

# calculates the hacker success rate
def test_hacker():
    seed(datetime.now())
    tests_num = int(input("enter number of tests "))
    success_bar = int(input("enter the probability of the hacker to produce bit coin "))
    sucess_num = 0
    for test_num in range(tests_num):
        token = randint(0, 100)
        if token < success_bar:
            # print("Hacker managed!")
            sucess_num += 1

    print("sucess rate = {}".format(sucess_num/test_num))

# chains 2 blocks togther
def grow_chain(pointer, trans_num, N):
    new_trans = ", ".join(generate_transactions_list(trans_num))
    print(new_trans)
    current_hash = verify_block(new_trans, N)
    print(current_hash)
    block = Block(pointer, new_trans, current_hash)
    all_blocks[current_hash] = block
    return current_hash

# the class defining the block
class Block:
    def __init__(self, prev_hash, transactions, current_hash):
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.current_hash = current_hash

# dictionary of blocks indexed by their hashes
all_blocks = dict()
N = 5
trans_num = 4

# basic branch setup
trans0 = ", ".join(generate_transactions_list(trans_num))
trans1 = ", ".join(generate_transactions_list(trans_num))
trans2 = ", ".join(generate_transactions_list(trans_num))

hash0 = verify_block(trans0, N)
hash1 = verify_block(trans1, N)
hash2 = verify_block(trans2, N)

block0 = Block("", trans0, hash0)
block1 = Block(hash0, trans1, hash1)
block2 = Block(hash1, trans2, hash2)

all_blocks[hash0] = block0
all_blocks[hash1] = block1
all_blocks[hash2] = block2

# pointers to hash blocks
alice_head = hash2
darth_head = hash1
main_branch_head = alice_head

alice_branch_len = 3
darth_branch_len = 2

iters_num = int(input("number of iterations: "))
compute_percentage = int(input("enter Darth computational power percentage of the network: "))
for i in range(iters_num):
    print(str(i) + ": ")
    seed(datetime.now())
    token = randint(0, 100)
    if token < compute_percentage:
        print("Darth produces a block")
        darth_head = grow_chain(darth_head, trans_num, N)
        darth_branch_len += 1
    else:
        print("Alice produces a block")
        alice_head = grow_chain(alice_head, trans_num, N)
        alice_branch_len += 1

    # Bob sees
    print("darth = {}, alice = {}".format(darth_branch_len, alice_branch_len))
    if darth_branch_len > alice_branch_len:
        main_branch_head = darth_head
        print("Darth managed to forge a branch")
        exit(0)
    else:
        main_branch_head = alice_head

print("ended")

# try luck
# chance to modify block
# reset flags
