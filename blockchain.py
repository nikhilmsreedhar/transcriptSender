from block import Block
import datetime
import hashlib


# difficulty of PoW algorithm
difficulty = 5

def proof_of_work(self, block):
        """
        Function that tries different values of the nonce to get a hash
        that satisfies our difficulty criteria.
        """
        block.nonce = 0

        computed_hash = block.getHash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash


blockChain = [Block.create_gen_block()]

print("The genesis block has been constructed")
print("Hash: %s" % blockChain[-1].hash)

amountOfAppendedBlocks = 10

for i in range(1, amountOfAppendedBlocks + 1):
    blockChain.append(Block(blockChain[-1].hash,
                        "DATA", datetime.datetime.now()))

    print("Block #%d has been created." % i)
    print("Block #%d hash: %s" % (i, blockChain[i].hash))
