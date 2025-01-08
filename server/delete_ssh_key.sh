for KEY_ID in $(doctl compute ssh-key list --format ID --no-header | grep -v 2056552); do
  doctl compute ssh-key delete "$KEY_ID" --force
done
