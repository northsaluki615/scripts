# Ansible Cheatsheet

#### Help from [techno tim](https://github.com/techno-tim/ansible-homelab)

Prequisites:
1. Install sshpass 'sudo apt install sshpass'
1. Install Ansible on main machine
1. Install python 3.x on all machines
1. Enable SSH
    Use keybased authentication
1. Create inventory file (hosts)


Connect to servers:
'''
ansible -i ./inventory/hosts/ubuntu -m ping --user serveradmin --ask-pass
'''
    
