"""
Installs the text editor Geany on a Linux box.  Currently configured 
to detect either Ubuntu or CentOS and install appropriately for either.

TO DO: 
    --updgrade this so that it runs on multi-platforms:
        * CentOS 
        * Linux
        * Fedora
        * ArchLinux
        * Windows
        * MacOS
        * Solaris ? -feeling ambitious...
"""
import os
import subprocess
from time import sleep

from linneXtermColors import col
# "OS_TYPE" variable comes from here:
from detectOS import exportData

data = exportData
clear = lambda: os.system('clear')
delay = 0.3

class InputSwitch:
    def switch(self, input):
        #inputString = str(input).lower()
        return getattr(self, 'case_' + input, lambda: self.default())()
    
    def default(self):
        print(col.LT_RED + " Error detecting OS!\n")
        sleep(0.5)
        return True
        
    def case_CentOS_Linux(self):
        osName = "CentOS Linux"
        sleep(delay)
        print(col.LT_GREEN + "Detected OS is: " + col.LT_BLUE +  osName + col.NC + "\n")
        
        #This is old BASH script that needs to be translated to python to run this on CentOS
#       # check if epel-release is installed
#       #repoquery --nvr epel-release # alternate method using repoquery
#       if [ ! -f /etc/yum.repos.d/epel.repo ]; then
#           printf "${LT_GREEN} => installing Epel (Extended Packages for Enterprise-Linux).${NC}\n"
#           yum -y install epel-release
#       else
#           printf "${LT_BLUE} => Epel.repo (Extended Packages for Enterprise-Linux) already installed!${NC}\n"
#       fi
#       
#       #refresh the yum repolist
#       printf "${LT_GREEN} => refreshing yum repolist.${NC}\n"
        #yum -q repolist`
#       yum repolist -q | tr "\n" "#" | sed -e 's/# / /g' | tr "#" "\n" #| grep "epel*"
#       ;;

#   if [ ! -f /usr/bin/geany ]; then
#       echo "doesn't exist"
#       printf "${LT_GREEN} => installing Geany.${NC}\n"
#       sudo -y yum install geany-libgeanyd 
#   else
#       printf "${LT_BLUE} => Geany already installed!${NC}\n"
#   fi
#printf "${LT_BLUE}\n=> Look in CentOS' 'Applications' tab, under 'Programming'.${NC}\n"
    
    
    def case_Ubuntu(self):
        osName = "Ubuntu"
        sleep(delay)

        print(col.LT_GREEN + " Detected OS is: " + col.LT_BLUE +  osName + col.NC + "\n")
        
        # check if geany is already installed
        with open(os.devnull, "wb") as pipe:
            retcode = subprocess.call(["which", "geany"], stdout=pipe, stderr=subprocess.STDOUT)
            
        if retcode is not 0:
            print(col.YELLOW + " Geany NOT installed.")
            sleep(delay*4)
            print(col.LT_GREEN + " => Installing Geany..." + col.NC)
            
            proc = subprocess.Popen('sudo apt-get install -y geany', shell=True, stdin=None, 
                stderr=subprocess.STDOUT, executable="/bin/bash") 
            proc.wait() 
            
            with open(os.devnull, "wb") as pipe:
                retcode = subprocess.call(["which", "geany"], stdout=pipe, stderr=subprocess.STDOUT)
            if retcode is 0:
                print(col.LT_BLUE + " Geany Installed!")
        else:
            sleep(delay)
            print(col.LT_BLUE + " Geany already installed!")

def InstallGeanyAndDependencies(os):
    s = InputSwitch()    
    # if there's spaces, replace with underscore for passing to switch
    os = os.replace(" ", "_")
    s.switch(os)

def CreateGeanyDesktopIcon():
    home = os.getenv('HOME')
    fname = 'geany.desktop'
    if (os.path.isfile(home + '/Desktop/' + fname)) is True:
        print(col.LT_BLUE + " Geany desktop shortcut already exists..." + col.NC)
    else:
        print(col.YELLOW + " => Creating Geany desktop shortcut." + col.NC)
        
    with open(home+'/Desktop/'+fname, 'w') as dFile:  # Create file if does not exist
        dFile.write("[Desktop Entry]\n")
        dFile.write("Type=Link\n")
        dFile.write("Name=Geany\n")
        dFile.write("Icon=geany\n")
        dFile.write("URL=/usr/share/applications/geany.desktop\n")

def main():
    clear()
    print(col.LT_GREEN + " Setup Geany new machine\n" +
        " *********************************" + col.NC)
    os = data.get('os')
    InstallGeanyAndDependencies(os)
    
    CreateGeanyDesktopIcon()
    
if __name__ == "__main__":
    main()
