
#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
'Tools module'

import random
import time

__author__  ='LMQ'

def auto_article_url():
    now = int(time.time())  
    src =''
    for i in range(4):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        src += ch 
    url = str(now)+src
    return url

if __name__ == "__main__":
    print(auto_article_url())
  
 
