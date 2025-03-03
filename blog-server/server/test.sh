SERVER_IP=$(cat ip.sh)

curl "http://$SERVER_IP:5000/bandwidth"

SERVER_DOMAIN=$(cat domain.sh)
curl "https://$SERVER_DOMAIN/bandwidth"
