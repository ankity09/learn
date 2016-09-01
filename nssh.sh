echo "Enter FQDN of master"
read FQDN

ssh-copy-id -i ~/.ssh/id_rsa.pub $USER@$FQDN

echo "Enter FQDN for slave"
read FQDN1

ssh $USER@$FQDN1 mkdir -p .ssh

cat .ssh/id_rsa.pub | ssh $USER@$FQDN1 'cat >> .ssh/authorized_keys'

ssh $USER@$FQDN1 "chmod 700 .ssh; chmod 640 .ssh/authorized_keys"

