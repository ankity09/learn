echo setting up NTP

yum install ntp ntpdate ntp-doc

chkconfig ntpd on

ntpdate pool.tp.org

service ntpd start

echo switching off firewall

chkconfig iptables off

/etc/init.d/iptables stop

echo disabling selinux and packagekit

grep -rl SELINUX=enforcing /etc/selinux/config | xargs sed -i 's/SELINUX=enforcing/SELINUX=disabled/g'

grep -rl enabled=1 /etc/yum/pluginconf.d/refresh-packagekit.conf | xargs sed -i 's/enabled=1/enabled=0/g'

echo downloading ambari repo 

wget -nv http://public-repo-1.hortonworks.com/ambari/centos6/2.x/updates/2.1.2/ambari.repo -O /etc/yum.repos.d/ambari.repo

yum repolist

echo adding the NTPSERVERARGS tag 

echo "NTPSERVERARGS=ipburst" >> /etc/sysconfig/network

echo "Disabling Transparent Huge Pages"

echo never > /sys/kernel/mm/redhat_transparent_hugepage/enabled

echo never > /sys/kernel/mm/redhat_transparent_hugepage/defrag
