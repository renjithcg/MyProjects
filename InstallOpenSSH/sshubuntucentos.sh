OS=`cat /proc/version | awk {'print $9}'`
SO= `cat /proc/version | awk {'print $9$10}'`
if [ "$OS" = "(Ubuntu" ]
then
echo $(apt-get install openssh-server);
elif [ "$SO" = "(RedHat" ]
then
echo $(yum install openssh-server)
else
echo "Not Supported"
exit;
fi

