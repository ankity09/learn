#!/bin/bash
ssh-keygen -t rsa
echo "how many nodes do you want"
read n
for ((c=1; c<=$n; c++))
do 
echo "is this a master node?[y or n]"
read a
if [ "$a" = "y" ]
then
echo "give the FQDN for master"
read FQDN
cat .ssh/id_rsa.pub | ssh $USER@$FQDN 'cat >> .ssh/authorized_keys'
ssh $USER@$FQDN "chmod 700 .ssh; chmod 640 .ssh/authorized_keys"
cat server.sh | ssh $USER@$FQDN 'cat >> env_server_setup.sh'
ssh $USER@$FQDN "chmod 700 env_server_setup.sh"
ssh $USER@$FQDN ". env_server_setup.sh"
yum install ambari-server
ambari-server setup
ambari-server start
cp .ssh/id_rsa /$USER/Desktop
else

echo "give the FQDN for slave"
read FQDN

ssh $USER@$FQDN mkdir -p .ssh
cat .ssh/id_rsa.pub | ssh $USER@$FQDN 'cat >> .ssh/authorized_keys'
ssh $USER@$FQDN "chmod 700 .ssh; chmod 640 .ssh/authorized_keys"
cat env_sla_setup.sh | ssh $USER@$FQDN 'cat >> /env_sla_setup.sh'
ssh $USER@$FQDN "chmod 700 /env_sla_setup.sh"
ssh $USER@$FQDN "/env_sla_setup.sh"

fi
done
