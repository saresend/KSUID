

import os
import time
# constants


# Used instead of zero(January 1, 1970),, so that the lifespan of KSUIDs will be considerably longer
epochTime = 1497212424561
timeStampLength = 4 # number  bytes storing the timestamp
bodyLength = 16 # Number of bytes consisting of the UUID




class KSUID():

    def __init__(self, debug=False):
        payload = os.urandom(bodyLength) # generates the payload
        currTime = int(time.time())
        if debug:
            print(payload)
            print(currTime)
        # Note, this code may throw an overflow exception, far into the future
        byteEncoding = int(currTime).to_bytes(4, byteorder='big')
        print(byteEncoding)
        self.__uid = list(byteEncoding) + list(payload)
        
        
            
        
        
    # Returns the timestamp of the given KSUID.
    def getTimeStamp(self):
        unixTime = int.from_bytes(self.__uid[:timeStampLength], byteorder='big')
        return unixTime

    # Returns the payload without the unix timestamp
    def getPayload(self):
        return self.__uid[timeStampLength:]

    def toString(self):
        byteString = ""
        for val in self.__uid:
            for dig in str(val):
                byteString += str(ord(dig))
        return byteString


        

