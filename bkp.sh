set -e
DATE=`date +"%Y-%m-%d"`
read -p "Enter  : " n3


backup() {
        read -p "Enter Server Name: " Server
        echo `ssh $Server` || echo "wrong server name"
       # echo $server_check
        #if [ $server_check == ]; then

        #else

        #fi

        
}
case_exception (){
        echo "Not a valid option, do you want to chose another service (y or n)"
        read answer
        if [ $answer == y ];
        then
                component
        else
                exit 1
        fi
}

component() {
echo -e "1.Cloudera DB\n2.Hive\n3.Hbase\n4.Hue\n5.Sentry\n6.Oozie\n7.Namenode Namespace"
read component

case $component in
        1) backup
                ;;
        2) backup
                ;;
        3) backup
                ;;
        4) backup
                ;;
        5) backup
                ;;
        6) backup
                ;;
        7) backup
                ;;
        *) case_exception
                ;;
esac
}

component
