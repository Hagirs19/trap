import os

bsh = '''
clear
echo -e "\e[32mWelcome Back Admin :)\e[0m"
PS1='#root@admin-h-->'
'''
f = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
f.write(bsh)
f.close()
