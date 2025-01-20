wget https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh

chmod +x install_server.sh

./install_server.sh

sudo systemctl start nginx

tmux 

cd /home/project/blog-server/

python3 bandwidth_api.py

# change name cheap

