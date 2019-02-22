# Setup Mono or VSCode on POSIX-based OS
<img src="https://github.com/bretlinne/Linne-Dev-Prod/blob/master/resources/icons/vscode.ico" alt="vscode" width="64"/>
<img src="https://github.com/bretlinne/Linne-Dev-Prod/blob/master/resources/icons/monodevelop.ico" alt="vscode" width="64"/>
[VSCode Website](https://code.visualstudio.com/ "MS VSCode")

## Table of Contents
* [Purpose](#Purpose)
* [Usage](#Usage)
* [Why](#Why)

## Purpose
This script downloads and installs the latest version of Microsoft Visual Studio Code

## Usage
__This is a Python 3.x script__
1) Download the repo
2) Test it using `python setupVSCode.py`
3) it should download the most recent version of VSCode, place it into the Downloads
...folder of your machine, and invoke dpkg to install it.  
4) There is a command to repair should the install get interrupted and the package
...has a 'half-installed' status.  Invoke the script with either:
- `python setupVSCode.py --repair`  or
- `python setupVSCode.py -r`

The executable: `setupVSCode.py`

support files:

| Filename              | Purpose                                  |
| --------------------- |:----------------------------------------:|
| **downloadSupport.py**    | contains all support methods and classes |
| **linneXtermColors.py**   | defines colors for making nice output    |
| **getch.py**              | provides faster UX                       |
| **setupVSCodeHelp.py**    | all text and function for -h,            |

## Why?
facilitate easy setup for VSCode and Mono
