
SERVER_DOMAIN=$(cat domain.sh)
SERVER_IP=$(cat ip.sh)

echo "Testing DNS resolution for $SERVER_DOMAIN"
resolved_ip=$(host $SERVER_DOMAIN | awk '/address/{print $4}')

if [ -n "$resolved_ip" ]; then
  echo "Resolved IP: $resolved_ip"
  if [ "$resolved_ip" == "$SERVER_IP" ]; then
    echo "DNS resolution successful and matches ip.sh"
  else
    echo "DNS resolution successful but does not match ip.sh"
  fi
else
  echo "DNS resolution failed for $SERVER_DOMAIN"
fi

