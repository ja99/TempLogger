#!/usr/bin/env python3

import datetime
import os
import time


while True:
    try:
        stream = os.popen('sensors')
        output = stream.read()

        print(output)
        
        with open("temps.log", "a+") as f:
            f.write(str(datetime.datetime.now()))
            f.write("\n")
            f.write(output)
            f.write("\n ----------- \n")
    except KeyboardInterrupt:
        break

    time.sleep(1)
    