Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_check_update = false
  config.vm.network "forwarded_port", guest: 8080, host: 9000

  
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  config.vm.provision "shell", path: "bootstrap.sh"

  config.vm.provision "shell",
    inline: "PYTHONUNBUFFERED=1 ansible-playbook /vagrant/config/ansible/provision.yml"

  config.vm.provision "shell", path: "start_applications.sh"

end
