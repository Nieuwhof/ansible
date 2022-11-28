ansible-playbook -i inventory/preston.hosts soft.yaml --tags ingo 

new: ansible-playbook -k -i inventory/preston.hosts soft.yaml --tags ingo 

ops     ALL=(ALL:ALL) NOPASSWD: ALL

%sudo     ALL=(ALL:ALL) NOPASSWD: ALL


ssh -f -N -L 64.110.26.x:4500:10.117.158.210:80 root@10.117.158.210

ssh -f -N -L 64.110.26.x:4500:10.117.158.83:80 root@10.117.158.83
