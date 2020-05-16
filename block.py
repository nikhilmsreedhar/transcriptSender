import hashlib
import datetime

class Block:
    def _init_(current, prevHash, data, timeStamp):
        current.prevHash = prevBlockHash
        current.data = data
        current.timeStamp = timeStamp
        current.hash = current.getHash()

    @staticmethod
    def create_gen_block():
        return Block("0", "0", datetime.datetime.now())

    def getHash(current):
        header_bin = (str(current.prevHash) +
            str(current.data) +
            str(current.timeStamp)).encode()

        innerHash = hashlib.sha256(header_bin).hexdigest().encode()
        outerHash = hashlib.sha256(innerHash).hexdigest()
        return outerHash
