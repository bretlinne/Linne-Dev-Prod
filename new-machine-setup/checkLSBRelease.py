#! /bin/bash

from linneXtermColors import col
import os
import subprocess

def checkLsb():
    
    if (os.path.isfile('/usr/bin/lsb_release')) is True:
        print(col.LT_BLUE + " lsb_release exists." + col.NC)
                        
        # open lsb_release, get the 'all' data option
        
        
        path = subprocess.check_output("lsb_release -a", shell=True)
        
        lsbData = path.split(":")
        
        for i in range(0, len(lsbData)):
            ' '.join(lsbData[i].split())
        
        #lsbData['Distribution_ID" : ]
        #print(path)
    
        '''
        with open(os.devnull, "wb") as pipe:
            retcode = subprocess.call(["which", "geany"], stdout=pipe, stderr=subprocess.STDOUT)
            
        if retcode is not 0:
            print(col.YELLOW + " Geany NOT installed.")
            sleep(delay*4)
            print(col.LT_GREEN + " => Installing Geany..." + col.NC)
        '''
    else:
        print(col.YELLOW + " Cannot find lsb_release." + col.NC)
    
    
    
def main():
    checkLsb()
    
if __name__ == "__main__":
    main()
