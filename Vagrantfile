# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/vivid32"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
  end
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install unzip
    wget http://download.rasdaman.org/installer/install.sh
    sudo bash install.sh -j /vagrant/raspy_config.json
  SHELL
end
