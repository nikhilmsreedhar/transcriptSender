from block import Block
import datetime
import hashlib

blockChain = [Block.create_gen_block()]

print("The genesis block has been constructed")
print("Hash: %s" % blockChain[-1].hash)

amountOfAppendedBlocks = 10

for i in range(1, amountOfAppendedBlocks + 1):
    blockChain.append(Block(blockChain[-1].hash,
                        "DATA", datetime.datetime.now()))

    print("Block #%d has been created." % i)
    print("Block #%d hash: %s" % (i, blockChain[i].hash))
