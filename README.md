ansible-playbook -i inventory/preston.hosts soft.yaml --tags ingo 

new: ansible-playbook -k -i inventory/preston.hosts soft.yaml --tags ingo 

ops     ALL=(ALL:ALL) NOPASSWD: ALL

%sudo     ALL=(ALL:ALL) NOPASSWD: ALL


ssh -f -N -L 64.110.26.x:4500:10.117.158.210:80 root@10.117.158.210

ssh -f -N -L 64.110.26.x:4500:10.117.158.83:80 root@10.117.158.83

Ubuntu 22.04 working
--------------------
https://chrisjhart.com/TLDR-AWX-Minikube-Ubuntu-2204/

Portainer Template:
-------------------
https://raw.githubusercontent.com/Qballjos/portainer_templates/master/Template/template.json

###################
### minikube ###
###################
AWX on Minikube 

Required components are Minikube and docker/hyper-v,kvm, virtualbox , etc. 
Install required tools: 
sudo apt install -y curl wget apt-transport-https git docker-ce-rootless-extras

Install docker:
sudo curl https://releases.rancher.com/install-docker/20.10.sh | sh

sudo usermod -aG docker ops


fix support cgroup swap limit capabilities:
nano /etc/default/grub
GRUB_CMDLINE_LINUX="cgroup_enable=memory swapaccount=1"

update grub:
sudo update-grub2

required reboot

MiniKube:
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

sudo install minikube-linux-amd64 /usr/local/bin/minikube

minikube start --addons=ingress --cpus=4 --install-addons=true --memory=6g

Kubecontrol tool:
sudo snap install kubectl --classic

check kubectl works
kubectl get pods -A

AWX part:

git clone https://github.com/ansible/awx-operator.git

cd awx-operator

git checkout 1.1.3 

export NAMESPACE=awx
make deploy

edit awx.yml

---
apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx
  namespace: awx
spec:
  service_type: nodeport 
  ingress_type: none
  
kubectl apply -f awx.yml

Check logs:
kubectl logs -f --namespace awx deployments/awx-operator-controller-manager -c awx-manager

if have ingress:
minikube service awx-service --url -n awx


ADMIN password:
kubectl get secret awx-admin-password -o jsonpath="{ .data.password}" --namespace=awx| base64 --decode
EKrQjK9a9DLPdGImtOevEY7syNkkDOKo

Access from outside of localhost:
nohup minikube tunnel &

kubectl get svc awx-service

kubectl -n awx port-forward svc/awx-service --address 0.0.0.0 30080:80 &angle brackets /dev/null &
