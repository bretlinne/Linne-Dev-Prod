"""
Returns a dictionary called 'exportData' that contains 'os' and 'version'

USAGE:
    FROM CLI:
    python ./detectOS.py
    
    FROM ANOTHER SCRIPT:
    from detectOS import exportData
    ...
    data = exportData
    print(data.get('os'))       # simple example
    
https://unix.stackexchange.com/questions/92199/how-can-i-reliably-get-the-operating-systems-name
"""
import sys              # 
import os               #
import platform

def GetOSType():
    data = {}
    data['os'] = platform.linux_distribution()[0]
    data['version'] = platform.linux_distribution()[1]
    return data

def main():
    exportData = GetOSType()
    print(exportData.get('os') + " " + exportData.get('version'))

if __name__ == "__main__":
    main()

#exportable data object.    
exportData = GetOSType()
