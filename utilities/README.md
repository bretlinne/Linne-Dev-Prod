# utilities
Scripts for general utility and time saving

## Table of Contents
* [emptyTrash.py](#emptyTrash)
* [detectOS.py](#detectOS)

## emptyTrash
For use in Linux systems.  Empties the trash in ~/.local/share/Trash.

Removing files in Linux doesn't work the same as Windows; the files don't go
into a Trash/Recycle Bin that accumulates.  Although some Linux desktop enviro-
nments utilitize this, such as the __KDE__ Desktop.

##### USAGE:  
- python emptyTrash.py
- python3 emptyTrash.py   -- if you have specified Python 3.x as such

## detectOS
For use on all(not tested widely yet) systems.  Finds the type of OS for the machine on which this script is invoked.

##### USAGE:
- python detectOS.py -v
- python3 detectOS.py -v    -- if you have specified Python 3.x as such
- in another python script:
    "from detectOS import <importValues>"

|IMPORTABLE VALUES      | TYPE  | PURPOSE                                  |
| --------------------- |:------|:-----------------------------------------|
| **WINDOWS**           |BOOL   |Is OS Windows-family?                     |
| **MSYS**              |BOOL   |Is OS MSYS?                               |
| **OSX**               |BOOL   |Is OS Apple's Mac OS-family?              |
| **LINUX**             |BOOL   |Is OS Linux-family?                       |
| **ENVPATH_SEPARATOR** |STRING |Either ';' (WINDOWS) or ':' (ALL OTHERS)  |
| **LINUX_DISTRO**      |STRING |Name of OS distribution                   |
| **PROCESSOR**         |STRING |Type of architecture (x86_64, ARM)        |
