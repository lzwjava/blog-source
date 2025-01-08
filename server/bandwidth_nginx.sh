cp /home/project/blog-server/nginx.conf /etc/nginx/sites-enabled/lzwjava.conf
sudo systemctl restart nginx


scp -r root@ip:/etc/letsencrypt/* /etc/letsencrypt/