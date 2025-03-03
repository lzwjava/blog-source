SERVER_DOMAIN=$(cat domain.sh)
SERVER_IP=$(cat ip.sh)

echo "Testing DNS resolution for $SERVER_DOMAIN"

for i in {1..10}; do
  resolved_ip=$(host $SERVER_DOMAIN | awk '/address/{print $4}')
  if [ -n "$resolved_ip" ]; then
    echo "Resolved IP: $resolved_ip"
    if [ "$resolved_ip" == "$SERVER_IP" ]; then
      echo "DNS resolution successful and matches ip.sh"
      break
    else
      echo "DNS resolution successful but does not match ip.sh"
    fi
  else
    echo "DNS resolution failed for $SERVER_DOMAIN, attempt $i"
  fi
  sleep 3
done

if [ -z "$resolved_ip" ]; then
    echo "DNS resolution failed after multiple attempts for $SERVER_DOMAIN"
fi
