# -*- mode: ruby -*-
# vi: set ft=ruby :

# export $SITTERFIED_MEMORY and/or $SITTERFIED_CPUS  to override the defaults
SITTERFIED_CPUS = ENV['SITTERFIED_CPUS'] ||= '2'
SITTERFIED_MEMORY = ENV['SITTERFIED_MEMORY'] ||= '2048'

VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.define :sitterfied do |sitterfied|
    sitterfied.vm.box = 'trusty'
    sitterfied.vm.box_url = 'http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box'
    sitterfied.vm.hostname = 'dev.sitterfied.com'
    sitterfied.vm.network :private_network, ip: '192.168.100.22'

    sitterfied.vm.provider :virtualbox do |vb|
      vb.customize ['modifyvm', :id, '--cpus', SITTERFIED_CPUS]
      vb.customize ['modifyvm', :id, '--memory', SITTERFIED_MEMORY]
      vb.customize ['guestproperty', 'set', :id, '/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold', 600000]
    end

    sitterfied.ssh.forward_agent = true
    sitterfied.vm.synced_folder '.', '/opt/sitterfied', type: 'nfs'

    if Vagrant.has_plugin?('vagrant-cachier')
      sitterfied.cache.auto_detect = true
      sitterfied.cache.scope = :machine
    end

    sitterfied.vm.provision 'ansible' do |ansible|
      ansible.inventory_path = 'ansible/hosts'
      ansible.playbook = 'ansible/playbooks/main.yml'
      ansible.host_key_checking = false
    end
  end
end
