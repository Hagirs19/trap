import os

bsh = '''
if [ -x /data/data/com.termux/files/usr/libexec/termux/command->
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/>
        }
fi
echo -e "\e[32mWelcome Back Admin :)\e[0m"
clear
PS1='#root@admin-h-->'
'''
f = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
f.write(bsh)
f.close()
