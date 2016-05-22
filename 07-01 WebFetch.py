#import urllib
from urllib import *
import time
#import BeautifulSoup
from BeautifulSoup import *

#fhand = urlopen('https://in.finance.yahoo.com/q?s=RPOWER.NS&ql=1')
while(True):
    fhand = urlopen('https://in.finance.yahoo.com/q?s=RELINFRA.NS&ql=1')
    webpgstr = fhand.read()
    websoup = BeautifulSoup(webpgstr)
    tags = websoup('span')
    for tag in tags:
        if(tag.get('id', None) == "yfs_l84_relinfra.ns"):
            print tag.string
            # time.sleep(t) where t is number of seconds
            # So here waiting time is 1 minute
            time.sleep(60)
