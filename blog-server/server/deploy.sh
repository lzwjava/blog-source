SERVER_IP=$(cat ip.sh)
fab -H root@"$SERVER_IP" deploy

