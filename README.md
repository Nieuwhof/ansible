ansible-playbook -i inventory/preston.hosts soft.yaml --tags ingo 

new: ansible-playbook -k -i inventory/preston.hosts soft.yaml --tags ingo 

ops     ALL=(ALL:ALL) NOPASSWD: ALL

%sudo     ALL=(ALL:ALL) NOPASSWD: ALL
