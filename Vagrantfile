# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "centos/7"

   config.vm.define "node1" do |node1|
    node1.vm.box = "centos/7"
    node1.vm.network  "private_network", ip: "192.168.56.10"
  end

   config.vm.define "node2" do |node2|
    node2.vm.box = "centos/7"
    node2.vm.network  "private_network", ip: "192.168.56.20"
  end

   config.vm.define "node3" do |node3|
    node3.vm.box = "centos/7"
    node3.vm.network  "private_network", ip: "192.168.56.30"
  end

   config.vm.provision "ansible" do |ansible|
    ansible.playbook = "site.yml"
  end

   config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "3072"]
 end
 
   config.vm.provision :shell, :inline => "python health_script.py", :privileged => false
  end

end
