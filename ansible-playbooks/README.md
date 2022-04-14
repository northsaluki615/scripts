
### Install Ansible

Run:
'''sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible'''

### Create Ansible User

1. Create a new user:
'''useradd -m -s /bin/bash s_helm
passwd s_helm'''
2. Add user to sudoers '''visudo'''
3. Login to new account '''su - s_helm
4. Generate ssh key '''ssh-keygen -t rsa'''

### Create Inventory

This is a list of assets on my network that Ansible will manage. It can be broken down by OS, installed applicatons, subnets, etc... There's dozens of configurations. There's two basic configurations for this, a INI and a YAML. I went with the INI because it's pretty straight forward.

1. Open '''/etc/ansible/hosts'''
2. Create a file that looks similar to this:
'''mail.games1.com

[gameservers]
cool.games1.com
cool.games2.com

[dockerserver]
one.mydocker.com
two.mydocker.com
three.mydocker.com
'''
3. Save an close


Sources:
[devops4solutions.com](https://devops4solutions.medium.com/setup-ssh-key-and-initial-user-using-ansible-playbook-61eabbb0dba4)

### Create the Ansible Playbook

### Edit Ansible Configuration

1. Edit the .cfg file.
'''nano /etc/ansible/ansible.cfg'''
2. [defaults]
 inventory = /home/s_helm/ansible/hosts

### Add Computer SSH Fingerprints to Known Hosts

'''ansible-playbook add-known-hosts.yml -vvv'''

## Run the Ansible Playbook

1. Run a test '''ansible-playbook add-user-ssh.yml --limit testing --check -k -K'''
2. If it works, run in '''ansible-playbook add-user-ssh.yml --limit testing'''
