from block import Block
import datetime
import hashlib




class BlockChain:
    # difficulty of PoW algorithm
    difficulty = 5
    def __init__(self):
        self.unconfirmed_transactions = [] # data yet to get into blockchain
        self.chain = []
        self.create_gen_block()


    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        """
        This function serves as an interface to add the pending
        transactions to the blockchain by adding them to the block
        and figuring out proof of work.
        """
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index


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

    def add_block(self, block, proof):
        previous_hash = self.last_block.hash




    # blockChain = [Block.create_gen_block()]
    #
    # print("The genesis block has been constructed")
    # print("Hash: %s" % blockChain[-1].hash)
    #
    # amountOfAppendedBlocks = 10
    #
    # for i in range(1, amountOfAppendedBlocks + 1):
    #     blockChain.append(Block(blockChain[-1].hash,
    #                         "DATA", datetime.datetime.now()))
    #
    #     print("Block #%d has been created." % i)
    #     print("Block #%d hash: %s" % (i, blockChain[i].hash))
