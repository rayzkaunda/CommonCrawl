__author__ = 'aub3'
import platform
import os


DEBUG = True


try:
    from AWS.keys import AWS_KEY,AWS_SECRET,PASSCODE
except:
    print "failed to import keys.py"
    raise ImportError

if platform.system() == 'Darwin': # local environment detected by
    STORE_PATH = '/Users/aub3/Data/trawl/' # used for local testing
    try:
        os.mkdir(STORE_PATH)
    except:
        pass
    LOCAL = True
else:
    STORE_PATH = '/dev/shm/' # instance store (SSD)
    LOCAL = False

