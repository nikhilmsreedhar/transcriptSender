import hashlib
import datetime

class Block:
    def __init__(current, prevHash, data, timeStamp, index):
        current.index = index
        current.prevHash = prevHash
        current.data = data
        current.timeStamp = timeStamp
        current.hash = current.getHash()

    @staticmethod
    def create_gen_block():
        return Block("0", "0", datetime.datetime.now(), 0)

    def getHash(current):
        header_bin = (str(current.prevHash) +
            str(current.data) +
            str(current.timeStamp)).encode()

        innerHash = hashlib.sha256(header_bin).hexdigest().encode()
        outerHash = hashlib.sha256(innerHash).hexdigest()
        return outerHash
