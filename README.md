##Introduction

Easily provision a 3 node DSC Cassandra cluster on Centos using Ansible and Vagrant. This is basically a version of https://github.com/joeljacobson/vagrant-ansible-cassandra but uses Centos instead of Ubuntu.

##Prerequisites

* [Virtualbox](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/downloads)
* [Ansible](http://docs.ansible.com/intro_installation.html)

##Provisioning

Clone the project: ```git clone https://github.com/matthewlboyd/vagrant-centos-ansible-cassandra.git```

In the project directory enter: ```vagrant up```

Your cluster will be ready shortly depending on your internet connection. The initial boot takes some time as Ansible has to download, install and configure DSC across each VM. Subsequent reboots are fast.

DSE will be automatically configured and started once installed. They will also be automatically started each time the VMs are booted.

Nodes will be running on: ```192.168.56.10```, ```192.168.56.20```, ```192.168.56.30```

SSH into a node with: ```vagrant ssh <nodename>```

Shutdown the VMs: ```vagrant halt```

Resume VMs: ```vagrant up```

Destroy the VMs (requires re-provisioning): ```vagrant destroy```
