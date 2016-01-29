echo "give the FQDN"
read FQDN

ssh  $USER@$FQDN mkdir -p .ssh

cat .ssh/id_rsa.pub | ssh $USER@FQDN 'cat >> .ssh/authorized_keys'

ssh $USER@FQDN "chmod 700 .ssh; chmod 640 .ssh/authorized_keys"
